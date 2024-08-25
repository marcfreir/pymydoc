from utils.parser import parse_code
from utils.doc_generator import generate_doc

if __name__ == '__main__':
    # Parse the sample script
    functions, classes = parse_code('my_script_example.py')
    
    # Generate documentation based on parsed functions and classes
    generate_doc(functions, classes)

    print("Documentation generated successfully!")
