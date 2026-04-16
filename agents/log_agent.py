from ml.anomaly_detection import AnomalyDetector
import numpy as np

class LogAgent:
    def __init__(self):
        self.detector = AnomalyDetector()

    def process_logs(self, logs):
        # Convert logs → numerical features (simplified)
        features = np.array([[len(log)] for log in logs])

        self.detector.train(features)
        result = self.detector.predict(features)

        anomalies = [logs[i] for i in range(len(logs)) if result[i] == -1]

        return anomalies