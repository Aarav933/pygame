import cv2 
import numpy as np
import matplotlib.pyplot as plt
def displayimage(title, image):
    plt.figure(figsize=(5,5))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()
def interactiveedgedetection(imagepath):
    image = cv2.imread(imagepath)
    if image is None:
        print("IMage not found")
        return
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
    displayimage("grayscale image", grayimage)
    print("Select an option")
    print("1Sobel")
    print("2CAnny")
    print("3LAplacian")
    print("4Gaussian")
    print("5Median")
    print("6Exit")
    while True:
        choice = input("ENter an option (1-6)")
        if choice == "1":
            sobelx = cv2.Sobel(grayimage, cv2.CV_64F , 1,0, ksize = 3)
            sobely = cv2.Sobel(grayimage, cv2.CV_64F , 0,1, ksize = 3)
            combinedsobel = cv2.bitwise_or(sobelx.astype(np.uint8), 
            sobely.astype(np.uint8))
            displayimage("Sobel Edge Detection", combinedsobel)
        elif choice =="2":
            print("Canny treshhold : 100-200")
            lowerthresh = int(input("Enter lower treshhold:  "))
            upperthresh = int(input("Enter upper threshhold:  "))
            edges =cv2.Canny(grayimage, lowerthresh, upperthresh)
            displayimage("Canny Threshhold", edges)
        elif choice =="4":
            print("GAussian must be odd number")
            kernelsize = int(input("Enter kernel size(odd number):  "))
            blurred = cv2.GaussianBlur(image,(kernelsize, kernelsize), 0)
            displayimage("Blureedimage", blurred)

        else:
            print("invalid choice")
interactiveedgedetection("tree.jpg")

