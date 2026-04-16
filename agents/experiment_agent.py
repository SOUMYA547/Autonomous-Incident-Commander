import os

class ExperimentAgent:
    def take_action(self, issue):
        if "Database" in issue:
            return "Restarting DB container..."

        if "network" in issue:
            return "Scaling service..."

        return "No action taken"