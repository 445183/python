import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)
time.sleep(2)

bg=cv2.imread('bg.png')
bg=np.resize(bg,(480,640,3))

while (cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break

    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_b=np.array([30,30,0])
    upper_b=np.array([104,153,70])

    masking=cv2.inRange(hsv,lower_b,upper_b)
    res=cv2.bitwise_and(hsv,hsv,mask=masking)

    f=hsv-res
    f=np.where(f==0,bg,f)

    final_output=cv2.addWeighted(img, 1, res, 1, 0)
    output_file.write(final_output)
    cv2.imshow("magic", final_output)
    cv2.waitKey(1)

cap.release()
output_file.release()
cv2.destroyAllWindows()