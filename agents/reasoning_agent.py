class ReasoningAgent:
    def analyze(self, anomalies):
        if not anomalies:
            return "System stable"

        if any("timeout" in log for log in anomalies):
            return "Network latency issue"

        if any("DB error" in log for log in anomalies):
            return "Database failure"

        if any("500" in log for log in anomalies):
            return "Internal server error"

        return "Unknown issue"