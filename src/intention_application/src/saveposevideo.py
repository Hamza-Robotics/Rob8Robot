import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
fps = int(cap.get(cv.CAP_PROP_FPS)/2)

validation= cv.VideoWriter("/home/hamza/yesintention1.avi",cv.VideoWriter_fourcc(*'MJPG'),fps, size)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here

    validation.write(frame)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
validation.release()

cv.destroyAllWindows()