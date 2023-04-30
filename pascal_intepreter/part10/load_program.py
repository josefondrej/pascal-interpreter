def load_program(file_name: str) -> str:
    """Load a program from a file."""
    with open(file_name) as f:
        return f.read()
