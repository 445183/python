import numpy as np
import csv
import plotly.express as px

f=open('data.csv')
raw_data=list(csv.reader(f))
raw_data.pop(0)

gre_score=[]
chances=[]
for i in raw_data:
    chance=float(i[8])
    score=int(i[1])

    gre_score.append(score)
    chances.append(chance)

m,c=np.polyfit(gre_score,chances,1)
y=[]

for x in gre_score:
    y_value=x*m+c
    y.append(y_value)

fig=px.scatter(x=gre_score,y=chances)
fig.update_layout(shapes=[dict(
        type='line',
        y0=min(y),y1=max(y),
        x0=min(gre_score),x1=max(gre_score)
)])
fig.show()