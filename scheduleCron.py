# -*- coding: utf-8 -*-
"""
len lich cho cronjob writeDate.py
"""

	
from crontab import CronTab
from datetime import datetime

# define crontab not existed
my_cron  = CronTab(use = 'trang', tab="""* * * * * command""")
job = my_cron.new(command='python C://Users//Admin//Desktop//Bao_Cao//Job_writeDate.py', comment='dateinfo')
# len lich thuc thi job
job.minute.every(1)    
# ghi job vao cron tab
my_cron.write()


# kiem tra job trong crontab
my_cron = CronTab(user='trang')
for job in my_cron:
    if job.comment == 'dateinfo':
        print (job)
        #len lich lai cho job 
        job.minute.every(10)
        my_cron.write()



# giai phong job khoi crontab
my_cron = CronTab(user='trang')
for job in my_cron:
    if job.comment == 'dateinfo':
        my_cron.remove(job)
        my_cron.write()
        

# kiem tra lich bieu cua job     # pip install croniter
my_cron = CronTab(user='trang')
for job in my_cron:
    sch = job.schedule(date_from=datetime.datetime.now())
    print (sch.get_next())