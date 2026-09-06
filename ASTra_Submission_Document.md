# ASTra: Edge-Native Security Action Layer
**Track:** 06 - Developer Tools  
**Format:** Phone-First (Red Light / Green Light)

## 1. Executive Summary
As the software industry rapidly adopts autonomous AI coding agents (such as GitHub Copilot, AutoGPT, and local LLMs), a critical security vulnerability has emerged: **Unsafe execution.** 

If an AI hallucinates or misinterprets a prompt, it can execute terminal commands that destroy local databases, leak Intellectual Property, or wipe the user's hard drive (`rm -rf /`). Sending code to cloud models for security validation is slow, costly, and compromises code privacy.

**ASTra solves this.** We have built an execution firewall that decoupling the generation from the execution. It grades AI intents into 3 Risk Tiers *before* they touch the terminal. Instead of relying on the cloud, ASTra places the security evaluation natively on the **iQOO smartphone**, creating an Edge-Native Security Hardware Key.

## 2. The Phone-First Architecture & Office Kit
Our system flawlessly integrates the iQOO hackathon constraints to achieve 100% real-world utility:

1. **Laptop (Green Light):** The developer works on their laptop. When the AI proposes a code execution, the local terminal pauses it.
2. **Office Kit Bridge:** The proposed command and the related code snippet are beamed seamlessly to the iQOO device via Office Kit.
3. **Snapdragon NPU Validation:** The iQOO phone acts as the physical security brain. It intercepts and evaluates the threat level completely offline.

## 3. Deep Technical Infrastructure
We aren't building a basic API wrapper. We built deep, underlying infrastructure optimized for edge devices:

* **Surgical AST Slicing (Tree-Sitter):** LLMs running locally on a phone have very small memory contexts. We use C-based Tree-sitter parsing to extract *only the exact 10 lines of code* that changed. This surgical extraction prevents the Snapdragon NPU from crashing under heavy memory loads.
* **Local Offline Memory (ChromaDB):** We implemented a local RAG (Retrieval-Augmented Generation) semantic indexing system for offline memory via SQLite.
* **Ephemeral Sandboxing (Docker):** Safe commands execute instantly inside an isolated Docker container on the host machine.
* **CI/CD Interception (FastAPI):** An automated Webhook server that intercepts GitHub Pull Requests for security scanning.

## 4. Creative Phone Use (Tier 3 Approvals)
ASTra intercepts commands into 3 tiers:
* **Tier 1 (Safe):** Read-only (e.g., `echo`, `ls`). Executed automatically.
* **Tier 2 (Write):** Non-destructive (e.g., `touch`). Executed in Docker.
* **Tier 3 (Destructive):** High-risk (e.g., `rm -rf`, `drop database`). 

**The iQOO Hardware Key:** When a Tier 3 command is detected, it is hard-blocked on the laptop. A physical alert triggers on the iQOO screen. The developer must pick up the phone and use **Voice Commands ("Approve Execution")** into the phone's microphone, or use FaceID, to authorize the dangerous deployment. 

## 5. Why ASTra is the Winning Solution
ASTra protects developers, secures our code, and proves that the future of enterprise security belongs on the edge. By heavily utilizing the Snapdragon NPU, Office Kit, and the physical microphone/biometrics of the iQOO device, we have transformed a consumer smartphone into a necessary piece of enterprise developer hardware. 

We have already shipped an 11-commit, validated, fully functioning prototype repository. We are ready for the 30-hour battle.
