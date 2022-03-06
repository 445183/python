import pandas as pd
import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps 

X=np.load('image.npz')['arr_0']
y=pd.read_csv('labels.csv')

classes=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sample_class=5

fig=plt.figure(figsize=(len(classes),sample_class))
idx_class=0

for cls in classes:
    idxs=np.flatnonzero(y==cls)
    idxs=np.random.choice(idxs,sample_class,replace=False)

    i=0
    for idx in idxs:
        plt_idx=i*len(classes)+idx_class+1

        p=plt.subplot(sample_class,len(classes),plt_idx)
        p=sns.heatmap(np.reshape(X[idx],(22,30)),cmap=plt.cm.gray,xticklabels=False,yticklabels=False,cbar=False)
        p=plt.axis('off')
        i+=1
    idx_class+=1

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=9,train_size=7500,test_size=2500)
X_train=X_train/255.0
X_test=X_test/255.0

clf=LogisticRegression(solver='saga',multi_class='multinomial').fit(X_train,y_train)
y_pred=clf.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)

cap=cv2.VideoCapture()

while True:
    try :
        ret,frame=cap.read()

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        height,width=gray.shape()

        p1=(int(width)/2-56,int(height)/2-56)
        p2=(int(width)/2+56,int(height)/2+56)
        rectangle=cv2.rectangle(gray,p1,p2,(0,255,0),5)

        roi=gray[p1[0]:p2[0],p1[1]:p2[1]]
        im_pil=Image.fromarray(roi)
        im_pil1=im_pil.convert('L')
        im_pil2=im_pil1.resize((28,28),Image.ANTIALIAS)
        im_pil3=PIL.ImageOps.invert(im_pil2)
        pixel_filter=20

        min_pixel=np.percentile(im_pil3,pixel_filter)
        max_pixel=np.max(im_pil3)

        image=np.clip(im_pil-min_pixel,0,255)
        
        img_arr=np.asarrray(image)/max_pixel
        test_sample=np.array(img_arr).reshape((1,784))

        test_pred=clf.predict(test_sample)
        print('Predicted class is: ',test_pred)

        cv2.imshow('frame',gray)
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break
    except:
        pass

cap.release()
cv2.destroyAllWindows()