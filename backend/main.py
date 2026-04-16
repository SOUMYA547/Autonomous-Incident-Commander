from fastapi import FastAPI
from agents.log_agent import LogAgent
from agents.reasoning_agent import ReasoningAgent
from agents.experiment_agent import ExperimentAgent

app = FastAPI()

log_agent = LogAgent()
reasoning_agent = ReasoningAgent()
experiment_agent = ExperimentAgent()

@app.post("/analyze")
def analyze(logs: list[str]):
    anomalies = log_agent.process_logs(logs)
    issue = reasoning_agent.analyze(anomalies)
    action = experiment_agent.take_action(issue)

    return {
        "anomalies": anomalies,
        "issue": issue,
        "action": action
    }