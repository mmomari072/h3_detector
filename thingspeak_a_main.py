#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:55:25 2022

@author: omari
"""
from __future__ import print_function
#import urllib2
import urllib
class thingspeak_a:
    def __init__(self,api_key='D54T1HUQSXID0IZR'):
        self.baseURL = 'http://api.thingspeak.com/update?'
        self.api_key = api_key
        self.__full_url__ =""
    def init(self):
        self.__full_url__ = self.baseURL+"api_key="+self.api_key
        return self
    def set_field_val(self,field_id=1,value=2):
        self.__full_url__+="&field{field_id}={value}".format(field_id=field_id,value=value)
        return self
    def push_to_server(self):
        try:
           # print(self.__full_url__)
            f = urllib.request.urlopen(self.__full_url__)
            f.read()
            f.close()	
            self.init
        except:
            return None
        return self

if __name__=="__main__":
    A=thingspeak_a()
    from time import sleep
    for i in range(1000):
        A.init()
        A.set_field_val(3,i)
        A.push_to_server()
        sleep(5)
    
        
