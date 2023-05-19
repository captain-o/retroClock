import schedule
import subprocess




def job():
    print('its time')



schedule.every(5).seconds.do(job)
