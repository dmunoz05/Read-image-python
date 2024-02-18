import cv2
import numpy as np

img = np.zeros((300, 600, 3),np.uint8)
cv2.namedWindow('Imagen')

def nothing(x):
    pass

cv2.createTrackbar('Rojo', 'Imagen', 0, 255, lambda x: nothing(x))
cv2.createTrackbar('Verde', 'Imagen', 0, 255, lambda x: nothing(x))
cv2.createTrackbar('Azul', 'Imagen', 0, 255, lambda x: nothing(x))


switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'Imagen', 0, 1, lambda x: nothing(x))


while True:
    r = cv2.getTrackbarPos('Rojo', 'Imagen')
    g = cv2.getTrackbarPos('Verde', 'Imagen')
    b = cv2.getTrackbarPos('Azul', 'Imagen')
    s = cv2.getTrackbarPos(switch, 'Imagen')

    if(s == 0):
        img[:] = 0
    else:
        img[:] = [b, g, r]

    cv2.imshow('Imagen', img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()