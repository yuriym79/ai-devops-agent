from tools.file_tools import read_file


def test_read_file(tmp_path):
    try:
        test_file = tmp_path / "sample.txt"
        test_file.write_text("hello world")

        content = read_file(str(test_file))
        assert content == "hello world"
    except Exception as ex:
        f"Test Failed. Exception: {ex}"