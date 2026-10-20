import cv2
import numpy as np
def applyfilter(image, ftype):
    image = image.copy()
    if ftype == "redtint":
        image[:,:,1]= image[:,:,0]=0
    elif ftype == "greentint":
        image[:,:,2]= image[:,:,0]=0
    elif ftype == "bluetint":
        image[:,:,1]= image[:,:,2]=0
    elif ftype =="sobel":
        gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1,0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=3)
        sobel= cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
        image = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
    elif ftype =="canny":
        gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray,100,200)
        image = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    elif ftype=="cartoon":
        gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray= cv2.medianBlur(gray, 5)
        edge= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9)
        color = cv2.bilateralFilter(image, 9,300,300)
        image = cv2.bitwise_and(color,color,mask=edge)
    return image
def main():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cant open camera")
        return
    ftype ="original"
    print("keys: r = RED, b=Blue, g=GREEN, s=SOBEL, c=CANNY, m=motionBLUR")
    while True:
        ret, frame=cap.read()
        if not ret:
            print("Frame not available")
            break
        out=applyfilter(frame,ftype)
        cv2.imshow("FILTER",out)
        key= cv2.waitKey(1)&0xFF
        if key == ord('r'):
            ftype = "redtint"
        elif key == ord('g'):
            ftype = "greentint"
        elif key == ord('b'):
            ftype = "bluetint"
        elif key == ord('s'):
            ftype = "sobel"
        elif key == ord('c'):
            ftype = "canny"
        elif key == ord('m'):
            ftype = "cartoon"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ =='__main__':
    main()
