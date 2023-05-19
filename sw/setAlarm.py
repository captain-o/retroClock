import json
import os
import datetime



directory = 'E:/owncloud/Coden/raspiSpielerei/Wecker/nextAlarm.json'


with open(directory) as f:
  data = json.load(f)



print(data["time"])
time = data["time"]


date_time_str = time
date_time_obj = datetime.datetime.strptime(time, '%H:%M')


print('Time:', date_time_obj.time())
