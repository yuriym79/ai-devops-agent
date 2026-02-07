import os

from tools.memory import ensure_memory, append_memory, read_memory, MEMORY_FILE


def test_memory_creation():
    try:
        ensure_memory()
        assert os.path.exists(MEMORY_FILE)
    except Exception as ex:
        f"Test Failded. Exception: {ex}"

def test_append_and_read_memory():
    try:
        append_memory("TEST ENTRY")
        data = read_memory()
        assert "TEST ENTRY" in data
    except Exception as ex:
        f"Test Failed. Exception: {ex}"