import cv2

rute = 'dorito13.jpg'

img = cv2.imread(rute)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagen', imgGray)
cv2.waitKey(0)