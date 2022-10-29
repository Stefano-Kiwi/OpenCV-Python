
#Actividad1: Realizar un script que permita leer/cargar la imagen del vehículo y
#luego se recorte la misma para obtener la zona de la chapa patente. Guardar
#esta nueva imagen recortada como patente.png

import cv2

imagen = cv2.imread("imagenes/auto-con-pantente-google.png")

#La recorto
imagenOut = imagen[350:450,500:735]
cv2.imwrite("imagenes/patente.png",imagenOut)
cv2.imshow("imagen de entrada",imagen)
cv2.imshow("imagen de salida",imagenOut)
cv2.waitKey(0)
cv2.destroyAllWindows()