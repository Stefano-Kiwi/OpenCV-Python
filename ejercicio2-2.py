#Actividad2: Realizar las 2 aplicaciones prácticos presentados en la clase 5:
# -Detección de colores
import cv2
import numpy as np

imagen = cv2.imread("imagenes/cuboRubik.png")

imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)  #Convierto la imagen de BGR a HSV
redBajo1 = np.array([0,100,20], np.uint8) 
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