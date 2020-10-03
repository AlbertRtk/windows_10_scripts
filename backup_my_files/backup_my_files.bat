:: Albert Ratajczak, 2019
::
@ECHO OFF
ECHO --------------------
ECHO --- Doing backup ---
ECHO --------------------
::
:: backuping each dir from list of dirs in file folders.txt
for /F %%f in (folders.txt) do (
	ECHO.
	ECHO.
	ECHO Copying C:\Users\Albert\Albert\%%f
	robocopy C:\Users\Albert\Albert\%%f G:\%%f /MIR
)
::
PAUSE
