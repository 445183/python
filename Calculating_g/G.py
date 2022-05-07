import pandas as pd
import csv

df=pd.read_csv('data.csv')

Vmag=list(df['V mag.'])
Name=list(df['Proper Name'])
Bayer=list(df['Bayer designation'])
Distance=list(df['Distance'])
Spectral=list(df['Spectral class'])
mass=list(df['Mass'])
radius=list(df['Radius'])
luminosity=list(df['Luminosity'])

headers=['V mag.','Proper Name','Bayer designation','Distance','Spectral class','Mass','Radius','Luminosity','g']
g_list=[]

G=6.67*(10**-11)
M=1988500000000000000000000000000.0
R=1390000000.0

for i in range(0,97):
    star_mass=mass[i]
    star_radius=radius[i]

    try:
        star_mass=float(star_mass)
        star_radius=float(star_radius)

        absolute_mass=star_mass*M
        absolute_radius=star_radius*R

        g=(absolute_mass*G)/(absolute_radius**2)
        g=str(g)+' m/s^2'

        g_list.append(g)

    except:
        g='undefined'

        g_list.append(g)

star_Data=[]
for i in range(0,97):
    temp=[]
    a1,a2,a3,a4,a5,a6,a7,a8,a9=Vmag[i],Name[i],Bayer[i],Distance[i],Spectral[i],mass[i],radius[i],luminosity[i],g_list[i]
    temp=[a1,a2,a3,a4,a5,a6,a7,a8,a9]

    star_Data.append(temp)

with open('final.csv','w',newline='',encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(star_Data)