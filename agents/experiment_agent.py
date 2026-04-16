class ExperimentAgent:
    def take_action(self, issue):
        if "Database" in issue:
            return "Restart DB service"

        if "Network" in issue:
            return "Scale service replicas"

        if "Internal" in issue:
            return "Restart API service"

        return "No action taken"