from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path("/tmp") / "shipping-dashboard-mpl"))

import matplotlib.pyplot as plt
import pandas as pd


METRIC_LABELS = {
    "turnaround_hours": "Turnaround Hours",
    "cargo_teu": "Cargo Volume (TEU)",
    "avg_speed_knots": "Average Speed (Knots)",
    "delay_rate": "Delay Rate",
}


def filter_records(
    df: pd.DataFrame,
    port: str = "All",
    route: str = "All",
    vessel_type: str = "All",
    min_cargo_teu: int = 0,
) -> pd.DataFrame:
    result = df.copy()
    if port != "All":
        result = result[result["port_name"] == port]
    if route != "All":
        result = result[result["route"] == route]
    if vessel_type != "All":
        result = result[result["vessel_type"] == vessel_type]
    result = result[result["cargo_teu"] >= min_cargo_teu]
    return result.reset_index(drop=True)


def kpi_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(
            [{"records": 0, "total_teu": 0, "avg_turnaround_hours": 0, "avg_speed_knots": 0, "delay_rate": 0}]
        )

    return pd.DataFrame(
        [
            {
                "records": len(df),
                "total_teu": round(float(df["cargo_teu"].sum()), 2),
                "avg_turnaround_hours": round(float(df["turnaround_hours"].mean()), 2),
                "avg_speed_knots": round(float(df["avg_speed_knots"].mean()), 2),
                "delay_rate": round(float(df["is_delayed"].mean() * 100), 2),
            }
        ]
    )


def port_performance(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["port_name", "records", "total_teu", "avg_turnaround_hours", "delay_rate"])

    summary = (
        df.groupby("port_name")
        .agg(
            records=("vessel_imo", "count"),
            total_teu=("cargo_teu", "sum"),
            avg_turnaround_hours=("turnaround_hours", "mean"),
            avg_speed_knots=("avg_speed_knots", "mean"),
            delay_rate=("is_delayed", "mean"),
        )
        .reset_index()
    )
    summary["delay_rate"] = (summary["delay_rate"] * 100).round(2)
    for column in ["total_teu", "avg_turnaround_hours", "avg_speed_knots"]:
        summary[column] = summary[column].round(2)
    return summary.sort_values("total_teu", ascending=False).reset_index(drop=True)


def route_performance(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["route", "records", "total_teu", "avg_turnaround_hours", "delay_rate"])

    summary = (
        df.groupby("route")
        .agg(
            records=("vessel_imo", "count"),
            total_teu=("cargo_teu", "sum"),
            avg_turnaround_hours=("turnaround_hours", "mean"),
            delay_rate=("is_delayed", "mean"),
        )
        .reset_index()
    )
    summary["delay_rate"] = (summary["delay_rate"] * 100).round(2)
    summary["total_teu"] = summary["total_teu"].round(2)
    summary["avg_turnaround_hours"] = summary["avg_turnaround_hours"].round(2)
    return summary.sort_values("avg_turnaround_hours", ascending=False).reset_index(drop=True)


def build_insights(df: pd.DataFrame) -> str:
    if df.empty:
        return "目前篩選條件沒有資料，請調整港口、航線或最低貨櫃量。"

    port_table = port_performance(df)
    busiest = port_table.iloc[0]
    slowest = port_table.sort_values("avg_turnaround_hours", ascending=False).iloc[0]
    delay_rate = df["is_delayed"].mean() * 100
    total_teu = df["cargo_teu"].sum()

    return (
        f"共分析 {len(df)} 筆航運紀錄，總吞吐量 {total_teu:,.0f} TEU。"
        f"吞吐量最高港口為 {busiest['port_name']}，累計 {busiest['total_teu']:,.0f} TEU。"
        f"平均滯港時間最高的是 {slowest['port_name']}，約 {slowest['avg_turnaround_hours']:.1f} 小時。"
        f"整體延誤率為 {delay_rate:.1f}%。"
    )


def plot_metric(df: pd.DataFrame, metric: str, chart_type: str):
    fig, ax = plt.subplots(figsize=(9, 4.8))
    color = "#2563eb"

    if df.empty:
        ax.text(0.5, 0.5, "No records match current filters", ha="center", va="center", fontsize=13)
        ax.set_axis_off()
        fig.tight_layout()
        return fig

    if metric == "delay_rate":
        metric_series = df.assign(delay_rate=df["is_delayed"].astype(float))
        value_column = "delay_rate"
    else:
        metric_series = df
        value_column = metric

    label = METRIC_LABELS.get(metric, metric)

    if chart_type == "Trend Line Chart":
        trend = metric_series.groupby("date")[value_column].mean().reset_index()
        if metric == "delay_rate":
            trend[value_column] = trend[value_column] * 100
        ax.plot(trend["date"], trend[value_column], marker="o", linewidth=2.2, color=color)
        ax.set_xlabel("Date")
        ax.set_ylabel(label)
        ax.set_title(f"{label} Daily Trend")
        ax.tick_params(axis="x", rotation=35)
    elif chart_type == "Port Average Bar Chart":
        by_port = metric_series.groupby("port_name")[value_column].mean().sort_values(ascending=False)
        if metric == "delay_rate":
            by_port = by_port * 100
        by_port.plot(kind="bar", ax=ax, color=["#2563eb", "#0891b2", "#16a34a", "#f59e0b", "#dc2626"])
        ax.set_xlabel("Port")
        ax.set_ylabel(label)
        ax.set_title(f"{label} by Port")
        ax.tick_params(axis="x", rotation=25)
    else:
        by_route = metric_series.groupby("route")[value_column].mean().sort_values(ascending=False)
        if metric == "delay_rate":
            by_route = by_route * 100
        by_route.plot(kind="barh", ax=ax, color="#0f766e")
        ax.set_xlabel(label)
        ax.set_ylabel("Route")
        ax.set_title(f"{label} by Route")

    ax.grid(True, axis="y", alpha=0.25)
    fig.tight_layout()
    return fig
