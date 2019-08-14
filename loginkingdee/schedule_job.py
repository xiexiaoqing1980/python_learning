#!/usr/bin/env python3                                       #文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-                                      #表示.py文件本身使用标准UTF-8编码
' demo to automatically runn python scripts '                 #任何模块代码的第一个字符串都被视为模块的文档注释；
__author__='xinna_xie'
 
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import loginkingdee 
def job():
    print("task executed at  ",datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    loginkingdee.authorize()

scheduler=BlockingScheduler()
# scheduler.add_job(job, 'date' ,run_date=datetime(2018, 11, 9, 23, 10, 5))

scheduler.add_job(job, 'interval' ,seconds=30 ,start_date="2018-11-09 23:15:00")   #按时间间隔执行作业
scheduler.start()