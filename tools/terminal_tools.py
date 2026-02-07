import subprocess


def run_terminal(cmd):
    return subprocess.getoutput(cmd)[:4000]