def write_file(file_name, file_content):
    
    """
    Write content to a file.
    Args:
        file_name (str): The name of the file.
        file_content (str): The content to write to the file.
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    """
    Append content to a file.
    Args:
        file_name (str): The name of the file.
        append_content (str): The content to append to the file.
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write("\n" + append_content)

def read_file(file_name):
    """
    Read and return the content of a file.
    Args:
        file_name (str): The name of the file.
    Returns:
        str: The content of the file.
    """
    with open(f"{file_name}.txt", "r") as file:
        content = file.read()
    return content
