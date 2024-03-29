import cv2
import numpy as np


cap = cv2.VideoCapture(0)

azulBajo = np.array([100, 100, 20], np.uint8)
azulAlto = np.array([125, 255, 255], np.uint8)

while True:
    rest, frame = cap.read()

    if rest == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV, azulBajo, azulAlto)
        maskBlue = cv2.add(mask, mask)
        maskRedvis = cv2.bitwise_and(frame, frame, mask=maskBlue)

        cv2.imshow("maskBlueAplicate", maskRedvis)
        # cv2.imshow("maskBlue", mask)
        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) & 0xFF == ord('s')):
          break

cap.release()
cv2.destroyAllWindows()
