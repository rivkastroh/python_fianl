import ast
from ctypes import c_int
from importlib.metadata import files
import uuid
import matplotlib.pyplot as plt
from parameters import file_len
from helpTestFunc import *
from testFunc import *
import numpy as np
import os



def pieChart(axs, files_py):
    c_len_func = 1
    c_len_file = 1
    c_unused_variables = 1
    c_missing_docstrings = 1
    for filename, content in files_py.items():
        func_length = functionLength(content)
        file_len = fileLength(content)
        unused_variables = unusedVariables(content)
        missing_docstrings = missingDocstrings(content)
        if not func_length:
            c_len_func += 1
        if not file_len:
            c_len_file += 1
        c_unused_variables += len(unused_variables)
        c_missing_docstrings += missing_docstrings

    problems = {"func length": c_len_func, "file len": c_len_file,
                "unused variables": c_unused_variables, "missing docstrings": c_missing_docstrings}
    # # המרת המילון לרשימה של ערכים
    problems_values = list(problems.values())
    labels = list(problems.keys())  # תוויות מהמפתחות של המילון
    problems_values = [0 if np.isnan(value) else value for value in problems_values]
    axs.pie(problems_values, labels=labels, autopct='%1.1f%%', startangle=140)
    axs.set_title("Function Lengths")


def grafFunctionLength(axs, files_py):
    lens = {}
    for filename, content in files_py.items():
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                length = len(node.body)
                lens[node.name] = length
    if lens:
        lengths = list(lens.values())
        axs.hist(lengths, bins=7, color="skyblue", edgecolor="black", density=True)
        axs.set_title("Function Lengths")
        axs.set_xlabel("Lines")
        axs.set_ylabel("Functions")
    else:
        axs.text(0.5, 0.5, "No functions found to plot.", horizontalalignment='center', verticalalignment='center')

def barChart(axs,files_py):
    issues_dict = {}
    for filename, content in files_py.items():
        c = 0
        c += functionLength(content)
        c += fileLength(content)
        c += len(unusedVariables(content))
        c += missingDocstrings(content)
        issues_dict[filename] = c
    file_names = list(issues_dict.keys())
    values = list(issues_dict.values())
    axs.bar(file_names, values, color="skyblue", edgecolor="black")
    axs.set_title("Number of issues per file")
    axs.set_xlabel("File Names")
    axs.set_ylabel("Problems")
    axs.tick_params(axis='x', rotation=45)


def create_combined_graph(files_py):
    # יצירת דמות חדשה עם תתי-גרפים
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # 3 תתי-גרפים בעמודה אחת
    pieChart(axs[0], files_py)  # קריאה לגרף עוגה
    grafFunctionLength(axs[1], files_py)  # קריאה להיסטוגרמה
    barChart(axs[2], files_py)  # קריאה לגרף עמודות

    plt.tight_layout()
    file_id = str(uuid.uuid4())
    combined_graph_path = f"combined_graph_{file_id}.png"
    plt.savefig(combined_graph_path)
    plt.close(fig)
    # קבלת הנתיב המלא של התמונה
    full_path = os.path.abspath(combined_graph_path)

    return full_path
