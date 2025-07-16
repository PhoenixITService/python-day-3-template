import pytest
import glob
import subprocess

# ✅ Single test case
test_cases = [
    ("120 101 122 101 100 103 72 111 79 78 99", "code"),
]

@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_spy_message(input_data, expected_output):
    spy_files = glob.glob("*_spy.py")
    assert spy_files, "No *_spy.py file found"

    result = subprocess.run(
        ["python", spy_files[0]],
        input=input_data,
        text=True,
        capture_output=True,
        timeout=5
    )

    output = result.stdout.strip()
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"
