#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 16:23:45 2022

@author: omari
"""

class Array(list):
    def __init__(self,data=[]):
        for d in data:
            self.append(d)
            pass
        pass
    def __filter__(self,data,func):
        if isinstance(data,(list,tuple)) or type(data)==type(Array):
            if len(self)==len(data):
                return Array(func(self[i],data[i]) for i in range(len(self)))
            return None
        else:
            return Array([func(self[i],data) for i in range(len(self))])
        return None
    def __getitem__(self,index):
        A=[x for x in self]
        if isinstance(index,slice):
            return Array(A[index])
        elif isinstance(index,int):
            return A[index]
        elif isinstance(index,(tuple,list)):
            if True in index or False in index:
                return Array([A[i] for i in range(len(index)) if index[i]==True])
            return Array([A[i] for i in index])
        else:
            return Array()
    # =================================================================
    def __add__(self,data):
        return self.__filter__(data,lambda a,b:a+b)
    __radd__=__add__
    def __sub__(self,data):
        return self.__filter__(data,lambda a,b:a-b)
    def __rsub__(self,data):
        return self.__filter__(data,lambda a,b:b-a)
    def __neg__(self):
        return self.__filter__(-1,lambda a,b:a*b)
    def __mul__(self,data):
        return self.__filter__(data,lambda a,b:a*b)
    __rmul__=__mul__
    def __rtruediv__(self,data):
        return self.__filter__(data,lambda a,b:b/a)
    def __truediv__(self,data):
        return self.__filter__(data,lambda a,b:a/b)
    def __pow__(self,data):
        return self.__filter__(data,lambda a,b:a**b)
    # =================================================================
    def __gt__(self,data):
        return self.__filter__(data,lambda a,b:a>b)
    def __ge__(self,data):
        return self.__filter__(data,lambda a,b:a>=b)
    def __lt__(self,data):
        return self.__filter__(data,lambda a,b:a<b)
    def __le__(self,data):
        return self.__filter__(data,lambda a,b:a<=b)
    def __eq__(self,data):
        return self.__filter__(data,lambda a,b:a==b)
    def __ne__(self,data):
        return self.__filter__(data,lambda a,b:a!=b)
    def __and__(self,data):
        return self.__filter__(data,lambda a,b:a and b)
    def __or__(self,data):
        return self.__filter__(data,lambda a,b:a or b)
    # ==================================================================
#    def __getattribute__(self,name):
#        #print(name,"=============>>>>")
#        return super().__getattribute__(name)
#    
##    def __getattr__(self,name):
##
##        if len(name)<10:
##            print(name,"--=====>>>-")
##        if name == "shape":
##            return [self[i] for i in range(len(self))]
##        return [1,3]

    def __call__(self):
        return [self[i] for i in range(len(self))]
    def __cmp__(self,value):
        print("-------------->>>>>>>>>>",value)
    # 
    def func(self,func):
        return Array([func(x) for x in self])
    def __name__(self):
        return [k for k,v in globals().items() if v is self]
    
#    def __array_struct__(self):
#        return  [self[i] for i in range(len(self))]

class database:
    def __init__(self,name="",description=""):
        attr={"__name":name,"description":description,"__data__":{}}
        for att,val in attr.items():
            self.__dict__[att]=val

        pass
    def __setattr__(self,name,value):
        print(name,value)
        if name in self.__dict__:
            object.__setattr__(self,name,value)
        else:
            self.__data__[name]=value
    def __setitem__(self,name,value):
        if name in self.__dict__:
            self.__dict__[name]=value
        else:
             self.__data__[name]=value
    def __getattr__(self,name):
        if name in self.__data__:
            return self.__data__[name]
        return None
    __getitem__=__getattr__
    
    def add_attribute(self,name,data):
        self[name]=data
        return self



if __name__=="__main__":
    from pylab import *
    from math import *
    A=Array([float(i)*.01 for i in range(1,1000)])
    B=(A.func(exp)).func(sqrt)
    def xx(A):
        print(dir())
    #xx(A)
    #plot((A)(),B()),grid()
    db = database()
    #print(dir())
    #plot(A,2*A+2)