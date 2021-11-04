import csv
import statistics

f=open('height-weight.csv','r')
file=csv.reader(f)
file_data=list(file)

file_data.pop(0)

newData=[]
for i in range(0,len(file_data)):
    newData.append(file_data[i][2])

total_val=0
data=[]
for i in newData:
    total_val+=float(i)
    data.append(float(i))

n=len(newData)

mean=total_val/n

print("Mean = ",mean)

mean=statistics.mean(data)
print(mean)