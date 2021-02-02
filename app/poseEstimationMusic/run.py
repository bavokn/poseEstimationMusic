import numpy as np
import cv2

cap = cv2.VideoCapture(0)
image = cv2.imread('files/images/person.jpeg')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print(cap)
        print("could not open webcam")
        break
    # Display the resulting frame
    cv2.imshow('image', cv2.pyrDown(image))

    cv2.imshow('webcam', cv2.pyrDown(frame))
    cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
