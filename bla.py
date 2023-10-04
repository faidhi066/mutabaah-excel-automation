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

task_list_id = 'MDEwMDY1ODE5NjU0NzIzNTg1ODU6MDow'

def create_sheets_service(credentials_file):
    creds = None
    # The file token_sheets.pickle stores the user's access and refresh tokens
    token_sheets = '/Users/faidhi/Documents/token_sheets.pickle'

    if os.path.exists(token_sheets):
        with open(token_sheets, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_sheets, 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Sheets API service
    service = build('sheets', 'v4', credentials=creds)

    return service


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Replace 'client_secret_sheets.json' with your Sheets credentials file
sheets_service = create_sheets_service('/Users/faidhi/Documents/client_secret.json')


    
myt_timezone = pytz.timezone('Asia/Kuala_Lumpur')
current_time = datetime.datetime.now()

# Iterate through the tasks
tasks = service.tasks().list(tasklist=task_list_id, showCompleted=True, showHidden=True).execute()

# Iterate through the tasks
for task in tasks.get('items', []):
    print( task['title'])
    # Check if the task was completed
    if 'completed' in task:
        completed_datetime = datetime.datetime.fromisoformat(task['completed'][:-1])
        due_datetime = datetime.datetime.fromisoformat(task['due'][:-1])
        # Add 7 hours to 'completed_datetime'
        completed_datetime = completed_datetime + datetime.timedelta(hours=8)
        time_difference = current_time - completed_datetime

        # Format the time difference as "HH:MM:SS"
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time_difference = f"{hours:02d}:{minutes:02d}"

        # Print the formatted time difference
        print("Completed time:", completed_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        print("Due time: " ,due_datetime)
        print("Current time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Time Difference:", formatted_time_difference)
        completed_datetime = completed_datetime.strftime('%A, %B %d, %Y, %H:%M')
        due_datetime = due_datetime.strftime('%A, %B %d, %Y, %H:%M')

        if time_difference.total_seconds() < 30:
            # Execute your desired action here
            print("Time difference is less than 30 seconds. Appending tables.", "\n")

            # Define the spreadsheet ID, sheet name, and column name
            spreadsheet_id = '1eDlIhyI8XfUM-qLiix80-06oAzFq3vKKW-yS8EDnwEg'
            sheet_name = f"{task['title']}"
            column_name = 'A'  # Replace with the column you want to update

            # Retrieve the values from the specified column
            result = sheets_service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=f'{sheet_name}!{column_name}:{column_name}'
            ).execute()

            # Extract the values from the response
            values = result.get('values', [])

            if values:
                # Find the index of the last non-empty cell in the column
                last_non_empty_index = max(i for i, val in enumerate(values) if val)
                print(last_non_empty_index)
                
                    # Define the values you want to append in a list
                values_to_append = [[completed_datetime, due_datetime]]

                # Create the request body
                request_body = {
                    'values': values_to_append
                }
                if values_to_append:
                    # Define the range for the empty rows to update
                    range_to_update = f'{sheet_name}!{column_name}{last_non_empty_index + 2}'
                    
                    try:
                        # Call the update method to update the empty rows
                        response = sheets_service.spreadsheets().values().update(
                            spreadsheetId=spreadsheet_id,
                            range=range_to_update,
                            valueInputOption='RAW',  # You can change this to 'USER_ENTERED' for formatting
                            body=request_body
                        ).execute()
                        print(f'{len(request_body)} rows added.')
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        if hasattr(e, 'content'):
                            print(f"Error details: {e.content}")
                else:
                    print('No empty rows to update.')
            else:
                print('No data in the column.')

        else:
            print("Time difference is greater 30 seconds.",  "\n")