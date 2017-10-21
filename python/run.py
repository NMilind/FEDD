#!/usr/bin/env python
import freenect as fn
import cv
import cv2
import frame_convert2 as fc
import numpy as np
import time

def get_depth():
	return fn.sync_get_depth()[0]
	#return fc.pretty_depth_cv(fn.sync_get_depth()[0])

def get_video():
	return fn.sync_get_video()[0]
	#return fc.video_cv(fn.sync_get_video()[0])

def frame_loop():

	cascPath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)

	#cv2.namedWindow("Depth")
	cv2.namedWindow("Video")

	while True:
		# Get a fresh frame
		#depth = get_depth()
		rgb = get_video()

		# Convert to grayscale for face analysis
		start = time.time()
		gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
		end = time.time()
		print("Gray Conversion: %s" % (end - start))

		start = time.time()
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30,30)
		)
		end = time.time()
		print("Face Detection: %s" % (end - start))

		# Draw rectangles around faces
		start = time.time()
		for (x, y, w, h) in faces:
			try:
				cv2.rectangle(rgb, (x,y), (x+w, y+h), (0, 255, 0), 2)
				print "(%s, %s)" % (x, y)
			except:
				pass
		end = time.time()
		print("Drawing Rectangles: %s" % (end - start))

		# Simple Downsample
		#cv2.imshow("Depth", depth);
		cv2.imshow("Video", rgb);
		if (cv2.waitKey(10) == 27):
			break;

frame_loop()
