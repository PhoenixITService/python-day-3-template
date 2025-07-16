import glob

def test_hello_py():
    py_files = glob.glob("*_hello.py")
    assert py_files, "No *_hello.py file found"

    with open(py_files[0], "r") as f:
        content = f.read()
        assert 'print("Hello, World")' in content or "print('Hello, World')" in content, "print('Hello, World') not found in the .py file"
