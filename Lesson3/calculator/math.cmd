@echo off

setlocal EnableDelayedExpansion

set logFile=./logs/math.log

echo %1% operation>> !logFile!

set a2=%2%

set b2=%3%

echo first param: !a2!>> !logFile!
echo second param: !b2!>> !logFile!

if "%1%" == "add" (

	set /a "c2=!a2!+!b2!"

	echo !c2!
	exit /B 0
)

if "%1%" == "sub" (

	set /a "c2=!a2!-!b2!"

	echo !c2!
	exit /B 0
)

if "%1%" == "mul" (

	set /a "c2=!a2!*!b2!"

	echo !c2!
	exit /B 0
)