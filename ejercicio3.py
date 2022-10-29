#Actividad3: Realizar una modificación al Script de la Actividad1: Detección de
#colores para poder encontrar el color azul en la imagen siguiente:
#NOTA: tomar como rangos de color azul en el Espacio de color HSV:

import cv2
import numpy as np

imagen = cv2.imread("imagenes/cuboRubik.png")

imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)  


bajo_azul = np.array([101,50,38], np.uint8)
alto_azul = np.array([110,255,255], np.uint8)   #IMPORTANTE: Tuve que cambiar los valores para una mejor detección del color azul.

maskBlue1 = cv2.inRange(imagenHSV, bajo_azul, alto_azul)    

maskBluevis = cv2.bitwise_and(imagen,imagen, mask= maskBlue1)
#La recorto
cv2.imshow("original",imagen)
cv2.imshow("Tomando lo azul",maskBlue1)
cv2.imshow("maskBluevis",maskBluevis)

cv2.waitKey(0)
cv2.destroyAllWindows()