import schedule
import subprocess
import time
import json
import datetime
#import testSound as alarm
import csv
import pandas as pd
from flask import Flask, request
import json


week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
weekday = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["saturday", "sunday"]

#alarm.playAlarm
#print(datetime.datetime.now().time())
def job():
    print('its time')
    subprocess.call('python testSound.py', shell=True)

def get_weekdays(frequency):
    if (frequency == "weekday"):
        return week
    elif (frequency == "weekend"):
        return weekend
    elif (frequency == "week"):
        return week
    else:
        return week


def create_jobs(frequency, time, id):
    if (frequency == "weekday"):
        schedule.every().monday.at(time).do(job).tag(id)
        schedule.every().tuesday.at(time).do(job).tag(id)
        schedule.every().wednesday.at(time).do(job).tag(id)
        schedule.every().thursday.at(time).do(job).tag(id)
        schedule.every().friday.at(time).do(job).tag(id)
        print(f"set alarm {id} at {time} on weekday")

    elif (frequency == "weekend"):
        schedule.every().saturday.at(time).do(job).tag(id)
        schedule.every().sunday.at(time).do(job).tag(id)
        print(f"set alarm {id} at {time} on weekend")

    elif (frequency == "week"):
        schedule.every().day.at(time).do(job).tag(id)
        print(f"set alarm {id} at {time} on week")

    else:
        schedule.every().day.at(time).do(job).tag(id)
        print(f"set alarm {id} at {time} on week")


def on_startup():
    with open('testDatabase.json', 'r') as f:
        data = json.load(f)

    for alarm in data:
        id = "job" + str(alarm["id"])
        time = alarm["time"]
        frequency = alarm["frequency"]
        create_jobs(frequency, time, id)
        #days = get_weekdays(frequency)
    return data
    print("alarms set")

def create_job(job):
    id = job["id"]
    time = job["time"]
    frequency = job["frequency"]
    create_jobs(frequency, time, id)
    db.append(job)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/alarms')
def get_data():
    #all_jobs = schedule.get_jobs()
    return db

@app.route('/api/setalarm', methods=['POST'])
def set_alarm():
    data = request.json
    print(f'post: {data}')
    create_job(data)
    print(schedule.get_jobs())

    return json.dumps({'message': 'Data processed successfully'})





all_jobs = schedule.get_jobs()
print(all_jobs)
db = on_startup()

#print(schedule.get_jobs('job2'))
all_jobs = schedule.get_jobs()
print(all_jobs)


if __name__ == '__main__':
    app.run()
    while True:
        schedule.run_pending()
        time.sleep(30)
