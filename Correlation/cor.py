import numpy as np
import plotly_express as px
import pandas as pd
import csv

f=open('cupOfCoffee.csv','r')
file_data=list(csv.reader(f))
file_data.pop(0)
a=pd.read_csv('cupOfCoffee.csv')

cold_sales=[]
temp=[]
ice_sales=[]
for i in file_data:
    temp.append(float(i[0]))
    ice_sales.append(float(i[1]))
    cold_sales.append(float(i[2]))

corr_ice=np.corrcoef(temp,ice_sales)
corr_cold=np.corrcoef(temp,cold_sales)
corr_vs=np.corrcoef(ice_sales,cold_sales)

corr_vs=corr_vs[0,1]
corr_cold=corr_cold[0,1]
corr_ice=corr_ice[0,1]
print(corr_cold,corr_ice,corr_vs)

fig=px.scatter(a,x='Temperature',y='Ice-cream Sales( ₹ )')
fig2=px.scatter(a,x='Temperature',y='Cold drink sales( ₹ )')

fig.show()
fig2.show()