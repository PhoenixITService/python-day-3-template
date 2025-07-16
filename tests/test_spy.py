import glob
import subprocess
import pytest

# Define test cases: (input string, expected output)
test_cases = [
    ("120 101 122 101 100 103 72 111 79 78 99", "code"),
    ("111 97 101 122 101 81 87 116", "tea"),
    ("41 73", "I"),
    ("65 66 67", "B"),  
    ("97 98 99 100 101 102", "eb"),
]

# Generate short and safe test IDs
test_ids = [f"case{i+1}" for i in range(len(test_cases))]

@pytest.mark.parametrize("input_data, expected_output", test_cases, ids=test_ids)
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
    assert output == expected_output, f"For input `{input_data}`, expected `{expected_output}`, but got `{output}`"
