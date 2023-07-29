@echo off
cd /d "%~dp0batch"
if "%1" == "install" (
    install.bat
    goto end
)
if "%1" == "make" (
    make.bat %2
    goto end
)
if "%1" == "update" (
    update.bat %2
    goto end
)
if "%1" == "help" (
    help.bat
    goto end
)
if "%1" == "clear" (
    clear.bat
    goto end
)
if "%1" == "del" (
    del.bat %2
    goto end
)
cd ..
type NUL >> "open/%1.py"
cd "compiler" >> NUL
copy "compiler.py" "../open/%1.py" >> NUL
cd .. >> NUL
type "%2" >> "open/%1.py"
echo. >> "open/%1.py"
echo. >> "open/%1.py"
echo # Code [.cns] CoNsol Script >> "open/%1.py"
type "%1" >> "open/%1.py"
python "open/%1.py"
:end