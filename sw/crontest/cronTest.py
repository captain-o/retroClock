from crontab import CronTab

cron = CronTab(user='pi')
#cron = CronTab()
job = cron.new(command='python3 /home/pi/Documents/example1.py')
job.minute.every(1)

cron.write()
