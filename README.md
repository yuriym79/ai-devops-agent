# AI DevOps Agent (Local LLM)

A local AI-powered DevOps assistant that can read files, analyze logs, run terminal commands, and remember past interactions — all offline using a local large language model.

This project explores tool-using AI agents, memory persistence, and autonomous system reasoning without relying on cloud APIs.

## 🚀 Features

- Local LLM (runs fully offline)
- Tool-using agent architecture
- File inspection
- Terminal command execution
- Log analysis
- Persistent memory system
- DevOps assistant behavior
- Lightweight CLI interface

The agent acts like a private AI sysadmin and coding copilot.

---

## 🧠 Architecture

User CLI
↓
Agent Brain (Python)
↓
Local LLM (Ollama)
↓
Tools:
• File reader
• Terminal executor
• Memory store

---
The agent decides when to use tools, executes them, and reasons about results.

---

## 🛠 Tech Stack

- Python 3
- Ollama (local LLM runtime)
- Qwen / Llama models
- subprocess (system execution)
- File-based memory persistence

No cloud dependencies.

---

## ✅ Prerequisites

Before running the AI DevOps Agent, make sure your system meets the following requirements.

---

### 1. Python

Python **3.10 or newer** is required.

Verify installation:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed:

👉 https://www.python.org/downloads/

---

### 2. Ollama (Local LLM Runtime)

This project runs entirely offline using Ollama.

Install Ollama:

👉 https://ollama.com/download

After installation, pull a supported model:

```bash
ollama pull qwen2.5:7b
```

Test the model:

```bash
ollama run qwen2.5:7b
```

If the model responds, Ollama is working correctly.

---

### 3. Operating System

Tested environments:

- Windows (PowerShell / MINGW / Git Bash)
- macOS
- Linux

Virtual environment activation:

**Windows**

```bash
source venv/Scripts/activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

### 4. Hardware Recommendation

For best performance:

- GPU with **8GB+ VRAM** recommended
- **16GB system RAM** minimum
- SSD storage

The agent can run on CPU-only systems, but responses will be slower.

---

### 5. Internet Requirement (First Run Only)

Internet access is required only once to download the model:

```bash
ollama pull qwen2.5:7b
```

After that, the agent runs fully offline.

---

## 📦 Installation

### 1. Install Ollama

https://ollama.com/download

Pull a model: 
```
ollama pull qwen2.5:7b
```
Test:
```
ollama run qwen2.5:7b
```

---

### 2. Clone project

```
git clone https://github.com/yuriym79/ai-devops-agent/tree/main
cd ai-devops-agent
```

---

### 3. Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```
pip install ollama
```

---

### 5. Run the agent

```
python main.py
```

---

## 🧪 Example Usage

- read log.txt and explain what happened
- run terminal docker ps
- summarize my past errors
- review this config file

```
>> read log.txt and explain what happened
>> run terminal ls
>> what errors have I seen before?
```

The agent can inspect your system and reason about technical issues.

---

## 🧠 Memory System

Memory lets the agent reference past sessions to provide context-aware analysis.

The agent stores history in: memory/history.txt
It remembers:

- past logs
- tool results
- user queries
- explanations

This allows context-aware debugging across sessions.

---

## 🔒 Privacy & Security

Everything runs locally:

- no cloud APIs
- no external data transmission
- full offline operation

Your logs and files never leave your machine.

Security / Safety Note

Since it executes local commands in a powerful way, a short warning about safety (e.g., “Be careful with commands like rm -rf /”) is useful.

---

## 🎯 Goals

This project explores:

- AI tool-using agents
- local LLM orchestration
- DevOps automation
- autonomous reasoning loops
- memory persistence in AI systems

It serves as a foundation for building:

- AI sysadmin assistants
- coding copilots
- debugging agents
- research bots
- autonomous repair loops

---

## 🚧 Future Roadmap

- Docker/Kubernetes inspector
- Git intelligence agent
- autonomous debugging loop
- VS Code integration
- multi-agent architecture
- web dashboard
- plugin system
- voice interface

---

## 📜 License

MIT License

---

## ✨ Author

Built as an experimental AI engineering project exploring local agent systems.