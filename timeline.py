import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🛡️ SOC Attack Timeline Visualization")

data = [
    {"stage": "AWS Log Ingestion", "time": 1},
    {"stage": "AI Anomaly Detection", "time": 2},
    {"stage": "SHA-256 Hashing", "time": 3},
    {"stage": "Merkle Root Creation", "time": 4},
    {"stage": "Blockchain Anchoring", "time": 5},
]

df = pd.DataFrame(data)

fig = px.line(df, x="time", y="stage", markers=True, title="Attack Timeline (Forensic Pipeline)")
st.plotly_chart(fig)