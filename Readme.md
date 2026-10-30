How to setup the virtual env for python
Steps

```
   1. py -3 -m venv <name-of-venv>
   2. Go to VSCODE command pallete Ctrl + Shift + p
   3. Search for Python: Select Interpreter
   4. type in the command pallette  .\<name-of-venv>\Scripts\python.exe
   5. pip install fastapi[all] to install all the fast-api dependency
   6. pip freeze to check the installed packages
```

Steps to run the Pyhton project

```
   uvicorn main:app
```

or Watcher the python project using the

```
   uvicorn main:app --reload
```

Schema Validation

```
   Pydantic is the library used in python FastAPI to validate the Payload schema, like a ZOD in nodejs
```
