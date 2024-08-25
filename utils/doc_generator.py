def generate_doc(functions, output_path='documentation.md'):
    with open(output_path, 'w') as doc_file:
        for func in functions:
            doc_file.write(f"# Implement function `{func['name']}`\n")
            doc_file.write(f"### Parameters: {', '.join(func['args'])}\n")
            doc_file.write(f"### Description: {func['docstring'] or 'No description provided.'}\n")
            doc_file.write("\n---\n")

if __name__ == '__main__':
    functions = parse_code('your_script.py')
    generate_doc(functions)
