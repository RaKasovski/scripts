from django.db import models
from django.shortcuts import render
from pprint import pprint
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from scriptss.models import data_key_usd, data_value_usd, data_key_eur, data_value_eur
import django.db.backends.postgresql
import datetime
CREDENTIALS_FILE = 'C:/Users/Ильяс/OneDrive/Рабочий стол/DjangoProject/encomercproject/valutShow/creds.json'

spreadsheet_id = '1GCd4uUOanIGYHspKsT4Km4GJSQWm5oOL3Mgx_xRf7Cg'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "A2:B3",
             "majorDimension": "COLUMNS",
             "values": [[data_key_usd, data_key_eur], [data_value_usd, data_value_eur]]},
        ]
    }
).execute()
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E10',
    majorDimension='COLUMNS'
).execute()
pprint(values)
