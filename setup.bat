@echo off
echo Setting up LeetCode Rank Tracker...

:: Install Python dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

:: Prompt user to enter the LeetCode username
set /p leetcode_username="Enter your LeetCode username: "

:: Update fetch_rank.py script with the provided username
echo Updating fetch_rank.py with LeetCode username...
python src/update_website_url.py %leetcode_username%

:: Run automated task scheduler script to register task
echo Setting up Task Scheduler...
python src/automated_task_sched.py

echo Setup complete!
pause
