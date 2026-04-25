from core.blockchain import Blockchain
from ingest.log_ingestor import ingest_logs
from core.anomaly_ai import LogAI
from core.merkle_treee import MerkleTree

from flask import Flask, jsonify
from aws_ingestion.s3_fetcher import fetch_logs
from processor.log_parser import parse_logs
from core.hasher import hash_log
from core.blockchain import Blockchain

# 🔥 REAL AWS LOGS
logs = ingest_logs("/aws/lambda/your-log-group-name")

# Build Merkle Tree from logs
tree = MerkleTree(logs)

print("\n🌳 Merkle Root Hash:")
print(tree.get_root())

chain = Blockchain()

# 🔥 REAL AWS LOGS
logs = ingest_logs("/aws/lambda/your-log-group-name")

ai = LogAI()
ai.train(logs)
anomalies = ai.detect(logs)

print("\n🚨 Anomalies:")
for a in anomalies:
    print(a)

for log in logs:
    chain.add_block(log)

print("\n🛡️ Chain Valid:", chain.is_valid())

# Step 1: ingest logs
logs = ingest_logs()

# Step 2: AI anomaly detection
ai.train(logs)
anomalies = ai.detect(logs)

print("\n🚨 Anomalies Detected:")
for a in anomalies:
    print(a)

# Step 3: store logs in blockchain
for log in logs:
    chain.add_block(log)

# Step 4: output blockchain
print("\n⛓️ Blockchain:")
for block in chain.export():
    print(block)

# Step 5: integrity check
print("\n🛡️ Integrity Valid:", chain.is_valid())

# Step 6: tamper demo
chain.chain[2].data = "HACKED LOG"
print("\n⚠️ After Tamper:", chain.is_valid())

from flask import Flask, jsonify
from aws_ingestion.s3_fetcher import fetch_logs
from processor.log_parser import parse_logs
from core.hasher import hash_log
from core.blockchain import Blockchain

app = Flask(__name__)
chain = Blockchain()

@app.route("/run_pipeline")
def run_pipeline():

    raw_logs = fetch_logs()
    logs = parse_logs(raw_logs)

    for log in logs:
        h = hash_log(log)
        chain.add_block(log, h)

    return jsonify(chain.get_chain())

@app.route("/chain")
def get_chain():
    return jsonify(chain.get_chain())

if __name__ == "__main__":
    app.run(debug=True)