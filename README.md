# AI DevOps Agent

A local AI-powered DevOps assistant that can read files, execute terminal commands, and maintain persistent memory — powered by Ollama and LangChain.

This project runs fully offline after model download and is designed as a foundation for building autonomous AI infrastructure tools.

---

## Features

- 📂 File reading and analysis
- 🖥 Terminal command execution
- 🧠 Persistent memory across sessions
- 🤖 Local LLM via Ollama (no cloud required)
- ⚡ Fast Python environment management with uv
- 🔒 Safety-first design with command awareness

---

## Tech Stack

- Python 3.10+
- uv (modern Python package manager)
- LangChain
- Ollama
- Qwen2.5 LLM
- Local filesystem memory store

---

## Prerequisites

Before running the agent, install:

### 1. Python

Python 3.10 or higher

Check:

```
python --version
```

---

### 2. Install uv

uv replaces pip + venv and manages dependencies automatically.

Windows:

```
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOS/Linux:

```
curl -Ls https://astral.sh/uv/install.sh | sh
```

Verify:

```
uv --version
```

---

### 3. Install Ollama

Download from:

https://ollama.com/download

Start Ollama and pull the model:

```
ollama pull qwen2.5:7b
```

Test:

```
ollama run qwen2.5:7b
```

If it responds, you’re ready.

---

## Setup

Clone the repo:

```
git clone https://github.com/yuriym79/ai-devops-agent
cd ai-devops-agent
```

Install dependencies:

```
uv sync
```

This installs all dependencies from the lockfile.

---

## Run the Agent

```
uv run python main.py
```

Example usage:

```
>> read log.txt and explain what happened
>> run docker ps
>> summarize previous errors
```

The agent will read files, execute commands, and store memory in:

```
memory/history.txt
```

---

## Project Structure

```
ai-devops-agent/
├── main.py
├── memory/
│   └── history.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Safety Warning

This agent can execute terminal commands.

Do NOT run destructive commands like:

```
rm -rf /
del /s /q
```

Always review commands before allowing execution.

This project is for development and experimentation.

---

## How Memory Works

The agent logs interactions to:

```
memory/history.txt
```

This allows it to:

- recall past sessions
- track recurring issues
- provide context-aware responses

Memory is simple and transparent by design.

---

## Why This Project Exists

This project explores:

- local AI autonomy
- DevOps automation
- safe tool-using agents
- offline AI workflows
- modern Python packaging

It serves as a base for future autonomous infrastructure assistants.

---

## Roadmap

Planned upgrades:

- log analysis tool
- Docker/Kubernetes integration
- autonomous troubleshooting loop
- command sandboxing
- plugin system
- structured memory database
- web dashboard

---

## Contributing

Pull requests welcome.

Ideas for tools and automation are encouraged.

---

## License

MIT License

---

## Author

Yuriy Mikhailidi  
Building local AI systems and DevOps tooling.