import ollama
import subprocess
import os
from datetime import datetime
from tools.memory import ensure_memory, read_memory, append_memory
from tools.file_tools import read_file
from tools.terminal import run_terminal

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

            append_memory(f"USER: {user}")
            append_memory(f"AGENT: {reply}")

if __name__== "__main__":
    main()