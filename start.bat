@echo off
REM Start backend
start cmd /k "cd apps\backend && uvicorn main:app --reload"
REM Start frontend
start cmd /k "cd apps\frontend && npm start"
