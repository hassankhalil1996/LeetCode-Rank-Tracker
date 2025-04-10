@echo off
echo Setting up LeetCode Rank Tracker...

:: Install Python dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

:: Prompt user to enter the ChromeDriver path if it's not set
set /p chromedriver_path="Enter the full path to chromedriver.exe (e.g. C:\path\to\chromedriver.exe): "

:: Update the fetch_rank.py script with the provided path
echo Updating fetch_rank.py with chromedriver path...
powershell -Command "(Get-Content fetch_rank.py) -replace 'path = r\"C:\\chromedriver-win64\\chromedriver.exe\"', 'path = r\"%chromedriver_path%\"' | Set-Content fetch_rank.py"

:: Run automated task scheduler script to register task
echo Setting up Task Scheduler...
python automated_task_sched.py

echo Setup complete!
pause
