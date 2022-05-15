# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:44:06 2020

@author: mohammed.omari
"""

from time import time,sleep
class ProgressBar:
    def __init__(self,start=0,end=100,n=100,message='',Draw=True):
        self.name = ""
        self.length = end-start
        self.percentage=0
        self.char="="
        self.index = 0
        self.start = start
        self.end   = end
        self.step  = 1
        self.timer =Timer()
        self.char_length = 50
        self.message = message
        self.__tmp =-1
        self.draw = Draw
        pass
    def __draw__(self):
        if not self.draw:
            return
        if self.length<1: 
            return
        self.percentage=float(self.index-1)/self.length
        if self.percentage<0:
            #print('How Come',self.index,self.length)
            #from sys import exit
            #return
            self.percentage = 0
            #exit(1) 
        l = int(self.percentage*self.char_length)
        self.timer.Toc()

        if l == self.__tmp*1:
            pass
        else:
            timeformat="%02i:%02i:%05.2f"
            #print('\r%s'%(' '*90),end='')
            print("\r[%s%s] (%6.2f%%,e=%s,r=%s) %s"%(
                    '\x1b[1;31;42m'+self.char*l+'\x1b[0m',' '*(self.char_length-l),
                    self.percentage*100,
                    timeformat%self.timer.elapsed(),
                    timeformat%self.timer.remaining(self.length-self.index+1),
                    self.message
                    ),
                    end='\x1b[0m')
            self.__tmp=l
            #print(self.length-self.index+1)
    
    def __iter__(self):
        self.__draw__()
        self.timer.Tic()
        self.current=0
        return self

    def __next__(self):
        if self.index >= self.length:
            self.index+=1
            self.__draw__()
            print()
            #
            raise StopIteration
        else:
            self.index += 1
            self.__draw__()
            return self.index-1+self.start
# =============================================================================
class Timer:
    def __init__(self):
        self.start = None
        self.previous = None
        self.last = None
        self.diff  = 0
        self.diff_2= 0
        self.rate = None
        self.__T_convert = [60*60,60]
        self.print_toc   = False
        pass
    def Tic(self):
        self.start=time()
        self.last=self.start
        self.previous=self.start
        #return self
        pass
    def Toc(self):
        self.last = time()
        if self.start is not None:
            self.diff = self.last-self.start
            self.diff_2 = self.last-self.previous
            self.previous = self.last
            pass
        else:
            self.Tic()
#        self.rate = 1/self.diff
        if self.print_toc:
            print(self)
        return self
    
    def elapsed(self,n=4):
        t=[]
        tt = self.diff
        for i in self.__T_convert :
            t.append(int(tt/i))
            tt-=t[-1]*i
            pass
        t.append(tt)
        return tuple(t)
    def remaining(self,step):
        t=[]
        #print(self.diff_2)
        tt = self.diff_2*(step)
        for i in self.__T_convert :
            t.append(int(tt/i))
            tt-=t[-1]*i
            pass
        t.append(tt)
        return tuple(t)
    
    def __repr__(self):
        t = self.array()
        if len(self.__T_convert)==3:
            Ts = "Elapsed time %02i:%02i:%02i:%05.2f"%t
        else:
            Ts = "Elapsed time %3i:%02i:%05.2f"%t
        return Ts
    
    def array(self):
        return self.elapsed()     
    pass

if __name__=="__main__":
    for i in ProgressBar(0,200):
        print(i)