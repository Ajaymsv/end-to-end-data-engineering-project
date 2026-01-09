"""
Ingest data from a public API and store it in raw layer
Use case: Raw data ingestion for analytics pipeline
"""

import json
import requests
from datetime import datetime
from pathlib import Path


RAW_DATA_PATH = Path("data/raw")


def fetch_api_data(url: str) -> dict:
    """Fetch data from external API"""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def save_raw_data(data: dict) -> None:
    """Save raw API response to JSON file"""
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DATA_PATH / f"api_data_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f)

    print(f"Raw data saved to {file_path}")


if __name__ == "__main__":
    API_URL = "https://api.publicapis.org/entries"
    api_data = fetch_api_data(API_URL)
    save_raw_data(api_data)
