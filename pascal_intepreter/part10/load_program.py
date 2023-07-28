import os


def load_program(file_name: str) -> str:
    """Load a program from a file."""
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path) as f:
        return f.read()
