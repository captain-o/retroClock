import schedule
import subprocess
import time
import datetime
import json
#import testSound as alarm



#alarm.playAlarm
print(datetime.datetime.now().time())

def job():
    print('its time')
    subprocess.call('python E:/owncloud/Coden/raspiSpielerei/Wecker/sw/testSound.py', shell=True)



# load time
def getAlarmTime():

    file = "E:/owncloud/Coden/raspiSpielerei/Wecker/api/time.json"
    with open(file, 'r') as f:
      data = json.load(f)
      #print(data)
    alarmTime = data['time']
    #print(alarmTime)
    return alarmTime


schedule.clear()
schedule.every().day.at(getAlarmTime()).do(job)

print(str(schedule.jobs))

count = 0


while True:
    curAlarm = getAlarmTime()
    if not curAlarm in str(schedule.jobs):
        print("newAlarm")

    print(str(schedule.jobs))
    schedule.run_pending()
    time.sleep(1)
