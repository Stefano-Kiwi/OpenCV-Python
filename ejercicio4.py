#Actividad3: Realizar un script que permita leer/cargar la imagen siguiente:
# Agregar contorno de color verde a ambas señales viales.
# Agregar texto de color verde con la leyenda “Alerta al conductor”.
import cv2
import numpy as np

imagen = cv2.imread("imagenes/ruta.jpg")

imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)  #Convierto la imagen de BGR a HSV
redBajo1 = np.array([0,0,0], np.uint8) 
redBajo2 = np.array([8,255,255], np.uint8)
redAlto1 = np.array([8,255,255], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

maskRed1 = cv2.inRange(imagenHSV, redBajo1, redAlto1)   #Imagen binaria, blanco = encontro el color
maskRed2 = cv2.inRange(imagenHSV, redBajo2, redAlto2)   #Negro = no está ese color presente

maskRed = cv2.add(maskRed1,maskRed2)    ## Tenemos como resultado una imagen binaria
maskRedvis = cv2.bitwise_and(imagen,imagen, mask= maskRed)
#La recorto
cv2.imshow("original",imagen)
cv2.imshow("maskRed",maskRed)
cv2.imshow("maskRedvis",maskRedvis)

cv2.waitKey(0)
cv2.destroyAllWindows()