@echo off
title Sudoku Graph Solver - UPC Complejidad Algoritmica
cd /d "%~dp0"
echo ===================================================
echo   Iniciando Sudoku Graph Solver (UPC - Grupo 5)
echo ===================================================
echo.
python src/main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] No se pudo iniciar con 'python'. Intentando con 'py'...
    py src/main.py
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo Error critico al ejecutar la aplicacion. Verifica tu instalacion de Python.
        pause
    )
)
