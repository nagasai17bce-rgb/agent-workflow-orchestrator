class Service:
    def __init__(self):
        self.runs = 0

    def run(self, value: str):
        self.runs += 1
        return {
            "workflow_id": f"run-{self.runs}",
            "input": value,
            "steps": [{"name": x, "status": "completed"} for x in ("plan", "retrieve", "act", "verify")],
            "retries": 0,
            "checkpoint": "verify",
        }
