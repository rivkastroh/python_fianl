# 🧠 CodeGuard – Code Analysis System

## Overview

CodeGuard is a backend system designed to automatically analyze Python code quality every time a user runs `wit push` (as part of a simplified version control flow).  
The system detects common code quality issues and returns visual insights as graphs, simulating a basic Continuous Integration (CI) process focused on Python code best practices.

---

## 📦 Technologies Used

- **Language:** Python 3.x
- **Web Framework:** FastAPI
- **Code Analysis:** Python’s `ast` (Abstract Syntax Tree) module
- **Visualization:** matplotlib (for graph generation)
- **Version Control Simulation:** Custom `wit` tool (with commands: init, add, commit, log, push)

---

## 🗂️ Folder Structure

```
project-root/
│
├── wit/                 # Source code for the custom wit version control tool
│   ├── __init__.py
│   └── ... 
│
├── server/              # FastAPI backend code
│   ├── main.py          # FastAPI app entrypoint
│   ├── analysis.py      # AST analysis functions
│   ├── graphing.py      # Graph generation utilities (matplotlib)
│   └── ... 
│
├── tests/               # (Optional) Unit tests
│
├── requirements.txt     # Python dependencies
├── README.md            # This documentation
└── ...
```

---

## 🚀 Installation & Running Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/HadassaAvimorNew/python_fianl.git
cd python_fianl
```

### 2. Create & Activate a Virtual Environment (Recommended)
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server
```bash
cd server
uvicorn main:app --reload
```
The API will be available at: [http://localhost:8000](http://localhost:8000)

### 5. Using the wit Tool
- Use the wit commands (`init`, `add`, `commit`, `log`, `push`) as described in the wit documentation.
- When running `wit push`, your Python files are sent to the FastAPI server for analysis.

---

## 🌐 API Endpoints

### `/analyze`  –  `POST`
- **Purpose:** Accepts Python files, analyzes them, and returns generated graphs as PNG images (or links).
- **Request:** Multipart/form-data with one or more Python files.
- **Response:** Images for:
  - Histogram: Distribution of function lengths
  - Pie Chart: Number of issues per issue type
  - Bar Chart: Number of issues per file
  - (Bonus) Line Graph: Issues over time

### `/alerts`  –  `POST`
- **Purpose:** Accepts Python files, analyzes them, and returns a JSON with code quality warnings.
- **Request:** Multipart/form-data with one or more Python files.
- **Response:** JSON object listing:
  - Functions longer than 20 lines
  - Files longer than 200 lines
  - Unused variables
  - Functions missing docstrings
  - (Bonus) Warnings for variables named in non-English (e.g., Hebrew)

---

## 🔍 Code Quality Checks (via AST)

For each Python file pushed, the system checks:
- **Function Length:** Warn if a function is longer than 20 lines.
- **File Length:** Warn if the file is longer than 200 lines.
- **Unused Variables:** Warn if a variable is assigned but never used.
- **Missing Docstrings:** Warn if a function lacks a docstring.
- **[Bonus] Non-English Variable Names:** Warn if variable names include non-English (e.g., Hebrew) letters.

---

## 📊 Visual Output

The system generates the following after analysis:
1. **Histogram:** Distribution of function lengths.
2. **Pie Chart:** Issue counts per issue type.
3. **Bar Chart:** Number of issues per file.
4. **Bonus:** Line graph showing issues over time.

All graphs are returned as PNG images (or links to images).

---

## 📝 Example Usage

### Analyze Files via API (with `curl`)
```bash
curl -F "file=@your_code.py" http://localhost:8000/analyze
curl -F "file=@your_code.py" http://localhost:8000/alerts
```

### With the wit workflow:
```bash
wit init
wit add your_code.py
wit commit -m "Initial commit"
wit push
# On push, code is analyzed & results are returned
```

---

## ✨ Bonus Feature

The server detects and warns about variable names containing non-English letters (e.g., Hebrew, Arabic, etc.), helping maintain code readability and consistency.

---

## 📚 Further Reading & References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [matplotlib Documentation](https://matplotlib.org/)
- [Python ast Module](https://docs.python.org/3/library/ast.html)
- [Uvicorn ASGI Server](https://www.uvicorn.org/)

---

---

# מערכת ניתוח קוד – תיעוד בעברית

## סקירה כללית

CodeGuard היא מערכת צד-שרת המיועדת לניתוח איכות קוד אוטומטי עבור קבצי פייתון, בכל הרצת `wit push` (בתוך מערכת בקרת גרסאות פשוטה).  
המערכת מזהה בעיות איכות קוד נפוצות ומחזירה תובנות בגרפים ויזואליים – סימולציה בסיסית של תהליך CI פנימי.

---

## טכנולוגיות עיקריות

- **Python 3.x** – שפת תכנות עיקרית
- **FastAPI** – שרת רסט מודרני ומהיר
- **ast** – ניתוח קוד באמצעות עץ תחביר אבסטרקטי
- **matplotlib** – הפקת גרפים ויזואליים
- **wit** – כלי ניהול גרסאות פשוט (init, add, commit, log, push)

---

## מבנה תיקיות מוצע

```
project-root/
│
├── wit/                 # קוד מקור של wit
│
├── server/              # שרת FastAPI
│   ├── main.py          # נקודת כניסה
│   ├── analysis.py      # ניתוח AST
│   ├── graphing.py      # גרפים
│
├── tests/               # בדיקות (אם קיימות)
│
├── requirements.txt     # תלותים
├── README.md            # תיעוד זה
```

---

## התקנה והרצה

1. לשכפל את המאגר:
   ```bash
   git clone https://github.com/HadassaAvimorNew/python_fianl.git
   cd python_fianl
   ```

2. להקים סביבה וירטואלית:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. התקנת תלותים:
   ```bash
   pip install -r requirements.txt
   ```

4. הרצת שרת FastAPI:
   ```bash
   cd server
   uvicorn main:app --reload
   ```

5. שימוש ב-wit:
   - להפעיל פקודות wit (init, add, commit, log, push)
   - ב-push יישלחו קבצים לשרת לניתוח

---

## הסבר על ה-API

### `/analyze`  –  `POST`
- קבלת קבצי פייתון, ניתוחם והחזרת גרפים (PNG).

### `/alerts`  –  `POST`
- קבלת קבצי פייתון, ניתוחם והחזרת אזהרות איכות קוד (JSON).

---

## בדיקות איכות קוד

- פונקציה מעל 20 שורות – אזהרה
- קובץ מעל 200 שורות – אזהרה
- משתנה לא בשימוש – אזהרה
- פונקציה ללא docstring – אזהרה
- (בונוס) משתנה בשם לא באנגלית – אזהרה

---

## גרפים ויזואליים

- היסטוגרמה – אורך פונקציות
- פאי – סוגי בעיות
- עמודות – כמות בעיות לכל קובץ
- בונוס: גרף קווי – בעיות לאורך זמן

---

## דוגמה לשימוש

```bash
curl -F "file=@your_code.py" http://localhost:8000/analyze
wit push
```

---

בהצלחה!
