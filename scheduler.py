#! /home/avalanche/anaconda3/envs/deep0/bin/python
import time
import os
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from config import global_config

STUID=global_config.getRaw('config','STU_ID')
PASSWD=global_config.getRaw('config','PASSWD')



def log_online():
    log=open("/home/avalanche/Desktop/auto_online/doc.txt",'a+')
    driver=webdriver.Firefox()
    driver.get("http://10.0.0.55/srun_portal_pc?ac_id=1&theme=bit")
    time.sleep(5)
    username=driver.find_element_by_id("username")
    try:
        username.send_keys(STUID)
    except ElementNotInteractableException:
        res="username input not found, maybe already online?"
        driver.close()
        cur_time=time.ctime()
        log.write(cur_time+': ')
        log.write(res+'\n')
        log.close()
        return
    
    time.sleep(2)
    passwd=driver.find_element_by_id("password")
    try:
        passwd.send_keys(PASSWD)
    except ElementNotInteractableException:
        res="password input was not interactable..."
        driver.close()
        cur_time=time.ctime()
        log.write(cur_time+': \n')
        log.write(res+'\n')
        log.close()
        return
    time.sleep(2)
    try:
        login_but=driver.find_element_by_id("login")
    except:
        res="no login found..."
        driver.close()
        cur_time=time.ctime()
        log.write(cur_time+': \n')
        log.write(res+'\n')
        log.close()
        return
    login_but.click()
    
    res_succ="login success!"
    succ_time=time.ctime()
    log.write(succ_time+': ')
    log.write(res_succ+'\n')
    time.sleep(5)
    driver.close()
    log.close()



log_online()


