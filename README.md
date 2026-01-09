# End-to-End Data Engineering Project

This project demonstrates a **complete data engineering pipeline**
from raw data ingestion to analytics-ready output using
industry best practices.

---

## 🏗 Architecture

Public API  
→ Raw Data Layer (JSON)  
→ Transformation Layer  
→ Processed Data (Parquet)

---

## 🧰 Tech Stack
- Python
- Pandas
- Requests
- Parquet
- Data Lake Architecture (Raw / Processed)

---

## 📂 Project Structure

end-to-end-data-engineering-project/
├── data/
│   ├── raw/        # Immutable raw API data (JSON)
│   └── processed/  # Cleaned analytics-ready data (Parquet)
├── src/
│   ├── ingest_api_data.py
│   └── transform_raw_data.py
├── docs/
└── README.md

---

## ⚙️ Pipeline Flow

### 1️⃣ Data Ingestion
- Fetches data from a public API
- Stores timestamped raw JSON files
- Ensures immutability of raw data

Script:

---

### 2️⃣ Data Transformation
- Reads latest raw JSON file
- Normalizes nested data
- Writes columnar Parquet output

Script:

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/ingest_api_data.py
python src/transform_raw_data.py

### Commit message:

Key Data Engineering Concepts Demonstrated

Data lake layering (raw → processed)

Idempotent ingestion

Schema normalization

Columnar storage (Parquet)

Production-style project structure
\
