def delete_protected(file_name):
    raise PermissionError(f"Deletion is not allowed: {file_name}")
