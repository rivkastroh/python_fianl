from testFunc import *
from testFuncGraf import *
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
async def get():
    return "application code analysis!"

@app.post("/analyze")
async def analyze(files: list[UploadFile] = File(...)):
    ret = {}
    content_files = {}
    for f in files:
        content = await f.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        content_files[f.filename] = content
    combined_graph_path = create_combined_graph(content_files)
    return {"combined_graph": combined_graph_path}

@app.post("/alerts")
async def alerts(files: list[UploadFile] = File(...)):
    ret = {}
    for file in files:
        content = await file.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        print(f"conetent one: {content}")
        issues = {}
        func_length = functionLength(content)
        file_len = fileLength(content)
        unused_variables = unusedVariables(content)
        missing_docstrings = missingDocstrings(content)
        # הוספת בעיות לתשובה
        issues['function_length'] = func_length
        issues['file_length'] = file_len
        issues['unused_variables'] = unused_variables
        issues['missing_docstrings'] = missing_docstrings
        ret[file.filename] = issues
    return ret
