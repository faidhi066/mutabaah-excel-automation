import datetime
import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pytz

def Create_Service(client_secret_file, api_name, api_version, *scopes):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    # Specify the directory where you want to check for the token file  # Specify a custom path for the pickle file
    custom_pickle_path = '/Users/faidhi/Documents'

    # Create the full path to the pickle file
    pickle_file = os.path.join(custom_pickle_path, f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle')

    if os.path.exists(custom_pickle_path):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        return service
    except Exception as e:
        os.remove(pickle_file)
        return None

# Create the Google Tasks service
CLIENT_SECRET_FILE = '/Users/faidhi/Documents/client_secret.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# Assuming you have created the Google Tasks service and retrieved a task's ID
task_id = 'aUo5MXdnZTNBYXdHbm9DRQ'  # Replace with the actual task ID you want to retrieve

# Call the tasks().get() method to get information about the specified task
task = service.tasks().get(tasklist='@default', task=task_id).execute()

title = task['title']
notes = task.get('notes', '')  # Optional notes field
due_date = task.get('due', '')  # Optional due date
completed = task.get('completed', '')

completed_datetime = datetime.datetime.fromisoformat(completed[:-1])
due_date_datetime = datetime.datetime.fromisoformat(due_date[:-1])

# Define the Malaysia time zone
myt_timezone = pytz.timezone('Asia/Kuala_Lumpur')

# Convert the timestamps to Malaysia time zone
completed_datetime_myt = completed_datetime.replace(tzinfo=pytz.UTC).astimezone(myt_timezone)
due_date_datetime_myt = due_date_datetime.replace(tzinfo=pytz.UTC).astimezone(myt_timezone)

# Format the timestamps as strings in the desired format
formatted_completed_time = completed_datetime_myt.strftime('%A, %B %d, %Y, %H:%M')
completed_datetime_myt = due_date_datetime_myt.strftime('%A, %B %d, %Y, %H:%M')

# Print the formatted time
print(formatted_completed_time)
