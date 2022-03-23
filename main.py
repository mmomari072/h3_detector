#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:39:38 2022

@author: omari
"""
import pickle
from datetime import datetime
from messages_classes import *
import serial
import memcache

mc = memcache.Client(["127.0.0.1:11211"])
mc_var_attribute = "__TYNE_DETECTOR_MESSAGE__"
fp = open(f"TYNE_00358_[{datetime.now()}].peckle","wb")
port_name = '/dev/ttyS0'
import serial

ser = serial.Serial(port = port_name,baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)
i=0
while True:
    try:
        ser_bytes = ser.readline()
        A = detector_message(ser_bytes.decode("utf-8"),i)
        A.set_data_2(ser_bytes.decode("utf-8"),i)
    
        if not A:
            continue
        mc.set(mc_var_attribute,A)
        pickle.dump(A, fp)
        #sock.sendall(bytes(m,encoding="utf-8"))

        i+=1
        fp.flush()

    except:
        print("Keyboard Interrupt")

        break
    
ser.close()
fp.close()