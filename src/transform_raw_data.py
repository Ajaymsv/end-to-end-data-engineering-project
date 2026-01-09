"""
Transform raw API data into analytics-ready format
Use case: Data cleaning and normalization
"""

import json
import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")


def load_latest_raw_file() -> dict:
    """Load the latest raw JSON file"""
    files = list(RAW_DATA_PATH.glob("*.json"))
    if not files:
        raise FileNotFoundError("No raw data files found")

    latest_file = max(files, key=lambda x: x.stat().st_mtime)

    with open(latest_file, "r") as f:
        return json.load(f)


def transform_data(raw_data: dict) -> pd.DataFrame:
    """Transform raw API response to tabular format"""
    entries = raw_data.get("entries", [])

    df = pd.DataFrame(entries)
    df = df[["API", "Category", "Description", "HTTPS", "Cors", "Link"]]

    return df


def save_processed_data(df: pd.DataFrame) -> None:
    """Save processed data as Parquet"""
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_PATH / "api_data.parquet"

    df.to_parquet(output_path, index=False)
    print(f"Processed data saved to {output_path}")


if __name__ == "__main__":
    raw_data = load_latest_raw_file()
    transformed_df = transform_data(raw_data)
    save_processed_data(transformed_df)
