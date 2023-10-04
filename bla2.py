import datetime
import pytz
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

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

try:
    # Get the tasks in the specified tasklist
    tasks = service.tasks().list(tasklist=task_list_id).execute()

    # Get the current time
    current_time = datetime.datetime.now()

    # Iterate through the tasks
    for task in tasks.get('items', []):
        # Check if the task was completed
        if 'completed' in task:
            completed_time = datetime.datetime.fromisoformat(task['completed'][:-1])

            # Calculate the time difference
            time_difference = current_time - completed_time

            # Check if the task was completed within 5 seconds
            if time_difference.total_seconds() <= 5:
                print('haha')
              
except Exception as e:
    print("Error:", e)

