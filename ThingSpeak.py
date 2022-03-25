#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 07:01:36 2022

@author: omari
"""
import thingspeak as tks
from datetime import datetime 
class str2num:
    def __init__(self,x:str="1"):
        self.x = x
    def convert_to(self,Type=int):
        try:
            return Type(self.x)
        except:
            return None
    def is_num(self):
        for Type in [int,float]:
            if isinstance(self.covert_to(Type),Type):
                return True
        return False
import json

def moveavg(x=[],n=10):
    if n==1:return x
    A=[] if len(x)>0 else []
    for i in range(0,len(x)):
        if i<n:
            A.append(sum(x[0:i+1])/(i+1))
        else:
            A.append(sum(x[i-n+1:i+1])/(n))
    for i in range(int(n/2),len(A)-int(n/2)):
        A[i]=sum(x[i-int(n/2):i+int(n/2)])/n
    return A

#from gi.repository import Gtk as gtk
#from gi.repository import AppIndicator3 as appindicator
#from gi.repository import Notify as notify


def build_menu():
    menu = gtk.Menu()
    item_joke = gtk.MenuItem('Tank Level')
    item_joke.connect('activate', joke)
    menu.append(item_joke)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu


ch=tks.Channel(id=857679,api_key="5L42IQS51735QOH4",fmt='json')

class thing_speak(tks.Channel):
    chl_info={'name': 'Tank Station',
     'description': 'Water Level ',
     'latitude': '0.0',
     'longitude': '0.0',
     'field1': 'r_id',
     'field2': 'Distance',
     'field3': 'Ambient Temp',
     'field4': 'Humidity',
     'field5': 'Water Temperature',
     'field6': 'Battery',
     'field7': 'Sun Shin',
     'field8': 'Duration',
     'created_at': '2019-09-03T20:34:17Z',
     'updated_at': '2021-09-15T03:37:10Z',
     'last_entry_id': 282907}
    def __init__(self,chl_id=857679,api_key_r="5L42IQS51735QOH4",api_key_w="D54T1HUQSXID0IZR"):
        tks.Channel.__init__(self,chl_id)
        self.name =""
        self.api_key_r = api_key_r
        self.api_key_w =api_key_w
        self.channel_id = chl_id
        self.api_key = self.api_key_r
        for key,_ in thing_speak.chl_info.items():
            self.__dict__[key]=None
        self.__data__={}
        
    def Get(self,options=None):
        self.api_key = self.api_key_r
        __data__ = json.loads(self.get(options)) if options is not None else json.loads(self.get())
        for key,val in __data__["channel"].items():
            self.__dict__[key]=val
        self.__data__= __data__["feeds"]
        timeformat="%Y-%m-%dT%H:%M:%SZ" if "offset" not in options else f"%Y-%m-%dT%H:%M:%S{options['offset']:+03.0f}:00"
        for i in range(len(self.__data__)):
            for f_id in range(1,9):
                self.__data__[i][f"field{f_id}"]=str2num(self.__data__[i][f"field{f_id}"]).convert_to(float)
                
            self.__data__[i]['created_at']=datetime.strptime(self.__data__[i]['created_at'],timeformat)
        return self.__data__
    
    def __getattr__(self,name):
        if name.find("Field")>=0:
            fid=[x for x in name.split("Field") if x!=''][0]
            #print(fid)
            return [x[f"field{fid}"] for x in self.__data__]
        elif name.lower()=="datetime" or name.lower()=="dt":
            return [x['created_at'] for x in self.__data__]
        else:
            pass
        return None
    def __iter__(self):
        return iter(self.__data__)
    def __getitem__(self,index):
        return self.__data__[index]
    def push_to_server(self,f_id,value):
        self.api_key=self.api_key_w
        self.update(f_id,value)
        return self
if __name__=="__main__":
    ch1=thing_speak()
    ch1.Get({"results":8000,"offset":3})
    