import datetime
import win32com.client
import subprocess
import os

scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()
root_folder = scheduler.GetFolder('\\')
task_def = scheduler.NewTask(0)

# Get Python path dynamically using 'where pythonw'
python_path = subprocess.check_output('where pythonw', shell=True).decode().splitlines()[0]


# Defining the Start time of job
start_time = datetime.datetime.now() + datetime.timedelta(minutes=4)

# For Daily Trigger set this variable to 2 ; for One time run set this value as 1
TASK_TRIGGER_DAILY = 2
trigger = task_def.Triggers.Create(TASK_TRIGGER_DAILY)



trigger.StartBoundary = start_time.isoformat()

# Create action
TASK_ACTION_EXEC = 0
action = task_def.Actions.Create(TASK_ACTION_EXEC)
action.ID = 'Run Python Script'

# Automate the working directory extraction based on the script location
current_directory = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(current_directory, 'fetch_rank.py')

print("script_path" , script_path)

action.Path = python_path
action.Arguments = f'"{script_path}"'  # Full path to fetch_rank.py

# Automate working directory extraction based on the script location
current_directory = os.path.dirname(os.path.realpath(__file__))
action.WorkingDirectory = current_directory

# Set parameters
task_def.RegistrationInfo.Description = 'Fetches and logs LeetCode rank using Python script'
task_def.Settings.Enabled = True
task_def.Settings.StopIfGoingOnBatteries = False
task_def.Settings.StartWhenAvailable = True # runs as soon as possible after the computer is back on


# Register task
# If task already exists, it will be updated
TASK_CREATE_OR_UPDATE = 6
TASK_LOGON_NONE = 0
root_folder.RegisterTaskDefinition(
    'LeetCode Rank Scrap-auto',  # Task name
    task_def,
    TASK_CREATE_OR_UPDATE,
    '',  # No user
    '',  # No password
    TASK_LOGON_NONE
)