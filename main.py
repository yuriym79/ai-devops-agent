import ollama
import subprocess

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
            {"role": "user", "content": prompt},
        ],
    )
    return response["message"]["content"]

print("AI DevOps Agent Ready")

while True:
    user = input(">> ")
    if user.lower() in ["exit", "quit"]:
        break

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

