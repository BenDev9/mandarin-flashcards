@echo off
.venv\Scripts\python.exe -m black ./src/
.venv\Scripts\python.exe -m ruff check . --fix