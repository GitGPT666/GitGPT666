def save_code(code, filename="optimized.py"):
    with open(filename, "w") as f:
        f.write(code)
    return filename
