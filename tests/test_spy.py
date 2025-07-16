import glob
import builtins

def test_spy_message(monkeypatch, capsys):
    # Look for a file like decode_spy.py or secret_spy.py
    py_files = glob.glob("*_spy.py")
    assert py_files, "No *_spy.py file found"

    # Input as per the problem
    sample_input = "120 101 122 101 100 103 72 111 79 78 99"
    expected_output = "code"

    # Mock input() to return the spy message
    monkeypatch.setattr(builtins, "input", lambda: sample_input)

    # Read and execute the code
    with open(py_files[0]) as f:
        code = f.read()
        exec(code, {})

    # Check printed output
    out, _ = capsys.readouterr()
    assert out.strip() == expected_output, f"Expected '{expected_output}' but got '{out.strip()}'"
