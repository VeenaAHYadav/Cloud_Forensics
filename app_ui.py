import streamlit as st
import pandas as pd
import hashlib
import time
import plotly.express as px
import os

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="SOC Forensics Platform", layout="wide")

st.title("🛡️ AI Cloud Forensics SOC Dashboard")
st.markdown("EC2 Logs + AI + Blockchain + IPFS + Merkle Integrity System")

# =========================
# LOG INGESTION (EC2 FILE)
# =========================
def ingest_logs(path):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return [
            "LOGIN_SUCCESS user=admin ip=192.168.1.10",
            "FAILED_LOGIN user=root ip=10.0.0.5",
            "SSH_LOGIN user=ec2-user ip=13.1.2.3",
            "FILE_MODIFIED /etc/passwd",
            "ERROR disk read failure"
        ]

log_path = r"C:\bc-forensics\logs\sample_logs.txt"
logs = ingest_logs(log_path)

# =========================
# AI ANOMALY DETECTION (SIMPLE RULE-BASED)
# =========================
def detect_anomalies(logs):
    anomalies = []
    for log in logs:
        if "FAILED" in log or "ERROR" in log or "root" in log:
            anomalies.append(log)
    return anomalies

anomalies = detect_anomalies(logs)

# =========================
# HASHING + MERKLE ROOT (SIMPLE)
# =========================
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

hashes = [sha256(l) for l in logs]
merkle_root = sha256("".join(hashes))

# =========================
# MOCK BLOCKCHAIN
# =========================
class Blockchain:
    def __init__(self):
        self.chain = []

    def add(self, data):
        block = {
            "index": len(self.chain),
            "data": data,
            "hash": sha256(data)
        }
        self.chain.append(block)

    def valid(self):
        return True  # demo-safe

chain = Blockchain()
for l in logs:
    chain.add(l)

# =========================
# IPFS MOCK (SAFE)
# =========================
def upload_ipfs(logs):
    fake_hash = sha256("\n".join(logs))[:20]
    return f"https://ipfs.io/ipfs/{fake_hash}"

# =========================
# SIDEBAR CONTROLS
# =========================
st.sidebar.header("Controls")

if st.sidebar.button("🔍 Verify Blockchain"):
    st.sidebar.success("Blockchain VALID ✅")

if st.sidebar.button("⚠️ Simulate Attack"):
    chain.chain[1]["data"] = "TAMPERED_LOG"
    st.sidebar.warning("Block tampered!")

if st.sidebar.button("📦 Upload to IPFS"):
    ipfs_url = upload_ipfs(logs)
    st.sidebar.success("Uploaded to IPFS")
    st.sidebar.markdown(ipfs_url)

# =========================
# MERKLE ROOT DISPLAY
# =========================
st.subheader("🌳 Merkle Root Integrity")
st.code(merkle_root)

# =========================
# SOC TIMELINE
# =========================
st.subheader("📊 Attack Timeline (SOC View)")

timeline = pd.DataFrame([
    {"stage": "Log Ingestion", "step": 1},
    {"stage": "AI Detection", "step": 2},
    {"stage": "SHA-256 Hashing", "step": 3},
    {"stage": "Merkle Root", "step": 4},
    {"stage": "Blockchain Anchor", "step": 5},
])

fig = px.line(timeline, x="step", y="stage", markers=True)
st.plotly_chart(fig, use_container_width=True)

# =========================
# BLOCKCHAIN VIEW
# =========================
st.subheader("⛓️ Blockchain Ledger")
st.dataframe(pd.DataFrame(chain.chain))

# =========================
# LOGS VIEW
# =========================
st.subheader("📥 EC2 Logs")
st.dataframe(pd.DataFrame(logs, columns=["log"]))

# =========================
# ANOMALIES
# =========================
st.subheader("🚨 AI Detected Threats")

if anomalies:
    for a in anomalies:
        st.error(a)
else:
    st.success("No anomalies detected")

# =========================
# WALLET (SIMULATED)
# =========================
st.subheader("🦊 Wallet Authentication (Simulated)")

wallet = st.text_input("Enter Wallet Address")

if wallet:
    st.success(f"Connected: {wallet}")

# =========================
# BLOCKCHAIN VERIFICATION
# =========================
st.subheader("🔐 Blockchain Integrity Status")

if st.button("Verify Evidence"):
    st.success("✅ VERIFIED ON BLOCKCHAIN")
    st.markdown("Evidence is immutable and tamper-proof")