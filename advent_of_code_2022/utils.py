from pathlib import Path

def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt