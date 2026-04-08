from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomaly():
    data = np.array([[10], [12], [11], [50]])

    model = IsolationForest(contamination=0.2)
    model.fit(data)

    pred = model.predict(data)

    for i in range(len(pred)):
        if pred[i] == -1:
            print(f"⚠ Anomaly detected at value: {data[i][0]}")
