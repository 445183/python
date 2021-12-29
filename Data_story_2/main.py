import statistics as stats
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import csv, random
import numpy as np

df=pd.read_csv('data.csv')
f=open('data.csv')
raw_data=list(csv.reader(f))
raw_data.pop(0)

fig_raw=px.scatter(df,y='quant_saved',color='wealthy',size='quant_saved')
fig_raw.show()

data_gender_m=[]
data_gender_f=[]
for i in raw_data:
    gender=int(i[1])
    if gender==1:
        data_gender_f.append(float(i[0]))
    else:
        data_gender_m.append(float(i[0]))

fig_quant_m=ff.create_distplot([data_gender_m],['Money saved by males :'],show_hist=False)
fig_quant_f=ff.create_distplot([data_gender_f],['Money saved by females :'],show_hist=False)

mean_saved_m=stats.mean(data_gender_m)
mean_saved_f=stats.mean(data_gender_f)
print("Money saved by men, ₹",mean_saved_m,", Money saved by women, ₹",mean_saved_f)

q1=df['quant_saved'].quantile(0.25)
q3=df['quant_saved'].quantile(0.75)
q_range=q3-q1

iqr_1=q1-(1.5*q_range)
iqr_2=q3+(1.5*q_range)

new_df=df[df['quant_saved']>iqr_1]
new_df=new_df[new_df['quant_saved']<iqr_2]

fig=ff.create_distplot([new_df['quant_saved']],['Savings: '],show_hist=False)
fig.show()

mean_list=[]
for i in range(0,100):
    raw_data_list=[]
    saving=new_df['quant_saved'].to_list()
    for i in range(0,1000):
        rand_index=random.randint(0,len(saving)-1)
        value=float(saving[rand_index])
        raw_data_list.append(value)
    mean_list.append(stats.mean(raw_data_list))

fig_final=ff.create_distplot([mean_list],['Savings (sampled):'],show_hist=False)
fig_final.show()

fig_quant_m.show()
fig_quant_f.show()

corr_wealthy=np.corrcoef(new_df['quant_saved'],new_df['wealthy'])
print(corr_wealthy[0,1])