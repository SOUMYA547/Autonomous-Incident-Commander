class DependencyMapper:
    def map_services(self):
        return {
            "auth": ["db"],
            "payment": ["auth", "db"]
        }