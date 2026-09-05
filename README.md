# 🚀 ASTra: Security-First, Repository-Local Action Layer

**ASTra** (AST-based Repository Action layer) is a secure "middleware" bridge for AI Developer Assistants (like GitHub Copilot or local LLM agents). It safely sits between what a developer asks an AI to do and the actual execution of those commands.

## The Problem
Integrating generative AI directly into development environments comes with two major risks:
1. **Context Blindness (Hallucinations):** Feeding an entire 2,000-line file to an AI to review a 3-line change overwhelms the model, leading to hallucinations.
2. **Unsafe Execution:** Allowing autonomous agents to execute shell commands directly on a host machine is extremely dangerous (e.g., executing `rm -rf /` or dropping a database).

## Our Solution (Architecture)
ASTra decouples generation from execution through five core components:

1. **Method-Level AST Slicer:** Uses `tree-sitter` to pinpoint changed lines and extract *only* the specific function/class enclosing it, drastically reducing prompt bloat.
2. **Local RAG Retrieval:** Uses `ChromaDB` to build an offline vector database of semantic code chunks, giving the AI hyper-relevant context.
3. **LLM Policy Gate:** An LLM acts as a security guard, reading proposed commands and assigning them a Risk Tier (1=Safe, 2=Write, 3=Destructive).
4. **Docker Sandbox Executor:** Safely executes Tier 1/2 commands inside an isolated Docker container, while completely blocking Tier 3 commands pending explicit human approval.
5. **Evidence Explanation Engine:** Links sandbox execution outputs back to the original AST slice to generate transparent Evidence Reports.

---

## 🛠️ Quick Start & Setup

We have included automated setup scripts for judges to test ASTra quickly!

### 1. Run the Setup Script
**Windows (PowerShell):**
```powershell
.\setup.ps1
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Add your API Key
The setup script creates an `.env` file. Open it and add your OpenAI API key (or point it to a local Ollama instance):
```
OPENAI_API_KEY=your_key_here
```

---

## 💻 Running the Demo

Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

### Demo 1: Method-Level AST Context Slicing
See how ASTra intelligently extracts just a specific method rather than feeding the LLM an entire file.
```bash
python examples/diff_review.py
```

### Demo 2: The Security Policy Gate
See the LLM intercept and classify intents dynamically.

**Safe Execution (Tier 1):**
```bash
python cli.py execute "echo Hello World"
```

**Blocked Destructive Execution (Tier 3):**
```bash
python cli.py execute "rm -rf .git"
```

### Demo 3: The CI/CD GitHub Webhook
Start the ASTra FastAPI webhook server to intercept GitHub Pull Requests in real-time.
```bash
# Terminal 1: Start the Server
python cli.py serve
```
```bash
# Terminal 2: Send a Mock PR Payload
curl -X POST http://127.0.0.1:8000/webhook -H "Content-Type: application/json" -d @examples/mock_pr_payload.json
```
