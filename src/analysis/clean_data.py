from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.utils.data_loader import save_processed_data


REQUIRED_COLUMNS = {
    "timestamp",
    "port_name",
    "route",
    "vessel_imo",
    "vessel_type",
    "turnaround_hours",
    "cargo_teu",
    "avg_speed_knots",
    "delay_status",
}

NUMERIC_COLUMNS = ["turnaround_hours", "cargo_teu", "avg_speed_knots"]
TEXT_COLUMNS = ["port_name", "route", "vessel_imo", "vessel_type", "delay_status"]


@dataclass(frozen=True)
class CleaningResult:
    raw: pd.DataFrame
    cleaned: pd.DataFrame
    issues: list[str]
    output_path: str


def validate_columns(df: pd.DataFrame) -> None:
    missing = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"CSV 缺少必要欄位：{joined}")


def _fill_numeric_by_port(df: pd.DataFrame, column: str) -> pd.Series:
    grouped_median = df.groupby("port_name")[column].transform("median")
    overall_median = df[column].median()
    if np.isnan(overall_median):
        overall_median = 0
    return df[column].fillna(grouped_median).fillna(overall_median)


def clean_shipping_data(df: pd.DataFrame, persist: bool = True) -> CleaningResult:
    """Clean shipping records and optionally write the processed CSV."""
    raw = df.copy()
    validate_columns(raw)

    cleaned = raw.copy()
    issues: list[str] = []

    cleaned["timestamp"] = pd.to_datetime(cleaned["timestamp"], errors="coerce")
    bad_dates = int(cleaned["timestamp"].isna().sum())
    if bad_dates:
        issues.append(f"移除 {bad_dates} 筆無法解析 timestamp 的資料")
    cleaned = cleaned.dropna(subset=["timestamp"])

    for column in TEXT_COLUMNS:
        cleaned[column] = cleaned[column].astype("string").str.strip()
        cleaned[column] = cleaned[column].replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})

    cleaned["port_name"] = cleaned["port_name"].fillna("Unknown Port")
    cleaned["route"] = cleaned["route"].fillna("Unknown Route")
    cleaned["vessel_type"] = cleaned["vessel_type"].fillna("Unknown Vessel")
    cleaned["delay_status"] = cleaned["delay_status"].fillna("Unknown")
    cleaned["vessel_imo"] = cleaned["vessel_imo"].fillna("IMO0000000")

    for column in NUMERIC_COLUMNS:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    before_bounds = len(cleaned)
    cleaned = cleaned[
        cleaned["turnaround_hours"].isna()
        | cleaned["turnaround_hours"].between(0, 168)
    ]
    cleaned = cleaned[cleaned["cargo_teu"].isna() | cleaned["cargo_teu"].between(0, 30000)]
    cleaned = cleaned[cleaned["avg_speed_knots"].isna() | cleaned["avg_speed_knots"].between(0, 40)]
    removed_bounds = before_bounds - len(cleaned)
    if removed_bounds:
        issues.append(f"移除 {removed_bounds} 筆超出合理營運範圍的資料")

    for column in NUMERIC_COLUMNS:
        missing = int(cleaned[column].isna().sum())
        if missing:
            issues.append(f"{column} 以港口中位數補齊 {missing} 筆缺失值")
        cleaned[column] = _fill_numeric_by_port(cleaned, column)

    before_dupes = len(cleaned)
    cleaned = cleaned.drop_duplicates(subset=["timestamp", "port_name", "vessel_imo"])
    removed_dupes = before_dupes - len(cleaned)
    if removed_dupes:
        issues.append(f"移除 {removed_dupes} 筆重複船舶日誌")

    cleaned["date"] = cleaned["timestamp"].dt.date
    cleaned["month"] = cleaned["timestamp"].dt.to_period("M").astype(str)
    cleaned["is_delayed"] = cleaned["delay_status"].str.lower().eq("delayed")
    cleaned = cleaned.sort_values(["timestamp", "port_name", "vessel_imo"]).reset_index(drop=True)

    output_path = ""
    if persist:
        output_path = str(save_processed_data(cleaned))

    if not issues:
        issues.append("資料格式完整，未偵測到需要修正的重大問題")

    return CleaningResult(raw=raw, cleaned=cleaned, issues=issues, output_path=output_path)
