#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:39:37 2022

@author: omari
"""
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("some_key", "Some value")
value = mc.get("some_key")









"""import thingspeak
ch = thingspeak.Channel(9)
import pickle
fp = open("shared.pkl","rb")
from time import sleep
Before = None
Before_tmp = None
while True:
    try:
        shared = pickle.load(fp)
        Before_tmp = shared["r_id"]
    except:
        pass
    if Before == Before_tmp:
        sleep(1);
        continue
    Before= Before_tmp
    print (shared)
    sleep(1)

"""