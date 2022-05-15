# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 07:02:49 2022

@author: mohammed.omari
"""

from os import system

def import_list():
    with open("F:\\list") as fid:
        return [line.strip().split()[0] for line in fid][2:]
    

status ={}
for a in import_list():
    status[a]=system(f"pip install -U {a}")

with open("F:\\Status.pip","w") as fid:
    for a,stat in status.items():
        print(f"{a},{stat}",file=fid)
        
    