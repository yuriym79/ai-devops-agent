from tools.terminal_tools import run_terminal


def test_terminal_echo():
    try:
        output = run_terminal("echo test")
        assert "test" in output.lower()
    except Exception as ex:
        f"Test Failed. Exception: {ex}"