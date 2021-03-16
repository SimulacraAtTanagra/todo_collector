# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:07:28 2021

@author: shane
"""

import os

def todo_collect(repofolder): #single use function to repair readmes written previously
    subdirs = [x[0] for x in os.walk(repofolder) if "src" not in x[0] and "git" not in x[0]]          
    #msg="Daily automated update"
    final=[]
    for foldername in subdirs:
        for file in [y for y in os.listdir(foldername) if '.py' in y]:
            filename=os.path.join(foldername,file)
            with open(filename,'r') as f:
                xyz=f.readlines()
            xyz=[f'{file} - {x}' for x in xyz if "#TODO" in x]
            final.extend(xyz)
    return(final)
def main(repofolder=None):
    if repofolder:
        repofolder=repofolder
    else:
        repofolder='c://where//you//keep//repos'
    todos=todo_collect(repofolder)
    for ix,todo in enumerate(todos):
        print(ix,todo)
        
    
if __name__=="__main__":
    main(repofolder=REPO)