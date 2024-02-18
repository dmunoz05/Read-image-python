#Libreria
import cv2
import numpy as np

img = cv2.imread("girasol.jpg")
img = cv2.resize(img,(300,250))

imgGray0 = cv2.imread("girasol.jpg", 0)
imgGray0 = cv2.resize(imgGray0, (300, 250))

#Kernel
kernel = np.ones((5, 5), np.uint8)

#Imagen original
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
imgCanny = cv2.Canny(img, 200, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Gris 1", imgGray)
cv2.imshow("Imagen Gris 2", imgGray0)
cv2.imshow("Imagen Blur", imgBlur)
cv2.imshow("Imagen Canny", imgCanny)
cv2.imshow("Imagen Dilatacion", imgDilation)
cv2.imshow("Imagen Eroded", imgEroded)
cv2.waitKey(0)