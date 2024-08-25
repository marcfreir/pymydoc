from utils.parser import parse_code
from utils.doc_generator import generate_doc

def generate_documentation(file_path, output_path='documentation.md'):
    """
    Generates documentation for the given Python file.

    Args:
        file_path (str): The path to the Python file to document.
        output_path (str): The path to save the generated documentation (default: documentation.md).
    """
    functions, classes = parse_code(file_path)
    generate_doc(functions, classes, output_path)
    print(f"Documentation generated and saved to {output_path}")

# Command for the user to call directly
def pymydoc(file_path, output_path='documentation.md'):
    """
    The main entry point for generating documentation.

    Args:
        file_path (str): The path to the Python file to document.
        output_path (str): The path to save the generated documentation (default: documentation.md).
    """
    generate_documentation(file_path, output_path)
