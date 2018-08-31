import cv2
import sys

#face cascades
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

#set video source to default camera
video_capture = cv2.VideoCapture(0)

while True:
    #capturing frame 
    # ret: return tells us if we have ran ut of frames
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors = 5, minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE)
    

    #draw rectangles around afces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #display the frame
    cv2.imshow('vid',frame)

    # exit script
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release capture

video_capture.release()
cv2.destroyAllWindows()
    


