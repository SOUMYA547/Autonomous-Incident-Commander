import os
from openai import OpenAI

class ReasoningAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("sk-1234ijkl1234ijkl1234ijkl1234ijkl1234ijkl"))

    def analyze(self, anomalies):
        if not anomalies:
            return "System stable"

        prompt = f"""
You are a Site Reliability Engineer.

Analyze the following logs:
{anomalies}

1. Identify root cause
2. Explain why
3. Suggest fix
Return short answer.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content