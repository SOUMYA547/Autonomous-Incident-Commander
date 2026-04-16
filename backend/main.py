from fastapi import FastAPI
from agents.log_agent import LogAgent
from agents.reasoning_agent import ReasoningAgent
from agents.experiment_agent import ExperimentAgent
from agents.risk_agent import RiskAgent
from memory.incident_store import IncidentStore

app = FastAPI()

log_agent = LogAgent()
reasoning_agent = ReasoningAgent()
experiment_agent = ExperimentAgent()
risk_agent = RiskAgent()
memory = IncidentStore()

@app.post("/analyze")
def analyze(logs: list[str]):
    anomalies = log_agent.process_logs(logs)
    issue = reasoning_agent.analyze(anomalies)

    safe = risk_agent.evaluate(issue)

    if safe:
        action = experiment_agent.take_action(issue)
    else:
        action = "Blocked due to risk"

    memory.store(logs, issue, action)

    return {
        "anomalies": anomalies,
        "issue": issue,
        "action": action
    }