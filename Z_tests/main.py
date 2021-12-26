import statistics as stats
from numpy import mod
import plotly.figure_factory as ff
import random
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv('data1.csv')

maths_score=df['Math_score'].to_list()
mean=stats.mean(maths_score)
stdev=stats.stdev(maths_score)
print('The mean and the stand.dev for complete population are, {} & {} respectively.'.format(mean,stdev))

def get_random_means(counter,list):
    data=[]
    for i in range(0,counter):
        rain=random.randint(0,len(list)-1)
        value=list[rain]
        data.append(value)
    m=stats.mean(data)
    return m

def setup():
    mean_list=[]
    for i in range(0,100):
        mean=get_random_means(100,maths_score)        
        mean_list.append(mean)
    mean_sd=stats.mean(mean_list)
    stdev_sd=stats.stdev(mean_list)
    print(mean_sd,stdev_sd)

    df1=pd.read_csv('data2.csv')
    ms=df1['Math_score(inter1)'].to_list()
    mean_s1=stats.mean(ms)
    print(mean_s1)

    df2=pd.read_csv('data3.csv')
    ms2=df2['Math_score(inter2)'].to_list()
    mean_s2=stats.mean(ms2)
    print(mean_s2)

    df3=pd.read_csv('data4.csv')
    ms3=df3['Math_score(inter3)'].to_list()
    mean_s3=stats.mean(ms3)
    print(mean_s3)

    fig=ff.create_distplot([mean_list],['Maths marks:'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean_sd,mean_sd],y=[0,0.2],mode='lines',name='Mean of samples'))
    fig.add_trace(go.Scatter(x=[mean_s1,mean_s1],y=[0,0.2],mode='lines',name='Mean of inter. 1'))
    fig.add_trace(go.Scatter(x=[mean_s2,mean_s2],y=[0,0.2],mode='lines',name='Mean of inter. 2'))
    fig.add_trace(go.Scatter(x=[mean_s3,mean_s3],y=[0,0.2],mode='lines',name='Mean of inter. 3'))
    fig.show()

setup()