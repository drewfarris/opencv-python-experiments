import numpy as np
import cv2

cap = cv2.VideoCapture(0)

index = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width, channels = frame.shape

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord(' '):
        fname = "images/image-%d.jpg" % (index)
        cv2.imwrite(fname, gray)
        index += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
