# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:07:28 2021

@author: shane
"""
from typing import List
import os

def get_py_files(path):
    #find all py files, even if there is nesting
    filelist=[]
    for dirpath, subdirs, files in os.walk(path):
        filelist.extend([os.path.join(dirpath, x) for x in files if x.endswith('.py')])
    return(filelist)

def todo_collect(filenames:List[str])-> List[str]: 
    """
    Accepts list of filenames and returns sorted set list of TODOs
    """
    final=[]
    for filename in filenames:
        with open(filename,'r') as f:
            xyz=f.readlines()
        file=filename.split('\\')[-1]
        xyz=[f'{file} - line {ix} - {x.strip()}' for ix,x in enumerate(xyz) if "#TODO" in x and '"#TODO"' not in x]
        final.extend(xyz)
    return(sorted(list(set(final))))
        
def main(repofolder=None,outfile=None):
    if repofolder:
        repofolder=repofolder
    else:
        repofolder=os.getcwd()
    todos=todo_collect(get_py_files(repofolder))
    if outfile:
        print(todos,file=outfile)
    else:
        for ix,todo in enumerate(todos):
            print(ix+1,todo)
    
if __name__=="__main__":
    main()