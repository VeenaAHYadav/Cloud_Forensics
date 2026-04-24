# ai_engine/detector.py
from sklearn.ensemble import IsolationForest
import pandas as pd

def run_ai_detection(logs):
    df = pd.DataFrame(logs)[["user", "action", "ip"]]

    model = IsolationForest(contamination=0.2)
    df["anomaly"] = model.fit_predict(df)

    return df