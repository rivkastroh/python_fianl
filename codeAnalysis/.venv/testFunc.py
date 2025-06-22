import ast
from parameters import file_len
from helpTestFunc import *

def functionLength(content):
    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            is_valid = unitFunctionLength(node)
            if not is_valid:
                return False
    return True

def fileLength(content):
    tree = ast.parse(content)
    return len(tree.body) <= file_len

def unusedVariables(content):
    params = set()
    use_params = set()
    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            print(f"in var not used {node.targets}")
            for target in node.targets:
                if isinstance(target, ast.Name):
                    params.add(target.id)
        if isinstance(node,ast.Name):
            if isinstance(node.ctx, ast.Load):
                use_params.add(node.id)
    print(f"params: {params}")
    print(f"use_params: {use_params}")
    unused = params - use_params
    print(f"unused: {unused}")
    return unused

def missingDocstrings(content):
    c =0
    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            has_docstring = unitMissingDocstrings(node)
            if not has_docstring:
                c+=1
    return c
