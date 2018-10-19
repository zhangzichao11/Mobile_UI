@echo off
title stopAppiumServer
tasklist /V|find "startAppiumServer">nul
if %errorlevel%==0 (
::¹Ø±Õappium·þÎñ
taskkill /F /IM node.exe
taskkill /F /FI "WINDOWTITLE eq startAppiumServer"
taskkill /F /IM cmd.exe
)