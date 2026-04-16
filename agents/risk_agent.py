class RiskAgent:
    def evaluate(self, issue):
        if "Database" in issue:
            return False  # risky

        return True