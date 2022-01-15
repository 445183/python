from sklearn.linear_model import LogisticRegression as lr
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler as ss
import pandas as pd

df=pd.read_csv('data.csv')
results=df['Chance of admit']
factors=df[['GRE Score','TOEFL Score']]

f_tr,f_ts,r_tr,r_ts=train_test_split(factors,results,test_size=0.25)
sc=ss()
f_tr=sc.fit_transform(f_tr)
f_ts=sc.transform(f_ts)

lr_predictor=lr(random_state=0)
lr_predictor.fit(f_tr,r_tr)
pred=lr_predictor.predict(f_ts)

accu=accuracy_score(r_ts,pred)
print(accu)