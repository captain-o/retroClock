import datetime
from pytz import timezone


fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# Current time in UTC
now_utc = datetime.datetime.now(timezone('UTC'))
print(now_utc.strftime(fmt))



# Convert to Europe/Berlin time zone
now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
print(now_berlin.strftime(fmt))

#print(datetime.datetime.now().time())
print(datetime.datetime.now().strftime("%H%M"))
#.strftime("%Y-%m-%d %H:%M:%S")
