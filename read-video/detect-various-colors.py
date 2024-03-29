import cv2
import numpy as np


def dibujar(mask, color, textColor):
    contornos, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 2000:
            M = cv2.moments(c)
            if (M["m00"] == 0):
                M["m00"] = 1
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])
            cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, textColor, (x+10, y), font,
                        0.75, (0, 255, 0), 1, cv2.LINE_AA)

            nuevoContorno = cv2.convexHull(c)
            cv2.drawContours(frame, [nuevoContorno], 0, color, 3)


cap = cv2.VideoCapture(0)


# Colores HSV

# Rojo
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([5, 255, 255], np.uint8)
redBajo2 = np.array([175, 100, 20], np.uint8)
redAlto2 = np.array([180, 255, 255], np.uint8)

# Naranja
orangeBajo = np.array([5, 100, 20], np.uint8)
orangeAlto = np.array([15, 255, 255], np.uint8)

# Amarillo
amarilloBajo = np.array([15, 100, 20], np.uint8)
amarilloAlto = np.array([45, 255, 255], np.uint8)

# Verde
verdeBajo = np.array([45, 100, 20], np.uint8)
verdeAlto = np.array([85, 255, 255], np.uint8)

# Azul claro
azulBajo1 = np.array([100, 100, 20], np.uint8)
azulAlto1 = np.array([125, 255, 255], np.uint8)

# Azul oscuro
azulBajo2 = np.array([125, 100, 20], np.uint8)
azulAlto2 = np.array([130, 255, 255], np.uint8)

# Morado
moradoBajo = np.array([135, 100, 20], np.uint8)
moradoAlto = np.array([145, 255, 255], np.uint8)

# Violeta
violetaBajo = np.array([145, 100, 20], np.uint8)
violetaAlto = np.array([170, 255, 255], np.uint8)


font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()

    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Detectamos los colores

        # Rojo
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1, maskRed2)

        # Naranja
        maskOrange = cv2.inRange(frameHSV, orangeBajo, orangeAlto)

        # Amarillo
        maskAmarillo = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)

        # Verde
        maskVerde = cv2.inRange(frameHSV, verdeBajo, verdeAlto)

        # Azul
        maskAzul1 = cv2.inRange(frameHSV, azulBajo1, azulAlto1)
        maskAzul2 = cv2.inRange(frameHSV, azulBajo2, azulAlto2)
        maskAzul = cv2.add(maskAzul1, maskAzul2)

        # Morado
        maskMorado = cv2.inRange(frameHSV, moradoBajo, moradoAlto)

        # Violeta
        maskVioleta = cv2.inRange(frameHSV, violetaBajo, violetaAlto)

        # Dibujamos los contornos
        dibujar(maskRed, (0, 0, 255), 'Rojo')
        dibujar(maskOrange, (0, 165, 255), 'Naranja')
        dibujar(maskAmarillo, (0, 255, 255), 'Amarillo')
        dibujar(maskVerde, (0, 255, 0), 'Verde')
        dibujar(maskAzul, (255, 0, 0), 'Azul')
        dibujar(maskMorado, (255, 0, 255), 'Morado')
        dibujar(maskVioleta, (255, 0, 255), 'Violeta')

        # Mostramos la imagen final
        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) & 0xFF == ord('s')):
            break

cap.release()
cv2.destroyAllWindows()
