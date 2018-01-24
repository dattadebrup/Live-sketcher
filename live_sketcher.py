#live sketcher
import cv2
import time
import numpy as np
test_frame=20
frames_count=0
def sketch(image):
    #img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurring
    gauss_blur = cv2.bilateralFilter(image, 10, 25, 25)
    
    #edge detection
    canny = cv2.Canny(gauss_blur, 30, 110)
    
    #inverting threshold
    ret,invert = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY_INV)
    return invert
cap= cv2.VideoCapture(0)
fps=0
while(cap.isOpened()):
    t=time.time()
    while(frames_count<=test_frame):
        ret,img=cap.read()
        frame=sketch(img)
        cv2.putText(frame,str(fps), (10,25), cv2.FONT_HERSHEY_COMPLEX, 1, (100,170,0), 1)
        cv2.imshow("canny",frame)
        frames_count=frames_count+1
        k=cv2.waitKey(1)
        if k==27:
            break
    if k==27:
            break
    fps=frames_count/(time.time()-t-0.001*frames_count)
    frames_count=0
cap.release()
cv2.destroyAllWindows()