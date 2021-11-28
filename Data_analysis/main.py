import csv
import plotly.express as px
import pandas as pd

f=open('data.csv')
file_data=list(csv.reader(f))
file_data.pop(0)

data_frame=pd.read_csv('data.csv')

lev1_TRL_xsl=[]
lev1_TRL_abc=[]
lev1_TRL_xyz=[]
lev1_TRL_zet=[]
lev1_TRL_123=[]
lev1_TRL_imb=[]
lev1_TRL_rst=[]
lev1_TRL_mno=[]
lev1_TRL_987=[]
lev1_TRL_mda=[]
lev1_TRL_zny=[]

lev2_TRL_xsl=[]
lev2_TRL_abc=[]
lev2_TRL_xyz=[]
lev2_TRL_zet=[]
lev2_TRL_123=[]
lev2_TRL_imb=[]
lev2_TRL_rst=[]
lev2_TRL_mno=[]
lev2_TRL_987=[]
lev2_TRL_mda=[]
lev2_TRL_zny=[]

lev3_TRL_xsl=[]
lev3_TRL_abc=[]
lev3_TRL_xyz=[]
lev3_TRL_zet=[]
lev3_TRL_123=[]
lev3_TRL_imb=[]
lev3_TRL_rst=[]
lev3_TRL_mno=[]
lev3_TRL_987=[]
lev3_TRL_mda=[]
lev3_TRL_zny=[]

lev4_TRL_xsl=[]
lev4_TRL_abc=[]
lev4_TRL_xyz=[]
lev4_TRL_zet=[]
lev4_TRL_123=[]
lev4_TRL_imb=[]
lev4_TRL_rst=[]
lev4_TRL_mno=[]
lev4_TRL_987=[]
lev4_TRL_mda=[]
lev4_TRL_zny=[]

def sort_by_level(data):
    level=data[1]
    id=data[0]
    if level=='Level 1':
        if id=='TRL_xsl':
            lev1_TRL_xsl.append(data[2])
        elif id=='TRL_abc':
            lev1_TRL_abc.append(data[2])
        elif id=='TRL_xyz':
            lev1_TRL_xyz.append(data[2])
        elif id=='TRL_zet':
            lev1_TRL_zet.append(data[2])
        elif id=='TRL_123':
            lev1_TRL_123.append(data[2])
        elif id=='TRL_imb':
            lev1_TRL_imb.append(data[2])
        elif id=='TRL_rst':
            lev1_TRL_rst.append(data[2])
        elif id=='TRL_mno':
            lev1_TRL_mno.append(data[2])
        elif id=='TRL_987':
            lev1_TRL_987.append(data[2])
        elif id=='TRL_mda':
            lev1_TRL_mda.append(data[2])
        elif id=='TRL_zny':
            lev1_TRL_zny.append(data[2])
    elif level=='Level 2':
        if id=='TRL_xsl':
            lev2_TRL_xsl.append(data[2])
        elif id=='TRL_abc':
            lev2_TRL_abc.append(data[2])
        elif id=='TRL_xyz':
            lev2_TRL_xyz.append(data[2])
        elif id=='TRL_zet':
            lev2_TRL_zet.append(data[2])
        elif id=='TRL_123':
            lev2_TRL_123.append(data[2])
        elif id=='TRL_imb':
            lev2_TRL_imb.append(data[2])
        elif id=='TRL_rst':
            lev2_TRL_rst.append(data[2])
        elif id=='TRL_mno':
            lev2_TRL_mno.append(data[2])
        elif id=='TRL_987':
            lev2_TRL_987.append(data[2])
        elif id=='TRL_mda':
            lev2_TRL_mda.append(data[2])
        elif id=='TRL_zny':
            lev2_TRL_zny.append(data[2])
    elif level=='Level 3':
        if id=='TRL_xsl':
            lev3_TRL_xsl.append(data[2])
        elif id=='TRL_abc':
            lev3_TRL_abc.append(data[2])
        elif id=='TRL_xyz':
            lev3_TRL_xyz.append(data[2])
        elif id=='TRL_zet':
            lev3_TRL_zet.append(data[2])
        elif id=='TRL_123':
            lev3_TRL_123.append(data[2])
        elif id=='TRL_imb':
            lev3_TRL_imb.append(data[2])
        elif id=='TRL_rst':
            lev3_TRL_rst.append(data[2])
        elif id=='TRL_mno':
            lev3_TRL_mno.append(data[2])
        elif id=='TRL_987':
            lev3_TRL_987.append(data[2])
        elif id=='TRL_mda':
            lev3_TRL_mda.append(data[2])
        elif id=='TRL_zny':
            lev3_TRL_zny.append(data[2])
    elif level=='Level 4':
        if id=='TRL_xsl':
            lev4_TRL_xsl.append(data[2])
        elif id=='TRL_abc':
            lev4_TRL_abc.append(data[2])
        elif id=='TRL_xyz':
            lev4_TRL_xyz.append(data[2])
        elif id=='TRL_zet':
            lev4_TRL_zet.append(data[2])
        elif id=='TRL_123':
            lev4_TRL_123.append(data[2])
        elif id=='TRL_imb':
            lev4_TRL_imb.append(data[2])
        elif id=='TRL_rst':
            lev4_TRL_rst.append(data[2])
        elif id=='TRL_mno':
            lev4_TRL_mno.append(data[2])
        elif id=='TRL_987':
            lev4_TRL_987.append(data[2])
        elif id=='TRL_mda':
            lev4_TRL_mda.append(data[2])
        elif id=='TRL_zny':
            lev4_TRL_zny.append(data[2])        

def get_mean(data):
    num=len(data)
    sum=0
    for i in data:
        sum+=int(i)
    mean=sum/num
    return mean

for i in file_data:
    sort_by_level(i)

graph=px.scatter(data_frame,x='student_id',y='level',color='attempt')
graph.show()