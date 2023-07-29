@echo off
cd /d "%~dp0batch"
if "%1" == "del" (
    del.bat %2
    goto end
)
if "%1" == "help" (
    help.bat
    goto end
)
if "%1" == "make" (
    make.bat %2
    goto end
)
