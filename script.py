# Script is called at 9:16 each day to send emails, if the day is wednesday wait until 10:01
from datetime import datetime
import json
from send_sign_in import send_not_signed_in_students, send_reminder_students
from settings_handler import get_setting
from send_sign_out import send_checked_out_students
import time
from pathlib import Path

def main():
    day_of_week = time.strftime("%A")
    print(f"Closing Script Called On '{day_of_week}'")
    
    # called at 9:16
    if day_of_week == "Wednesday":
        handle_wednesday()
    else:
        handle_normal_day()

def handle_wednesday():
    # 30 minutes (9:46)
    time.sleep(1800)
    print("Wednesday: Task Slept For 1800 Seconds")
    send_reminder_email()
    # 15 minutes (10:01)
    time.sleep(900)
    send_not_signed_in_email()
    # 5.25 hours (3:16)
    time.sleep(18900)
    send_closing_email()

def handle_normal_day():
    send_reminder_email()
    # 15 minutes (9:31)
    time.sleep(900)
    send_not_signed_in_email()
    # 5.5 hours (3:16)
    time.sleep(20700)
    send_closing_email()

def send_closing_email():
    filename = get_log_filename()
    with open(filename, "r") as file:
        data = json.loads(file.read())
        send_checked_out_students(data)
    print("Closing email sent")

def send_reminder_email():
    filename = get_log_filename()
    with open(filename, "r") as file:
        data = json.loads(file.read())
        send_reminder_students(data)
    print("Reminder email sent")

def send_not_signed_in_email():
    filename = get_log_filename()
    with open(filename, "r") as file:
        data = json.loads(file.read())
        send_not_signed_in_students(data)
    print("Sign In Email Sent")

def get_log_filename():
    return Path(__file__).parent.absolute() / get_setting("logs-directory-path") / datetime.now().strftime("%Y-%m-%d.json")

if __name__ == "__main__":
    main()


    

