import cv2
import numpy as np
import matplotlib.pyplot as plt

# Procesando la imagen
RuteImg = 'dorito13.jpg'
Img = cv2.imread(RuteImg)
imgGray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
Imagen_hsv = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)
ImgResize = cv2.resize(np.uint8(imgGray), (50, 50))

# Detectar contornos
listSingleContourn = []

# Colores HSV
# Naranja
orangeBajo = np.array([5, 100, 20], np.uint8)
orangeAlto = np.array([15, 255, 255], np.uint8)

# Amarillo
amarilloBajo = np.array([15, 100, 20], np.uint8)
amarilloAlto = np.array([45, 255, 255], np.uint8)


def searchContour(mask):
  contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  return contornos


def draw(mask, color, textColor, img, ruta):
  contornos = searchContour(mask)
  for c in contornos:
      area = cv2.contourArea(c)
      if area > 2000:
          M = cv2.moments(c)
          if (M["m00"] == 0):
              M["m00"] = 1
          x = int(M["m10"]/M["m00"])
          y = int(M["m01"]/M["m00"])
          cv2.circle(img, (x, y), 7, (0, 255, 0), -1)
          font = cv2.FONT_HERSHEY_SIMPLEX
          cv2.putText(img, textColor, (x+10, y), font, 0.95, (0, 255, 0), 1, cv2.LINE_AA)
          newContourn = cv2.convexHull(c)
          cv2.drawContours(Img, [newContourn], 0, color, 3)
          # Añadir contorno
          listSingleContourn.append({"contorno": newContourn, "Ruta": ruta})

#Leer imagen
frameHSV = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)

# Mascara naranja y amarillo
maskOrange = cv2.inRange(frameHSV, orangeBajo, orangeAlto)
maskYellow = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
maskOrangeAndYellow = cv2.add(maskOrange, maskYellow)

# Dibujamos los contornos
draw(maskOrangeAndYellow, (0, 165, 255), 'Centro', Img, RuteImg)

# Procesar imagen
plt.imshow(Img, cmap='gray')
plt.title('Imagen en escala de grises')
plt.axis('off')
plt.show()
