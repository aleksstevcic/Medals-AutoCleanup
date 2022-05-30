@echo off

set pathtoclips=""
set pathtoscripts=""
set pathtoJSON=""

set /A timetodelete=7

ForFiles /p %pathtoclips% /s /d -%timetodelete% /m *.mp4 /c "cmd /c del @path"
ForFiles /p %pathtoclips% /s /d -%timetodelete% /m *.mkv /c "cmd /c del @path"
ForFiles /p %pathtoclips% /s /d -%timetodelete% /m *.jpg /c "cmd /c del @path"

python %pathtoscripts%\cleanJSON.py %pathtoJSON%
