#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:59:14 2022

@author: omari
"""
from datetime import datetime
def Split(Str,char=" "):
    return [x for x in Str.split(char) if x!=""]

class detector_message:
    def __init__(self,message:str=':A0F0 0000.2 MPCA 000358 000000 00000.0 mREM/HR_',iter_id=0):
        self.__message__ = message 
        self.iteration_id = iter_id
        self.detector_SN =""
        self.flowrate_message = ""
        self.activity_concentration = 0
        self.activity_concentration_unit = "MPCA"
        self.radiation_dose_rate = 0
        self.radiation_dose_rate_unit = "mrem/hr"

        
        self.MPCa2uCi_per_m3_factor = 8.4 #Max Permissible Concerntration of Airporn Activity
        self.mrem2mSv_factor = 0.01
        #
        self.__data__list__ =[]
        self.__is_good_message__= False
        
        self.check_message()
        self.set_data()
        self.datetime=datetime.now()
        pass
    def check_message(self):
        self.__data__list__  = Split(self.__message__)
        if len(self.__data__list__ )!=7:
            self.__is_good_message__ = False
            return False
        if self.__data__list__ [0][0]!=":":
            self.__is_good_message__ = False
            return False
        self.__is_good_message__ = True
        return True
    def set_data(self):
        if self.__is_good_message__:
            #self.iteration_id=iteration_id
            self.flowrate_message=self.__data__list__[0][1:]
            self.activity_concentration = round(float(self.__data__list__[1]),2)
            self.radiation_dose_rate =round(float(self.__data__list__[5]),2)
            self.detector_SN =self.__data__list__[3]
        return self
    def set_data_2(self,message=':A0F0 0000.2 MPCA 000358 000000 00010.0 mREM/HR_',iteration_id=0):
        self.__message__=message
        self.iteration_id = iteration_id
        self.check_message()
        self.set_data()
        self.datetime=datetime.now()
        return self
#    def __getattribute__(self,name):
#        if name in object.__getattribute__(self, "__dict__"):
#            return object.__getattribute__(self,name)
#        elif name=="dose_rate":
#            return self.radiation_dose_rate*self.mrem2mSv_factor
#        elif name=="concentration":
#            return self.activity_concentration*self.MPCa2uCi_per_m3_factor
#        else:
#            return None
    def __getattr__(self, name):
        if name=="dose_rate":
            return self.radiation_dose_rate*self.mrem2mSv_factor
        elif name=="concentration":
            return round(self.activity_concentration*self.MPCa2uCi_per_m3_factor,6)
        else:
            return None
        """Called if __getattribute__ raises AttributeError"""
#        return 'close but no ' + name   
    
    def __bool__(self):
        return self.__is_good_message__
    def __getstate__(self): 
        return self.__dict__
    def __setstate__(self, d): 
        self.__dict__.update(d)
if __name__=="__main__":
    TYNE = detector_message()
    TYNE.dose_rate