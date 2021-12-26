import statistics as stats
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import csv

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

fig_quant_m.show()
fig_quant_f.show()