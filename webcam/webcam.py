import sys
sys.path.append("/usr/local/lib/python3.5/site-packages")

import cv2

WIDTH = 213
HEIGHT = 160

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
video_capture.set(3, WIDTH)
video_capture.set(4, HEIGHT)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=0
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        MID_X = (x + (w / 2.0))
        MID_Y = (y + (h / 2.0))
        print("Face at (%s, %s)" % (MID_X, MID_Y))
        # cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    # cv2.imshow('Video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()