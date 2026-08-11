import cv2
image = cv2.imread('tree.jpg')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resizedimage = cv2.resize(grayimage, (500,500))
cv2.imshow('Resized Image', resizedimage)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale_processed_image.jpg', resizedimage)
    print('Image saved as grayscale_preocessed_image.jpg ')
else:
    print('Error image not saved')
cv2.destroyAllWindows()
print(f"Processed dimensions = {resizedimage}")