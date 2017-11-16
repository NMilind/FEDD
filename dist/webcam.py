import sys
import time
import servo_control

# Set the path to the OpenCV installation on the RPi
sys.path.append("/usr/local/lib/python3.5/site-packages")

# Set up lambda function for current time in milliseconds
get_time = lambda: int(round(time.time() * 1000))

# Import OpenCV
import cv2

# Suggested resolution for webcam
WIDTH = 213
HEIGHT = 160

# Cascade stylesheet containing face characteristics
cascPath = "haarcascade_frontalface_default.xml"
# Set the profile for OpenCV
faceCascade = cv2.CascadeClassifier(cascPath)

# Begin video capture with suggested resolution
video_capture = cv2.VideoCapture(0)
video_capture.set(3, WIDTH)
video_capture.set(4, HEIGHT)

x_past = [0, 0, 0]

start_time = 0
end_time = 0

MOVE = float(sys.argv[1])

# Initialize servo module

servo_control.initialize()

frameskip = 0

while True:

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    # Obtain true width and height of each frame
    height, width, channels = frame.shape

    # Convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=0
    )

    end_time = get_time()
    delta_t = end_time - start_time
    start_time = get_time()

    # Draw a rectangle around the faces and compute deltas
    for (x, y, w, h) in faces:

        # Remove last elements in history
        x_past = x_past[0:2]

        # Calculate midpoints of face
        MID_X = (x + (w / 2.0))
        VEL_X = (MID_X - (WIDTH / 2))**2 # x_past[0]) / delta_t

        # Add new values to history
        x_past = [MID_X] + x_past

        if frameskip >= 2:
            VEL_X = (x_past[2] - (WIDTH / 2))
            # Send input to servo module to move servo
            servo_control.handle_input(VEL_X, delta_t, MOVE)

        print("Face at X=%s | Movement: %s" % (MID_X, VEL_X))
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frameskip += 1

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
