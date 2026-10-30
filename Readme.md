How to setup the virtual env for python
Steps

```
   1. py -3 -m venv <name-of-venv>
   2. Go to VSCODE command pallete Ctrl + p
   3. type in the command pallette  .\<name-of-venv>\Scripts\python.exe
   4. pip install fastapi[all] to install all the fast-api dependency
   5. pip freeze to check the installed packages
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
