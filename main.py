import os
import time
from datetime import datetime as dt
import smtplib
import email

def check_file_age(folder_path: str, age_threshold: int):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            mod_datetime = dt.fromtimestamp(mod_time)
            current_time = dt.now()
            file_age_days = (current_time - mod_datetime).days
            
            if file_age_days > age_threshold:
                print(f'The file {file_path} is {file_age_days} old')
                

folder_path = os.path.join(os.path.expanduser('~'), 'Desktop/dns')
age_threshold = 20

check_file_age(folder_path, age_threshold)


