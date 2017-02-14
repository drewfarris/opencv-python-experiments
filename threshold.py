import numpy as np
import cv2

cap = cv2.VideoCapture(0)

t1 = 70
t2 = 255

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width, channels = frame.shape

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh1 = cv2.threshold(blur, t1, t2, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    text = "t1: %d; t2: %d" % (t1, t2)
    cv2.rectangle(thresh1, (0,0), (300, 40), (0,0,0), thickness=-1)
    cv2.putText(thresh1, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)


    # Display the resulting frame
    cv2.imshow('frame',thresh1)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('w'):
        t1 += 10
    elif key == ord('s'):
        t1 -= 10
    elif key == ord('e'):
        t2 += 10
    elif key == ord('d'):
        t2 -= 10

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
