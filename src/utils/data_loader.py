from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "sample_shipping_data.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_shipping_data.csv"


def load_sample_data() -> pd.DataFrame:
    """Load the bundled shipping dataset."""
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Sample data not found: {RAW_DATA_PATH}")
    return pd.read_csv(RAW_DATA_PATH)


def load_uploaded_csv(file_path: str | Path | None) -> pd.DataFrame:
    """Load an uploaded CSV file, falling back to the bundled sample data."""
    if file_path is None:
        return load_sample_data()
    return pd.read_csv(file_path)


def save_processed_data(df: pd.DataFrame, path: Path = PROCESSED_DATA_PATH) -> Path:
    """Persist the cleaned dataset and return the output path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
