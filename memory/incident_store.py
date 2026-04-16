class IncidentStore:
    def __init__(self):
        self.store_data = []

    def store(self, logs, issue, action):
        self.store_data.append({
            "logs": logs,
            "issue": issue,
            "action": action
        })

    def get_all(self):
        return self.store_data