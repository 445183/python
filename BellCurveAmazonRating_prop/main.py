import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics as stats
import plotly.graph_objects as go

df=pd.read_csv('data.csv')
fig=ff.create_distplot([df['Avg Rating']],['Rating of smartphones'],show_hist=False)

mean_rating=stats.mean(df['Avg Rating'])
print("Mean of the ratings of the smartphones' is, ",mean_rating)

sd=stats.stdev(df['Avg Rating'])

sd1_l=mean_rating-sd
sd1_u=mean_rating+sd

sd2_l=mean_rating-(2*sd)
sd2_u=mean_rating+(2*sd)

sd3_l=mean_rating-(sd*3)
sd3_u=mean_rating+(sd*3)

fig.add_trace(go.Scatter(x=[mean_rating,mean_rating],y=[0,0.7],mode='lines',name='Mean'))

fig.add_trace(go.Scatter(x=[sd1_l,sd1_l],y=[0,0.7],mode='lines',name='Standard deviation 1 start;'))
fig.add_trace(go.Scatter(x=[sd1_u,sd1_u],y=[0,0.7],mode='lines',name='Standard deviation 1 end.'))
n_sd1=len([result for result in df['Avg Rating'] if result>sd1_l and result<sd1_u])
per1=n_sd1/len(df['Avg Rating'])*100

print("The percenatge of data which lies in range of standard deviation 1 is {}%".format(per1))

fig.add_trace(go.Scatter(x=[sd2_l,sd2_l],y=[0,0.7],mode='lines',name='Standard deviation 2 start;'))
fig.add_trace(go.Scatter(x=[sd2_u,sd2_u],y=[0,0.7],mode='lines',name='Standard deviation 2 end.'))
n_sd2=len([result for result in df['Avg Rating'] if result>sd2_l and result<sd2_u])
per2=n_sd2/len(df['Avg Rating'])*100

print('The percentage of data which lies in range of standard deviation 2 is {}%'.format(per2))

fig.add_trace(go.Scatter(x=[sd3_l,sd3_l],y=[0,0.7],mode='lines',name='Standard deviation 3 start;'))
fig.add_trace(go.Scatter(x=[sd3_u,sd3_u],y=[0,0.7],mode='lines',name='Standard deviation 3 end.'))
n_sd3=len([result for result in df['Avg Rating'] if result>sd3_l and result<sd3_u])
per3=n_sd3/len(df['Avg Rating'])*100

print('The percentage of data which lies in range of standard deviation 3 is {}%'.format(per3))

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