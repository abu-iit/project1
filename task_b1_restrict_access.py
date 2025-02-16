import os

def safe_path(file_name):
    base_path = os.path.abspath("./data")
    file_path = os.path.abspath(os.path.join(base_path, file_name))
    if not file_path.startswith(base_path):
        raise ValueError(f"Access denied: {file_path} is outside /data directory.")
    return file_path
