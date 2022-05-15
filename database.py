#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 16:23:45 2022

@author: omari
"""
from exe_func import ProgressBar,Timer
import xlrd,openpyxl
import datetime,time
import pickle
class Timer200:
    def __init__(self,name=""):
        self.start_time = time.time()
        self.end_time   = None
        self.delta      = 0
        pass
    def Tic(self):
        self.start_time = time.time()
        return self
    def Toc(self):
        self.end_time   = time.time()
        self.delta      = self.end_time - self.start_time 
        return self
    def __str__(self):
        self.Toc()
        return f"Elapsed Time = {self.delta:10.2f} sec(s)"
    def __repr__(self):
        #print(self)
        return str(self)
    pass
###############################################################################

# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high,Index):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[Index[(low + high) // 2]]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[Index[i]] < pivot:
            i += 1

        j -= 1
        while nums[Index[j]] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        Index[i], Index[j] = Index[j], Index[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    Index=list(range(len(nums)))
    def _quick_sort(items, low, high,Index):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high,Index)
            _quick_sort(items, low, split_index,Index)
            _quick_sort(items, split_index + 1, high,Index)

    _quick_sort(nums, 0, len(nums) - 1,Index)
    return Index
def Dict_Filter(data={},function=lambda x:x>50,*arg,**kwd):
    func_name = function.__name__
    func_args = function.__code__.co_varnames
    Map={x:x for x in func_args}
    if len(kwd)!=0:
        for k,att in kwd.items():
            if k in []:
                continue
            if k in func_args:
                Map[k]=att
    #print(Map)
    length=len(data[[x for x in data.keys()][0]])
    Index=[]
    for i in range(length):
        argv=[]
        for arg in func_args:
            argv+=[data[Map[arg]][i]]
        if function(*argv)==True:
            Index.append(i)
        
    return {key:[d[i] for i in Index] for key,d in data.items()}

def quick_search(Array=[],value=1,start=0)->"index (i,i+1)":
    Mid_fun_indez = lambda x,y:int(0.5*(x+y))
    i_left,i_right=start,len(Array)-1#Mid_fun_indez(0,len(Array)-1),len(Array)-1
    #i_old,i_1_1 =cp.deepcopy((i,i_1))
    if value>Array[-1] or value<Array[0]:return None
    j=0
    if value == Array[i_right]:
            return i_right
    while i_left+1<i_right:
        i_mid = Mid_fun_indez(i_left,i_right)
        if Array[i_mid]<=value<Array[i_right]:
            i_left=i_mid
            #print("Is Up>>> Change left to mid", end="\t")
        elif Array[i_mid]>value>=Array[i_left]:
            i_right=i_mid
            #print("Is Down>>> Change right to mid",end="\t")
        else:
            return None

        #print(j,i_left,i_right,"------->",Array[i_left],Array[i_right])
        j+=1
        if j==100:
            print("Break")
            break

    return i_left
def linear_search(Array=[],value=1,start=0)->"index (i,i+1)":
    index = None
    if Array[0]==value:
        return 0
    if Array[-1]==value:
        return len(Array)-1
    for i in range(1,len(Array)):
        if Array[i-1]<=value<Array[i]:
            index=i
            break
    return index
###############################################################################
def convert_xls_datetime_to_python_datetime(excel_date:float)->datetime:
    return datetime.datetime(*xlrd.xldate_as_tuple(excel_date, 0))
class Array(list):
    def __init__(self,data=[],unit=""):
        super().__init__(data)
        self.unit = unit
        self.__Index__ = []
        self.__tmp_date__ = []
        pass
    def __filter__(self,data,func):
        if isinstance(data,(list,tuple)) or type(data)==type(Array):
            if len(self)==len(data):
                return Array(func(self[i],data[i]) for i in range(len(self)))
            return None
        else:
            return Array([func(self[i],data) for i in range(len(self))])
        return None
        map(func,self,data)
    def __getitem__(self,index):
        try:
            return super().__getitem__(index) if isinstance(index, int) else\
        Array(super().__getitem__(index),self.unit)
        except:
            if isinstance(index,(tuple,list)):
                stat = len([1 for i in index if isinstance(i,bool)])
                if stat>0:
                    return Array([self[i] for i in range(len(index)) if index[i]==True])
                return Array([self[i] for i in index])
    #     A=[x for x in self]
    #     if isinstance(index,slice):
    #         return Array(A[index])
    #     elif isinstance(index,int):
    #         return A[index]
    #     elif isinstance(index,(tuple,list)):
    #         stat = len([1 for i in index if isinstance(i,bool)])
    #         if stat>0:
    #             return Array([A[i] for i in range(len(index)) if index[i]==True])
    #         return Array([A[i] for i in index])
    #     else:
    #         return Array()
    # # =================================================================
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
    def __floordiv__(self,data):
        return self.__filter__(data,lambda a,b:a//b)
    def __mod__(self,data):
        return self.__filter__(data,lambda a,b:a%b)
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
    def __invert__(self):
        return Array([not x for x in self])
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

    def __call__(self,val):
        self.Sort()
        # i = self.find_index(val)
        # if i  in [0, len(self)] or val==self[i]:
        #     return val
        # return 0.5*(self[i]+self[i+1])
        # return self.find_index(val)
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

    def Sort(self):
        self.__Index__ = Array(quick_sort(self))
        self.__tmp_data__ = self[self.__Index__]
        return self    
    def find_index(self,val:list=[],start=0,end=None,mutli_index_search=False):
            if not isinstance(val,(tuple,list)):
                if mutli_index_search:
                    Index = Array()
                    for i in range(len(self)):
                        print(start)
                        Index.append(self.find_index(val,start))
                        if Index[-1] is None :
                            Index=Index[:-1]
                            break
                        print(Index)
                        start = Index[-1]
                        start = start+1 if start is not None else None
                        print(start)
                        if start is None:break
                        if start >= len(self):
                            break
                    return self.__Index__[Index]
                #print("search for single value")
                if 1:
                    i = quick_search(self.__tmp_data__,val,start)
                else:
                    i = linear_search(self.__tmp_data__,val,start)
                return self.__Index__[i] if i is not None else None 
            else:
                #print("search for multi value")
                return Array([self.find_index(x,mutli_index_search=mutli_index_search) for x in val])
        
            
            return Index
        
            
    
    
class Table:
    attr={"__name":"","description":"",
              "__data__":{},"__Index__":Array()}

    def __init__(self,name="",description=""):
        attr={"__name":name,"description":description,
              "__data__":{},"__Index__":Array(),
              "__Size__":(None,None,None)}
        for att,val in attr.items():
            self.__dict__[att]=val
        pass
    def __setattr__(self,name,value):
        #print(name,value)
        if name in self.__dict__:
            object.__setattr__(self,name,Array(value))
        else:
            self.__data__[name]=Array(value)
    def __setitem__(self,name,value):
        if name in self.__dict__:
            self.__dict__[name]=Array(value) if isinstance(value,(list,tuple,Array)) \
                else Array([value])
        else:
             self.__data__[name]=Array(value) if isinstance(value,(list,tuple,Array)) \
                 else Array([value])
    def __getattr__(self,name):
        if name in self.__data__:
            return self.__data__[name]#[self.__Index__] if len(self.__Index__)!=0 else self.__data__[name]
        return None
    __getitem__=__getattr__
    # def __getattribute__(self, name):
    #     print(name)
    #     if name in database.attr:
    #         if name =="__Index__":
    #             if self.__dict__[name]==[]:
    #                 self.update_index()
    #         return self.__dict__[name]
    def __str__(self):
        Str=""
        for key in self.__data__:
            Str = Str+f"{key}\n"
        return Str
    def add_attribute(self,name,data):
        Name = name
        for char in [" ","\n","\t"]+"~!@#$%^&*()-+.1234567890/".split():
            Name=Name.replace(char,"_")
        if Name not in self.__data__:
            self[Name]=Array(data)
        else:
            #Name=
            self.add_attribute(name, data)
        return self
    def append_value(self,data:list={},**attr):
        for attribute,datum in data.items():
            if attribute not in self.__data__:
                self.add_attribute(attribute,Array())
            self.__data__[attribute].append(datum)
        if len(attr)>0:
            self.append_value(data=attr)
        return self
    def import_from_xls(self,filename= "Reactor_history_2022.xls",sheet="Sheet1"):
        attribute_list=[]

        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_name(sheet)
        # Attributes = [x.replace(" ","_") for x in sh.row_values(0)]
        # if len(attribute_list)>0:
        #     attributes={attr:index for index,attr in enumerate(Attributes) if attr in attribute_list}

        # for i in range(len(Attributes)):
        #     for char in [" ","(",")"]:
        #         Attributes[i]=Attributes[i].replace(char,"_")
        # data={}
        # for i,att in enumerate(Attributes):
        #     self[att]=Array(sh.col_values(i,1))
        
        attributes = {x.replace(" ","_"):i for i,x in enumerate(sh.row_values(0))}

        if len(attribute_list)>0:
            attributes={attr:index for attr,index in attributes.items() if attr in attribute_list}
        LIMIT,COUNTER=100,0
        for i in ProgressBar(1,sh.nrows):
            data={}
            All_None=True
            for attr,index in attributes.items():
                data[attr]=sh.cell(i,index).value
                All_None = All_None and data[attr] is None
                
            if All_None:
                COUNTER+=1
            elif COUNTER!=0:
                LIMIT = 0
            if COUNTER>=LIMIT:
                print("Data importing has been stopped due to many None Values")
                break
            #print(i,COUNTER,All_None)

            if True and not All_None:
                self.append_value(data)

        
        return self
    def import_from_xlsx(self,filename="omari.xlsx",sheet="omari",
                         append=False,attribute_list=[],start_row=1):
        timer =Timer()
        try:
            print(f"opening excel file -> filename = {filename} -> sheet = {sheet}")
            wb = openpyxl.load_workbook(filename=filename,read_only=False,data_only=True)
            print("loading file is done. ",timer)
            
            sh = wb[sheet]
            row1 = sh[start_row]
            attributes = {str(row1[i].value):i for i in range(len(row1))
                          if row1[i].value is not None}
            #print(attributes)
            if len(attribute_list)>0:
                attributes={attr:index for attr,index in attributes.items() if attr in attribute_list}
            if len(attributes)==0:
                wb.close()
                print("Noting to import")
                return self
            if not append:
                for att in attributes:
                    self[att]=Array()
            max_row = sh.max_row
            #print(attributes)
            # print(attributes.keys())

            # for att,index in attributes.items():
                
            #     Col_Letter = openpyxl.utils.get_column_letter(index)
            #     print(f"Importing data -->{att} -> [{Col_Letter}2:{Col_Letter}{max_row}]")
            #     data=Array([x[0].value for x in sh[f"{Col_Letter}2:{Col_Letter}{max_row}"]])
            #     #data=[]
            #     self.add_attribute(att, data)
            LIMIT,COUNTER=100,0
            for i in ProgressBar(start_row+1,max_row+1):
                # data = [x.value for x in sh[i]]
                
                # if sum([1 for _ in data if _ is not None])==0:
                #     LIMIT+=1
                # elif LIMIT!=0:
                #     LIMIT = 0
                # if COUNTER<=LIMIT:
                #     break
                # data={att:data[i-1] for att,i in attributes.items()}
                # #print(data)
                data={}
                All_None=True
                for attr,index in attributes.items():
                    data[attr]=sh.cell(i,index+1).value
                    All_None = All_None and data[attr] is None
                    
                if All_None:
                    COUNTER+=1
                elif COUNTER!=0:
                    LIMIT = 0
                if COUNTER>=LIMIT:
                    print("Data importing has been stopped due to many None Values")
                    break
                #print(i,COUNTER,All_None)

                if True and not All_None:
                    self.append_value(data)
                
            print("Importing data has been done. closing the file.[",timer)
            wb.close()
            #return sh,wb
            return self
        except:
            print(f"Error in importing data for {filename}")
            return wb
            wb.close()
        
        return self
        pass
    def Sort(self,attribute="",reverse=False,save=False):
        Index = Array(quick_sort(self[attribute]))
        if reverse:
            Index=Array([Index[i] for i in range(len(Index)-1,-1,-1)])
        self.__Index__=Array(Index)
        if save:
            self.save()
            return self
        return Index
    
    def save(self):
        for attribute,datum in self.__data__.items():
            #print("Saving_filtered data to ",attribute)
            self[attribute]=datum[self.__Index__]
            #self.__data__[attribute]=datum[self.__Index__]
            #self.__data__[attribute].unit=datum.unit
            # the unit to be assinded
        return self

    def Filter(self,function=lambda x:x>50,*arg,**kwd):
        data = self.__data__
        func_name = function.__name__
        func_args = function.__code__.co_varnames
        Map={x:x for x in func_args}
        if len(kwd)!=0:
            for k,att in kwd.items():
                if k in []:
                    continue
                if k in func_args:
                    Map[k]=att
        #print(":::::::::::::::::::::")
        print(Map)
        length=len(data[[x for x in data.keys()][0]])
        Index=[]
        for _,key in Map.items():
            if key not in data.keys():
                #print("*-*-*-*-*-*-*-*-*-*")
                pass
                #return self
        #print("22:::::::::::::::::::::")
        #print(func_args)
        for i in range(length):
            argv=[]
            for arg in func_args:
                #print(i,arg,Map[arg],data[Map[arg]][i])
                argv+=[data[Map[arg]][i]] if Map[arg] in data.keys() else [Map[arg]]
            #print(argv)
            if function(*argv):
                Index.append(i)
            
        self.__Index__ = Array(Index,unit="index")
        return self
    
    def __len__(self):
        LENs =[len(x) for _,x in db.__data__.items()]
        #print()
        self.__Size__= len(self.__data__),min(LENs),max(LENs)
        return max(LENs)
    
    def __str__(self):
        STR = "\n"+"-"*50+"\n"
        for att,val in self.__data__.items():
            STR+=f"{att:50}: {len(val)}\n"
        return STR
    def __repr__(self):
        return str(self)
    
    def __contains__(self,name):
        return name in self.__data__ 

    
    def link_attibutes_with_main_dict(self):
        for ky,data in self.__data__.items():
            self.__dict__[ky]=data
        return self
    
    def set_index(self,index):
        self.__Index__=index
        return self
    
    def reset_index(self):
        self.__Index__=Array()
    
    def update_index(self):
        self.__Index__=list(range(min([len(d) for _,d in self.__data__.items()])))
        return self
    
    def __iter__(self):
        return iter(self.__data__.items())
    def export_to_xlsx(self,filename="omari.xlsx",sheet="omari",attribute_list=[]):
        timer=Timer()
        wb = openpyxl.Workbook()
        sh = wb.create_sheet(sheet)
        column_index=1
        for attribute,data in self:
            if len(attribute_list)>0 and attribute not in attribute_list:
                continue
            sh.cell(1,column_index,attribute)
            for index,value in enumerate(data):
                sh.cell(index+2,column_index,value)
            column_index+=1
        print(timer)
        wb.save(filename)
        print(timer)
        return self
    # -------------------------------------------------------------------------
    def link_attibutes_with_main_dict(self):
        for ky,data in self.__data__.items():
            self.__dict__[ky]=data
        return self
    #
    def set_index(self,index):
        self.__Index__=index
        return self   
    def reset_index(self):
        self.__Index__=Array() 
    def update_index(self):
        #print(">>> Updating the database index array")
        self.__Index__=Array(range(max([len(d) for _,d in self.__data__.items()])))
        self.__data__["__db_i__"]=Array(range(max([len(d) for _,d in self.__data__.items()])))
        return self
    # -------------------------------------------------------------------------
    def add_function(self, *func):
        for f in func:
            if f.__name__ in self.__dict__:
                continue
            self.__dict__[f.__name__] = f.__get__(self)
            #self.__fun_list.append(f.__name__)
            pass
    def rm_function(self, *func_name):
        for fn in func_name:
            if fn in self.__fun_list:
                del self.__dict__[fn]
                self.__fun_list.remove(fn)
                pass
            pass
        pass
    def rplc_function(self, func_name, func):
        if func_name in self.__fun_list:
            self.RmFunc(func_name)
            self.AddAttribute(func)
        pass
    # -------------------------------------------------------------------------
    def Export(self,Locals=locals()):
        for x in self.attibute_dict:
            Locals[x]=self[x]
            pass
    def Share_memcache(self,host="localhost:11211"):
        key = "omari"
        from memcache import Client
        mc = Client([host])
        mc.set(key,db)
        return self
    # =========================================================================
    def save_to_pickle(self,filename):
        with open(filename,"bw") as fid:
            pickle.dump(self,fid)
        return self
    def load_from_pickle(self,filename):
        with open(filename,"br") as fid:
            self= pickle.load(fid)
        return self
    def __getstate__(self): 
        return self.__dict__
    def __setstate__(self, d): 
        self.__dict__.update(d)
    
    def __contains__(self,name):
        return name in self.__data__

# *****************************************************************************
database=Table
# *****************************************************************************

if __name__=="__main__":
    # from pylab import *
    # from math import *
    Timer1=Timer()
    A=Array([float(i)*.01 for i in range(1,1000)])
    print(Timer1)
    #B=(A.func(exp)).func(sqrt)
    def xx(A):
        print(dir())
    #xx(A)
    #plot((A)(),B()),grid()
    db = database()
    print(Timer1)

    #print(dir())
    #plot(A,2*A+2)
    def fun1(self,x=1):
        return x+len(self)
    A=db.import_from_xlsx()#attribute_list=["FPD"])
    print(len(db))
    db.import_from_xlsx(append=True)#attribute_list=["FPD"])
    print(len(db))

    print(Timer1)




# if __name__=="__main__":
#     from pylab import *
#     from math import *
#     A=Array([float(i)*.01 for i in range(1,1000)])
#     B=(A.func(exp)).func(sqrt)
#     def xx(A):
#         print(dir())
#     #xx(A)
#     #plot((A)(),B()),grid()
#     db = database()
#     #print(dir())
#     #plot(A,2*A+2)
    
#     db.import_from_xls()
#     db.rx_startup_date = db.Rx_Startup_Date.func(convert_xls_datetime_to_python_datetime)