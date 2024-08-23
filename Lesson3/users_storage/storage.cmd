@echo off

setlocal EnableDelayedExpansion

set storageFile=.\storage\users.dat
set fieldsSeparator=  {}

if "%1%" == "create" (

	set id=1
	FOR /F "tokens=1 delims=" %%G IN (!storageFile!) DO set /A id+=1

	echo !id!
	set b=%2%

    set line=!id!!fieldsSeparator!!b!
    echo !line!>> !storageFile!

	exit /B 0
)

if "%1%" == "get" (

	set id=%2%!fieldsSeparator!

	FOR /F "tokens=* USEBACKQ" %%F IN (`findstr /B /R "!id!" !storageFile!`) DO (

		SET _test=%%F
		SET _result=!_test:*{}=!
        ECHO !_result!

		exit /B 0
	)


	exit /B 0
)