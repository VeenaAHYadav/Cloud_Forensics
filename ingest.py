# ingestion/ingest.py
import json

def ingest_logs(file_path="logs/sample_logs.json"):
    with open(file_path, "r") as f:
        logs = json.load(f)
    return logs