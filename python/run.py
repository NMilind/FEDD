#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv
import cv2
import numpy as np
  
def doloop():

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    global depth, rgb
    while True:
        # Get a fresh frame
        (depth,_), (rgb,_) = get_depth(), get_video()
        
        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        da = np.hstack((d3,rgb))

        image = cv.fromarray(np.array(da[::2,::2,::-1]))
        gray = cv2.cvtColor(image, cv.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

        # Simple Downsample
        cv.ShowImage('both', image)
        cv.WaitKey(5)

doloop()
