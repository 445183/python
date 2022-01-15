import numpy as np
from sklearn.linear_model import LogisticRegression
import csv
import matplotlib.pyplot as plt

f=open('data.csv')
raw_data=list(csv.reader(f))
raw_data.pop(0)

velocity_l=[]
escape_l=[]
for i in raw_data:
    velocity=float(i[0])
    escape=float(i[1])

    velocity_l.append(velocity)
    escape_l.append(escape)

X=np.reshape(velocity_l,(len(velocity_l),1))
Y=np.reshape(escape_l,(len(escape_l),1))

lr=LogisticRegression()
lr.fit(X,Y)

plt.figure()
plt.scatter(X.ravel(),Y,color='red',zorder=20)

def model(x):
    return 1/(1+np.exp(-x))
X_test=np.linspace(0,50,100)

escape_chance=model(X_test*lr.coef_+lr.intercept_).ravel()
plt.plot(X_test,escape_chance,color='black',linewidth=3)
plt.xlim(min(velocity_l),max(velocity_l))

plt.show()