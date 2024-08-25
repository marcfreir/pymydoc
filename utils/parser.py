import ast

class CodeParser(ast.NodeVisitor):
    def __init__(self):
        self.classes = []
        self.functions = []

    def visit_ClassDef(self, node):
        class_info = {
            'name': node.name,
            'docstring': ast.get_docstring(node),
            'methods': []
        }
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_info = {
                    'name': item.name,
                    'docstring': ast.get_docstring(item),
                    'args': [arg.arg for arg in item.args.args]
                }
                class_info['methods'].append(method_info)
        self.classes.append(class_info)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if isinstance(node.parent, ast.Module):
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
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node
        parser = CodeParser()
        parser.visit(tree)
        return parser.functions, parser.classes
