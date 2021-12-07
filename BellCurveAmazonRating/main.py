import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv('data.csv')
fig=ff.create_distplot([df['Avg Rating']],['Rating of smartphones'],show_hist=False)
fig.show()

f=open('data.csv')
data=list(csv.reader(f))
data.pop(0)

Samsung=[]
Apple=[]
Motorola=[]
Nokia=[]
Huawei=[]
Sony=[]
Google=[]
Xiaomi=[]
Asus=[]

for i in data:
    name=i[1]
    if name=='Samsung':
        Samsung.append(float(i[2]))
    elif name=='Apple':
        Apple.append(float(i[2]))
    elif name=='Motorola':
        Motorola.append(float(i[2]))
    elif name=='Nokia':
        Nokia.append(float(i[2]))
    elif name=='HUAWEI':
        Huawei.append(float(i[2]))
    elif name=='Sony':
        Sony.append(float(i[2]))
    elif name=='Google':
        Google.append(float(i[2]))
    elif name=='Xiaomi':
        Xiaomi.append(float(i[2]))
    elif name=='ASUS':
        Asus.append(float(i[2]))

Sam=ff.create_distplot([Samsung],['Samsung phone ratings'],show_hist=False)
Sam.show()
App=ff.create_distplot([Apple],['Apple phone ratings'],show_hist=False)
App.show()
Mot=ff.create_distplot([Motorola],['Motorola phone ratings'],show_hist=False)
Mot.show()
Nok=ff.create_distplot([Nokia],['Nokia phone ratings'],show_hist=False)
Nok.show()
Hua=ff.create_distplot([Huawei],['Huawei phone ratings'],show_hist=False)
Hua.show()
Son=ff.create_distplot([Sony],['Sony phone ratings'],show_hist=False)
Son.show()
Gol=ff.create_distplot([Google],['Google phone ratings'],show_hist=False)
Gol.show()
Xia=ff.create_distplot([Xiaomi],['Xiaomi phone ratings'],show_hist=False)
Xia.show()
Asu=ff.create_distplot([Asus],['Asus phone ratings'],show_hist=False)
Asu.show()