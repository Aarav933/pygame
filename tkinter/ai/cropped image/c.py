import cv2
import matplotlib.pyplot as plt
image = cv2.imread('car.jpg')
imagerbg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(imagerbg)
plt.title("Rgb image")
plt.show()
image = cv2.imread('car.jpg')
imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(imagegray, cmap="gray")
plt.title("Grayscale image")
plt.show()
croppedimage = image[100:300, 200:400]
croppedrgb = cv2.cvtColor(croppedimage, cv2.COLOR_BGR2RGB)
plt.imshow(croppedrgb)
plt.title("Cropped image")
plt.show()