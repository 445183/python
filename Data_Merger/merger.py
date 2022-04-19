import csv
import pandas as pd

file1 = 'brown_dwarfs.csv'
file2 = 'starData.csv'

file1_data = []
file2_data = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        file1_data.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        file2_data.append(i)

h1 = file1_data[0]
h2 = file2_data[0]

p_file1_data = file1_data[1:]
p_file2_data = file2_data[1:]

h = h1+h2

p_d =[]

for i in p_file1_data:
    p_d.append(i)
for j in p_file2_data:
    p_d.append(j)
with open("final.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('final.csv')
df.tail(8)