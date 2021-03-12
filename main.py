import os
import time
from datetime import datetime
from threading import Timer
from config import global_config

TIME_SPAN=int(global_config.getRaw('config','INTERVAL'))
PROJ_DIR=global_config.getRaw('config','PROJ_DIR')
PYTHON_DIR=global_config.getRaw('config','PYTHON_DIR')

def task():
    os.system('cd '+PROJ_DIR+ ' && ' +PYTHON_DIR+ ' scheduler.py')
    cur_time=time.ctime()
    log_file=global_config.getRaw('config','LOG')
    f=open(log_file,'a+')
    f.write(cur_time+': ')
    f.write("scheduler executed...\n")
    f.close()

while True:
    timer=Timer(5,task,())
    timer.start()
    time.sleep(TIME_SPAN)
