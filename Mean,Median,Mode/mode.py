from collections import Counter
import csv
f=open('height-weight.csv','r')
file=csv.reader(f)
file_data=list(file)

file_data.pop(0)

newData=[]
for i in range(0,len(file_data)):
    newData.append(file_data[i][2])

n = len(newData)
  
data = Counter(newData)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)