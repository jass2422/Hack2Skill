 # Hack2Skill
 # 🚨 AI Incident Commander

AI-powered incident analysis and intelligent remediation engine designed for modern cloud-native systems.

Built for hackathon submission.

🌍 Live Demo

🔗 https://ai-incident-commander.onrender.com

📌 Problem Statement

Modern production systems face frequent incidents:

Application crashes

Database connection exhaustion

Kubernetes pod failures

Deployment rollbacks

Sudden traffic spikes

Engineers manually:

Inspect logs

Check metrics

Identify root causes

Suggest remediation steps

This process is slow and reactive.

💡 Solution

AI Incident Commander automates:

1️⃣ Incident analysis
2️⃣ Root cause detection
3️⃣ Remediation suggestion
4️⃣ Auto-remediation readiness
5️⃣ MCP-compatible agent architecture

🏗️ Architecture Overview
Frontend

HTML

CSS

Simple interactive UI

Backend

FastAPI (Python)

REST API endpoints

Gemini AI integration

AI Engine

Gemini 2.5 Flash

Root cause reasoning

Remediation recommendation

Deployment

Render (Production Hosting)

Designed to be:

MCP-compatible

Agent-extensible

Kubernetes-ready

CI/CD integratable

⚙️ How It Works

1️⃣ User enters incident description
2️⃣ Backend sends structured prompt to Gemini
3️⃣ AI analyzes incident context
4️⃣ Returns:

Incident ID

Likely root cause

Recommended action

Confidence score
5️⃣ UI renders structured response

🔮 Future Architecture (Agent Mode)

This system is designed to evolve into:

🧠 Auto-Remediation Agent

Execute kubectl commands

Scale deployments

Restart failing pods

Roll back faulty releases

☸️ Kubernetes Diagnostics

Check pod health

Analyze logs

Monitor CPU & memory

Detect crash loops

💬 Slack / Teams Alerts

Send root cause

Severity level

Confidence score

Action taken

🔄 CI/CD Integration

Detect deployment failure spikes

Trigger automated rollback

Open GitHub issue

Notify DevOps channel

🧩 MCP Compatibility

The project follows an MCP-style architecture:

Event Trigger

Diagnostic Tool

AI Reasoning Engine

Policy Decision Layer

Execution Tool

This allows future integration with:

Archestra Platform

Agentic orchestration systems

Autonomous infrastructure workflows

📁 Project Structure
incident-mcp-server/
│
├── main.py
├── templates/
├── static/
├── requirements.txt
├── requirements.md
├── design.md
└── README.md

🛠️ Local Setup
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd incident-mcp-server

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000


Visit:

http://localhost:8000

🧠 AI Prompting Strategy

Structured incident parsing

Infrastructure-aware reasoning

Confidence scoring

Action-oriented output

🚀 Hackathon Submission Includes

✅ Working deployed app
✅ GitHub repository
✅ requirements.md
✅ design.md
✅ Presentation deck
✅ MCP-style architecture diagram

📈 Impact

This project moves incident management from:

Manual Debugging → AI-Assisted Analysis → Autonomous Remediation

👩‍💻 Author

Jasmeen Shaikh


