import csv
import statistics

f=open('height-weight.csv','r')
file=csv.reader(f)
file_data=list(file)

file_data.pop(0)

newData=[]
for i in range(0,len(file_data)):
    newData.append(float(file_data[i][2]))

newData.sort()
n=len(newData)

if n%2==0:
    m1=float(newData[n//2])
    m2=float(newData[n//2+1])

    median=(m1+m2)/2
else:
    m1=float(newData[n//2])
    median=m1

print("Median =",median)

print(statistics.median(newData))