import cv2
import numpy as np
def applyfilter(image,filter_type):
    filteredimage = image.copy()
    if filter_type =="red_tint":
        filteredimage[:, :, 1]=0
        filteredimage[:, :, 0]=0
    elif filter_type =="blue_tint":
            filteredimage[:, :, 1]=0
            filteredimage[:, :, 2]=0
    elif filter_type =="green_tint":
            filteredimage[:, :, 0]=0
            filteredimage[:, :, 2]=0
    elif filter_type =="increase_blue":
          filteredimage[:, :, 0] = cv2.add(filteredimage[:, :, 0], 80)
    elif filter_type =="decrease_red":
            filteredimage[:, :, 2] = cv2.subtract(filteredimage[:, :, 2], 80)
    return filteredimage
imagepath = 'tree.jpg'
image = cv2.imread(imagepath)
if image is None:
    print("Error no image")
else:
    filter_type = "original"
    print("Press following keys to apply the following filters:")
    print("r Red")
    print("b Blue")
    print("g Green")
    print("a increase blue")
    print("s decrease red")      
    print("q Quit")
    while True:
        filteredimage = applyfilter(image, filter_type)
        cv2.imshow("Filtered Image", filteredimage)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            filter_type="red_tint"
        elif key == ord('b'):
            filter_type="blue_tint"
        elif key == ord('g'):
            filter_type="green_tint"
        elif key == ord('a'):
            filter_type="increase_blue"
        elif key == ord('s'):
            filter_type="decrease_red"
        elif key == ord('q'):
            print("Exiting")
            break
        else:
            print("Invalid key Please use a correct one")
cv2.destroyAllWindows()
                    