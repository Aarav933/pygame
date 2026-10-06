import cv2
facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cant open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Image not captured")
        break
    grayscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = facecascade.detectMultiScale(grayscale, scaleFactor=1.1,minNeighbors=5, minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'people counted: {len(faces)}', (20,20),font,1,(0,0,255), 2, cv2.LINE_AA)
    cv2.imshow('Face Tracking ', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()