import ast
from parameters import func_len

def unitFunctionLength(func):
    if isinstance(func, ast.FunctionDef):
        return len(func.body) <= func_len
    return False

def unitMissingDocstrings(func):
    if isinstance(func,ast.FunctionDef):
        return ast.get_docstring(func) is not None
    return False