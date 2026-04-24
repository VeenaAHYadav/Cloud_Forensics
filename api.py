# api.py
from flask import Flask, jsonify
from ingestion.ingest import ingest_logs
from verification.verifier import verify

app = Flask(__name__)

@app.route("/verify", methods=["GET"])
def verify_logs():
    logs = ingest_logs()
    results = verify(logs)
    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000)