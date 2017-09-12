from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret2.json'
# APPLICATION_NAME = 'Google Sheets API Python Quickstart'
APPLICATION_NAME = 'Strava Project2'


#https://www.googleapis.com/auth/spreadsheets   

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'strava_export.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/129x0UDGDWaJaKglB1V1CGhGVaQpfYzoi-9dislefxU4/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '129x0UDGDWaJaKglB1V1CGhGVaQpfYzoi-9dislefxU4'
    rangeName = 'Class Data!A2:E'

    values = [
        # First row in the range
        [
            # First data item (column) in the row.
            'Slinky',
            # Second data item (column) in the row.
            'Dog'
        ],
        # Second row in the range
        [
            'Creature',
            'Creature'
        ]
    ]
    body = {
        'values': values

    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId, range=rangeName, body=body,
        valueInputOption='USER_ENTERED').execute()
    #values = result.get('values', [])

    print(result)




if __name__ == '__main__':
    main()