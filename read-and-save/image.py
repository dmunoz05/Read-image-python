import cv2

#Leer imagen
img = cv2.imread('girasol.jpg', 0)

#Redimensionar imagen
cv2.resize(img, (183, 275))

#Mostrar imagen
cv2.imshow('Girasol', img)

#Esperar a que se presione una tecla para cerrar la ventana y salir
cv2.waitKey(0)

#Guardar si no existe en el path
imgSaved = cv2.imread('girasol_gris.jpg')
if(imgSaved is None):
    cv2.imwrite('girasol_gris.jpg', img)
else:
    print('La imagen ya existe')

#Cerrar todas las ventanas abiertas y salir del programa
cv2.destroyAllWindows()

