
md5 on win:
certutil -hashfile \\hostname\path\file.csv md5


rem Typical arg check in a bat file:

if [%1]==[] goto exit1
if not [%COMPUTERNAME%]==[MACHINE12345] goto exit1

echo doing stuff
d:
cd D:\folder
goto exit0

:exit1
echo errors
goto theend

:exit0
echo done
:theend
