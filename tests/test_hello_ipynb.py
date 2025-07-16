import glob
import json

def test_hello_ipynb():
    ipynb_files = glob.glob("*_hello.ipynb")
    assert ipynb_files, "No *_hello.ipynb file found"

    with open(ipynb_files[0], "r", encoding="utf-8") as f:
        notebook = json.load(f)
        found = any(
            'print("Hello, World")' in str(cell.get("source", ""))
            or 'print(\'Hello, World\')' in str(cell.get("source", ""))
            for cell in notebook.get("cells", [])
        )
        assert found, "print('Hello, World') not found in the .ipynb file"
