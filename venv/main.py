from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import random
import time
import os

app = FastAPI(title="AI Incident Commander MCP Server")

# -------- Static Files --------

app.mount("/static", StaticFiles(directory="static"), name="static")

# -------- Models --------

class IncidentRequest(BaseModel):
    description: str

class IncidentResponse(BaseModel):
    incident: str
    likely_root_cause: str
    recommended_action: str
    confidence: str

# -------- Homepage --------

@app.get("/", response_class=HTMLResponse)
def homepage():
    with open("templates/index.html") as f:
        return f.read()

# -------- Health --------

@app.get("/health")
def health():
    return {"status": "ok"}

# -------- Tool Discovery --------

@app.get("/tools")
def list_tools():
    return {
        "tools": [
            {
                "name": "incident_analyzer",
                "description": "Analyzes production incidents and suggests root cause and remediation",
                "endpoint": "/analyze-incident",
                "method": "POST",
                "input_schema": {
                    "description": "string"
                }
            }
        ]
    }

# -------- Core Logic --------

@app.post("/analyze-incident", response_model=IncidentResponse)
def analyze_incident(req: IncidentRequest):
    time.sleep(1)

    possible_causes: List[str] = [
        "Database connection pool exhausted",
        "Memory leak in microservice",
        "Kubernetes pod crashloop",
        "External API timeout",
        "High CPU due to traffic spike"
    ]

    actions: List[str] = [
        "Scale replicas to 5",
        "Restart failing pods",
        "Rollback last deployment",
        "Increase DB connection limit",
        "Enable circuit breaker"
    ]

    return IncidentResponse(
        incident=req.description,
        likely_root_cause=random.choice(possible_causes),
        recommended_action=random.choice(actions),
        confidence=f"{random.randint(70,95)}%"
    )
