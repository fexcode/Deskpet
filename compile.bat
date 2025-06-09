@echo off

.\v\Scripts\pyinstaller.exe --windowed --add-data="logo.png;." --distpath . --name=Pet main.py

copy .\logo.png .\dist\Pet\

rename .\Pet\ dist