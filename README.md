# 🚀 ASTra: Security-First, Repository-Local Action Layer

**ASTra** (AST-based Repository Action layer) is a secure "middleware" bridge for AI Developer Assistants (like GitHub Copilot or local LLM agents). It safely sits between what a developer asks an AI to do and the actual execution of those commands.

## The Problem
Integrating generative AI directly into development environments comes with two major risks:
# 🛡️ ASTra: Edge-Native Security Action Layer

![ASTra Banner](https://img.shields.io/badge/iQOO-Hackathon_2026-blue?style=for-the-badge)
![Track](https://img.shields.io/badge/Track-Developer_Tools-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)

ASTra is an edge-native execution firewall that protects developers from dangerous AI-generated commands. By turning the iQOO smartphone into a hardware security key, ASTra intercepts, grades, and sandboxes autonomous terminal commands using local LLMs on the Snapdragon NPU.

## 🌟 The Problem
When developers use autonomous AI agents (like AutoGPT or Copilot) to execute code, a hallucination can be disastrous. An AI executing `rm -rf /` or `drop database` can ruin a machine. Furthermore, sending enterprise code to cloud APIs for security checks violates privacy policies and causes immense latency.

## 🚀 The ASTra Solution
ASTra decouples generation from execution. 
1. **Laptop (Green Light):** The AI proposes a command.
2. **Office Kit Bridge:** The command is beamed to the iQOO smartphone.
3. **Snapdragon Validation:** The phone's local LLM (running entirely offline) grades the intent into 3 Risk Tiers.
4. **Execution:** 
   - 🟢 **Tier 1 (Safe):** Executed instantly.
   - 🟡 **Tier 2 (Write):** Executed strictly inside an isolated Docker Sandbox.
   - 🔴 **Tier 3 (Destructive):** Hard-blocked. Requires biometric/voice approval on the phone.

## 🏗️ Deep Technical Architecture
Unlike simple API wrappers, ASTra utilizes deep infrastructure:
* **Tree-sitter AST Slicing:** Extracts exact method-level context so small NPU models don't crash from memory overload.
* **ChromaDB / SQLite:** Local RAG (Retrieval-Augmented Generation) for offline project semantic memory.
* **Docker Sandboxing:** Ephemeral container isolation.
* **FastAPI:** CI/CD Webhook interception.

---

## 🛠️ Quick Start Guide for Judges

### 1. 1-Click Setup (Windows)
We have provided automated setup scripts to make evaluation frictionless.
```powershell
.\setup.ps1
```
*(This creates the virtual environment, installs Tree-sitter, Chroma, and Pytest).*

### 2. Activate the Environment
```powershell
.\venv\Scripts\Activate.ps1

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
