import cv2
import matplotlib.pyplot as plt
imagepath = 'car.jpg' 
image = cv2.imread(imagepath)
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height , width,_= imagergb.shape
rect1width, rect1height = 100 , 100
topleft1 = (20,20)
bottomright1 = (topleft1[0]+rect1width, topleft1[1]+rect1height)
cv2.rectangle(imagergb, topleft1, bottomright1, (255,50,255), 2)
rect2width , rect2height = 200,150
topleft2 = (width-rect2width-20,height-rect2height-20)
bottomright2 = (topleft2[0]+rect2width, topleft2[1]+rect2height)
cv2.rectangle(imagergb, topleft2, bottomright2, (255,255,50),2)
center1x = topleft1[0] +rect1width //2
center1y = topleft1[1] +rect1height //2
center2x = topleft2[0] +rect2width //2
center2y = topleft2[1] +rect2height //2
cv2.circle(imagergb, (center1x, center1y), 15, (0,255,255),-1)
cv2.circle(imagergb, (center2x, center2y), 15, (0,255,255),-1)
cv2.line(imagergb, (center1x, center1y), (center2x, center2y), (0,255,255),2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagergb, 'Region 1', (topleft1[0], topleft1[1]-10), font, 0.7 , (255,255,255), 2, cv2.LINE_AA)
cv2.putText(imagergb, 'Region 2', (topleft2[0], topleft2[1]-10), font, 0.7 , (255,255,255), 2, cv2.LINE_AA)
cv2.putText(imagergb, 'Center1', (center1x-40, center1y+40), font, 0.7 , (255,255,255), 2, cv2.LINE_AA)
cv2.putText(imagergb, 'Center2', (center2x-40, center2y+40), font, 0.7 , (255,255,255), 2, cv2.LINE_AA)
arrowstart = (width-50,20)
arrowend = (width-50, height-20)
plt.figure(figsize=(12,8))
plt.imshow(imagergb)
plt.axis('off')
plt.show()
