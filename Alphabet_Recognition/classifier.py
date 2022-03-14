from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from PIL import Image

X=np.load('image.npz')['arr_0']
y=pd.read_csv('labels.csv')

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=2500,train_size=7500,random_state=9)
X_train=X_train/255.0
X_test=X_test/255.0

clf=LogisticRegression(solver='saga',multi_class='multinomial').fit(X_train,y_train)
y_pred=clf.predict(X_test)
accu=accuracy_score(y_test,y_pred)
print("The accuracy of the prediction model is: ",str(accu*100),'%')

def image_processing(image):
    im_pil=Image.open(image)
    im_pil_bw=im_pil.convert('L')
    im_pil_resized=im_pil_bw.resize((28,28),Image.ANTIALIAS)
    pixel_filter=20
    min_pixel=np.percentile(im_pil_resized,pixel_filter)
    im_pil_final=np.clip(im_pil_resized-min_pixel,0,255)
    max_pixel=np.max(im_pil_resized)
    im_pil_final=np.asarray(im_pil_resized)/max_pixel

    test_sample=np.array(im_pil_final,).reshape(1,784)
    return test_sample

def alphabet_recognition(image):
    y_val=image_processing(image)
    test_pred=clf.predict(y_val)
    return test_pred