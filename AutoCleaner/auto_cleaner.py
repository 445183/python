import os
import shutil
import time

def deleteFolder(path):
    shutil.rmtree(path)

def deleteFile(path):
    os.remove(path)

def findLastAccesedTime(path):
    a_time=os.path.getatime(path)
    return a_time

cur_tim = time.time()
folder=input("Enter the folder name which you would like to cleanse: ")
time=float(input("Enter the time period of files you would like to save, remaining would get deleted (in days): "))
files = os.listdir(folder)
tim_per=cur_tim-(time*24*60*60)

for file in files:
    name,ext = os.path.splitext(file)
    t=findLastAccesedTime(folder+'/'+file)
    if ext=='':
        if tim_per>=t:
            deleteFolder(folder+'/'+file)
    else :
        if tim_per>=t:
            deleteFile(folder+'/'+file)