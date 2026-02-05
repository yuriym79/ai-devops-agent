import ollama
import subprocess
import os
from datetime import datetime

MEMORY_DIR = "memory"
MEMORY_FILE = os.path.join(MEMORY_DIR, "history.txt")

SYSTEM_PROMPT = """
You are a DevOps AI assistant.
You can use tools when needed.

Available tools:
1. read_file(path) — read a file
2. terminal(cmd) — run a shell command

When you want to use a tool, respond EXACTLY in this format:

TOOL: tool_name
INPUT: argument

Otherwise respond normally.
"""

def ensure_memory():
    os.makedirs(MEMORY_DIR, exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            return f.write("=== AI Agent Memory ===\n")

def read_memory(limit=4000):
    try:
        with open(MEMORY_FILE, "r") as f:
          data = f.read()
          return data[-limit:] # only last chunk to avoid overload      
    except:
        return ""

def append_memory(entry):
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open(MEMORY_FILE, "a") as f:
        f.write(f"\n[{timestamp}] {entry}\n")

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def run_terminal(cmd):
    return subprocess.getoutput(cmd)[:4000]

def call_model(prompt):
    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
    )
    return response["message"]["content"]

print("AI DevOps Agent Ready")


def main():
    while True:
        user = input(">> ")
        if user.lower() in ["exit", "quit"]:
            break

        # Ensures the folder exists
        ensure_memory()
        # Load memory in
        memory_context = read_memory()

        memory_promt = f""""
        Previous memory:
        {memory_context}
        
        User request:
        {user}
        """
        reply = call_model(memory_promt)
        append_memory(f"USER: {user}")
        append_memory(f"AGENT: {reply}")

        reply = call_model(user)

        if reply.startswith("TOOL:"):
            lines = reply.split("\n")
            tool = lines[0].replace("TOOL:", "").strip()
            arg = lines[1].replace("INPUT:", "").strip()

            if tool == "read_file":
                result = read_file(arg)
            elif tool == "terminal":
                result = run_terminal(arg)
            else:
                result = "Unknown tool"

            print(f"\n[Tool Result]\n{result}\n")

            final = call_model(f"Tool result:\n{result}\nExplain this to the user.")
            print(final)

        else:
            print(reply)

if __name__== "__main__":
    main()