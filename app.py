# app.py
import streamlit as st
from ingestion.ingest import ingest_logs
from hashing.hasher import generate_hash
from blockchain.web3_client import store_hash
from ai_engine.detector import run_ai_detection
from verification.verifier import verify

st.title("🔐 AI Blockchain Forensics Dashboard")

logs = ingest_logs()

if st.button("Run Pipeline"):
    hashes = [generate_hash(log) for log in logs]

    for h in hashes:
        store_hash(h)

    st.success("Stored on Blockchain!")

    ai_results = run_ai_detection(logs)
    st.write(ai_results)

    verification = verify(logs)
    st.write("Verification:", verification)