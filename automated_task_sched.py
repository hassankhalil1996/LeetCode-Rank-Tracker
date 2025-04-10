import datetime
import win32com.client
import subprocess

scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()
root_folder = scheduler.GetFolder('\\')
task_def = scheduler.NewTask(0)

# Get Python path dynamically using 'where python'
python_path = subprocess.check_output('where python', shell=True).decode().splitlines()[0]

# Defining the Start time of job
start_time = datetime.datetime.now() + datetime.timedelta(minutes=4)

# For Daily Trigger set this variable to 2 ; for One time run set this value as 1
TASK_TRIGGER_DAILY = 2
trigger = task_def.Triggers.Create(TASK_TRIGGER_DAILY)

#Repeat for a duration of number of day
# num_of_days = 10
# trigger.Repetition.Duration = "P"+str(num_of_days)+"D"

#use PT2M for every 2 minutes, use PT1H for every 1 hour
# trigger.Repetition.Interval = "PT1H"
trigger.StartBoundary = start_time.isoformat()

# Create action
TASK_ACTION_EXEC = 0
action = task_def.Actions.Create(TASK_ACTION_EXEC)
action.ID = 'Run Python Script - hassan'
action.Path = python_path
action.Arguments ='fetch_rank.py'
action.WorkingDirectory = r'C:\Users\hassa\Desktop\job_searching\leetcode_ranks'

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
    'LeetCode Rank Scrap',  # Task name
    task_def,
    TASK_CREATE_OR_UPDATE,
    '',  # No user
    '',  # No password
    TASK_LOGON_NONE
)