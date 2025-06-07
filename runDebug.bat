@echo off
echo Starting FastAPI application...
venv313\Scripts\activate
uvicorn app.main:app --reload
pause
