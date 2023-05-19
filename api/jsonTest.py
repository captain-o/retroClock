import json

directory = 'E:/Dateien/Entwicklung/retroClock/retroclockbackend/api/time.json'

with open(directory, 'r') as f:
  data = json.load(f)


print(data['time'])


newTime = json.loads('{"time":"12:34"}')


f = open(directory,"w", encoding='UTF-8' )
f.write(str(newTime))
f.close()
