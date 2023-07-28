import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES=["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID1= #for teacher leave  c
SPREADSHEET_ID2= #for admin leave   u
SPREADSHEET_ID3= #for teacher urgent message  u
SPREADSHEET_ID4= #for admin urgent message  u
SPREADSHEET_ID5= #for teacher update u

def store_data_leave(chat_id, type, message, list_teacher):
    def column(sheets, n):
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID1, range=f"Sheet1!A{n}:A").execute()
        return result


    def check_column_empty(credentials, list_teacher):
        try:
            service = build("sheets", "v4", credentials=credentials)

            sheets = service.spreadsheets()
            n = 1
            while True:
                result = column(sheets, n)
                values = result.get('values', [])
                if not values or not values[0]:
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID1, range=f"Sheet1!A{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[0]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID1, range=f"Sheet1!B{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID1, range=f"Sheet1!C{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}/{list_teacher[3]}/{list_teacher[4]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID1, range=f"Sheet1!D{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}/{list_teacher[3]}/{list_teacher[4]+list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID1, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[5]}"]]}).execute()
                    print("Teacher information updated successfully.")
                    break
                else:
                    n += 1
                    print("Column is not empty.")
        except HttpError as error:
            print(error)

    def main():
        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
                credentials = flow.run_local_server(port=0)
                with open("token.json", "w") as token:
                    token.write(credentials.to_json())

            # Call the check_column_empty function
        check_column_empty(credentials, list_teacher)
        list_teacher.clear()

    if type=="name":
        teacher_name=message
        list_teacher.append(teacher_name)
        print(teacher_name)
    elif type=="duration":
        teacher_duration=message
        list_teacher.append(int(teacher_duration))
        print(teacher_duration)
    elif type=="year":
        teacher_year=2023
        list_teacher.append(int(teacher_year))
        print(teacher_year)
    elif type=="month":
        teacher_month=message
        list_teacher.append(teacher_month)
        print(teacher_month)
    elif type=="date":
        teacher_date=message
        print(teacher_date)
        list_teacher.append(int(teacher_date))
    elif type=="reason":
        teacher_reason=message
        list_teacher.append(teacher_reason)
        print(teacher_reason)
        print(list_teacher)
        main()


def store_data_urgent_teacher(chat_id, type, message, list_teacher):
    def column(sheets, n):
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID3, range=f"Sheet1!A{n}:A").execute()
        return result


    def check_column_empty(credentials, list_teacher, chat_id):
        try:
            service = build("sheets", "v4", credentials=credentials)

            sheets = service.spreadsheets()
            n = 1
            while True:
                result = column(sheets, n)
                values = result.get('values', [])
                if not values or not values[0]:
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID3, range=f"Sheet1!A{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{chat_id}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID3, range=f"Sheet1!B{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[0]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID3, range=f"Sheet1!C{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID3, range=f"Sheet1!D{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}"]]}).execute()
                    print("Teacher information updated successfully.")
                    break
                else:
                    n += 1
                    print("Column is not empty.")
        except HttpError as error:
            print(error)

    def main():
        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
                credentials = flow.run_local_server(port=0)
                with open("token.json", "w") as token:
                    token.write(credentials.to_json())

            # Call the check_column_empty function
        check_column_empty(credentials, list_teacher, chat_id)
        list_teacher.clear()

    if type=="name":
        urgent_teacher_name=message
        list_teacher.append(urgent_teacher_name)
        print(urgent_teacher_name)
    elif type=="contact":
        urgent_teacher_contact=message
        list_teacher.append(urgent_teacher_contact)
        print(urgent_teacher_contact)
    elif type=="message":
        urgent_teacher_message=message
        list_teacher.append(urgent_teacher_message)
        print(urgent_teacher_message)

def store_data_update_teacher(chat_id, type, message, list_teacher):
    def column(sheets, n):
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!A{n}:A").execute()
        return result


    def check_column_empty(credentials, list_teacher):
        try:
            service = build("sheets", "v4", credentials=credentials)

            sheets = service.spreadsheets()
            n = 1
            while True:
                result = column(sheets, n)
                values = result.get('values', [])
                if not values or not values[0]:
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!A{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[0]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!B{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!C{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!D{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[3]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[4]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[5]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[6]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[7]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[8]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[9]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[10]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[11]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[12]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID5, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[13]}"]]}).execute()
                    print("Teacher information updated successfully.")
                    break
                else:
                    n += 1
                    print("Column is not empty.")
        except HttpError as error:
            print(error)

    def main():
        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
                credentials = flow.run_local_server(port=0)
                with open("token.json", "w") as token:
                    token.write(credentials.to_json())

            # Call the check_column_empty function
        check_column_empty(credentials, list_teacher)
        list_teacher.clear()
    if type=="name":
        update_teacher_name=message
        list_teacher.append(update_teacher_name)
        print(update_teacher_name)
    elif type=="class":
        update_teacher_class=message
        list_teacher.append(update_teacher_class)
        print(update_teacher_class)
    elif type=="section":
        update_teacher_section=message
        list_teacher.append(update_teacher_section)
        print(update_teacher_section)
    elif type=="date":
        update_teacher_date=message
        list_teacher.append(update_teacher_date)
        print(update_teacher_date)
    elif type=="subject":
        update_teacher_subject=message
        list_teacher.append(update_teacher_subject)
        print(update_teacher_subject)
    elif type=="period":
        update_teacher_period=message
        list_teacher.append(update_teacher_period)
        print(update_teacher_period)
    elif type=="topic":
        update_teacher_topic=message
        list_teacher.append(update_teacher_topic)
        print(update_teacher_topic)
    elif type=="sub_topic":
        update_teacher_sub_topic=message
        list_teacher.append(update_teacher_sub_topic)
        print(update_teacher_sub_topic)
    elif type=="activity_type":
        update_teacher_activity_type=message
        list_teacher.append(update_teacher_activity_type)
        print(update_teacher_activity_type)
    elif type=="activity_detail":
        update_teacher_activity_detail=message
        list_teacher.append(update_teacher_activity_detail)
        print(update_teacher_activity_detail)
    elif type=="challenge":
        update_teacher_challenge=message
        list_teacher.append(update_teacher_challenge)
        print(update_teacher_challenge)
    elif type=="comment":
        update_teacher_comment=message
        list_teacher.append(update_teacher_comment)
        print(update_teacher_comment)
    elif type=="follow":
        update_teacher_follow=message
        list_teacher.append(update_teacher_follow)
        print(update_teacher_follow)

def store_data_urgent_admin(chat_id, type, message):
    def column(sheets, n):
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID4, range=f"Sheet1!A{n}:A").execute()
        return result


    def check_column_empty(credentials, list_admin, chat_id):
        try:
            service = build("sheets", "v4", credentials=credentials)

            sheets = service.spreadsheets()
            n = 1
            while True:
                result = column(sheets, n)
                values = result.get('values', [])
                if not values or not values[0]:
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID4, range=f"Sheet1!A{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{chat_id}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID4, range=f"Sheet1!B{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[0]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID4, range=f"Sheet1!C{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID4, range=f"Sheet1!D{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}"]]}).execute()
                    print("Teacher information updated successfully.")
                    break
                else:
                    n += 1
        except HttpError as error:
            print(error)

    def main():
        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
                credentials = flow.run_local_server(port=0)
                with open("token.json", "w") as token:
                    token.write(credentials.to_json())

            # Call the check_column_empty function
        check_column_empty(credentials, list_admin, chat_id)
        list_admin.clear()
    if type=="name":
        urgent_admin_name=message
        list_admin.append(urgent_admin_name)
        print(urgent_admin_name)
    elif type=="contact":
        urgent_admin_contact=message
        list_admin.append(urgent_admin_contact)
        print(urgent_admin_contact)
    elif type=="message":
        urgent_admin_message=message
        list_admin.append(urgent_admin_message)
        print(urgent_admin_message)

def store_data_leave_admin(chat_id, type, message, list_admin):
    def column(sheets, n):
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID2, range=f"Sheet1!A{n}:A").execute()
        return result


    def check_column_empty(credentials, list_admin):
        try:
            service = build("sheets", "v4", credentials=credentials)

            sheets = service.spreadsheets()
            n = 1
            while True:
                result = column(sheets, n)
                values = result.get('values', [])
                if not values or not values[0]:
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID2, range=f"Sheet1!A{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[0]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID2, range=f"Sheet1!B{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID2, range=f"Sheet1!C{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}/{list_teacher[3]}/{list_teacher[4]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID2, range=f"Sheet1!D{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[2]}/{list_teacher[3]}/{list_teacher[4]+list_teacher[1]}"]]}).execute()
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID2, range=f"Sheet1!E{n}", valueInputOption='USER_ENTERED', body={"values":[[f"{list_teacher[5]}"]]}).execute()
                    print("Teacher information updated successfully.")
                    break
                else:
                    n += 1
        except HttpError as error:
            print(error)

    def main():
        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
                credentials = flow.run_local_server(port=0)
                with open("token.json", "w") as token:
                    token.write(credentials.to_json())

            # Call the check_column_empty function
        check_column_empty(credentials, list_admin)
        list_admin.clear()
    if type=="name":
        admin_name=message
        print(admin_name)
        list_admin.append(admin_name)
    elif type=="duration":
        admin_duration=message
        list_admin.append(admin_duration)
        print(admin_duration)
    elif type=="year":
        admin_year=2023
        list_admin.append(admin_year)
        print(admin_year)
    elif type=="month":
        admin_month=message
        list_admin.append(admin_month)
        print(admin_month)
    elif type=="date":
        admin_date=message
        list_admin.append(admin_date)
        print(admin_date)
    elif type=="reason":
        admin_reason=message
        list_admin.append(admin_reason)
        print(admin_reason)
        print(list_admin)
        main()
