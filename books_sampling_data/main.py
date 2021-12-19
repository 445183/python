import statistics as stats
import random
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv('medium_data.csv')
fig=ff.create_distplot([df['reading_time']],['Reading time of book:'],show_hist=False)
fig.show()

def get_sample_data(counter):
    data=[]
    r_time=df['reading_time'].to_list()
    for i in range(0,counter):
        rain=random.randint(0,len(df['reading_time']))
        value=r_time[rain]
        data.append(value)
    a=stats.mean(data)
    return a

def repeater():
    mean_list=[]
    for i in range(0,100):
        mean=get_sample_data(100)
        mean_list.append(mean)
    plot_graph(mean_list)

def plot_graph(i):
    fig=ff.create_distplot([i],['Reading time of book:'],show_hist=False)
    fig.show()

repeater()