def generate_doc(functions, classes, output_path='documentation.md'):
    with open(output_path, 'w') as doc_file:
        # Document functions
        for func in functions:
            doc_file.write(f"# Implement function `{func['name']}`\n")
            doc_file.write(f"### Parameters: {', '.join(func['args'])}\n")
            doc_file.write(f"### Description: {func['docstring'] or 'No description provided.'}\n")
            doc_file.write("\n---\n")
        
        # Document classes
        for cls in classes:
            doc_file.write(f"# Implement class `{cls['name']}`\n")
            doc_file.write(f"### Description: {cls['docstring'] or 'No description provided.'}\n")
            for method in cls['methods']:
                doc_file.write(f"## Implement method `{method['name']}` of class `{cls['name']}`\n")
                doc_file.write(f"### Parameters: {', '.join(method['args'])}\n")
                doc_file.write(f"### Description: {method['docstring'] or 'No description provided.'}\n")
                doc_file.write("\n---\n")
