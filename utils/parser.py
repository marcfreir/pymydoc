import ast

class CodeParser(ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node):
        func_info = {
            'name': node.name,
            'docstring': ast.get_docstring(node),
            'args': [arg.arg for arg in node.args.args]
        }
        self.functions.append(func_info)
        self.generic_visit(node)

def parse_code(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
        parser = CodeParser()
        parser.visit(tree)
        return parser.functions
