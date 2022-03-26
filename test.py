#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:19:53 2022

@author: omari
"""

from messages_classes import *
from time import sleep
if 1:
    import memcache
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
else:
    from pymemcache.client.base import Client
    mc = Client('127.0.0.1:11211')
    
with open("data","r") as fid:
    i = 0
    for line in fid:
        message=line.replace("[","").replace("]","").replace(","," ").replace("'"," ").strip()
        TYNE_DETECTOR=detector_message(message,i)
        TYNE_DETECTOR.set_data_2(message,i)
        TYNE_DETECTOR.check_message()
        if TYNE_DETECTOR:
            mc.set("__TYNE_DETECTOR_MESSAGE__",TYNE_DETECTOR)
            print("sending data")
        i+=1
        print(TYNE_DETECTOR.__message__)
        sleep(0.01)

