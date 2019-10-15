# -*- coding: utf-8 -*-
"""
cron job
"""

	
import datetime


with open('C:\Users\Admin\Desktop\Bao_Cao\dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))