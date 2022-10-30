#Actividad3: Realizar un script que permita leer/cargar la imagen siguiente:
# Agregar contorno de color verde a ambas señales viales.
# Agregar texto de color verde con la leyenda “Alerta al conductor”.
import cv2

imagen = cv2.imread("imagenes/ruta.jpg")
imagenGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)   
bordes = cv2.Canny(imagenGris,400,895)          #Aproximación más próxima a lo que deseo obtener de la imagen (las señales)
bordes = cv2.dilate(bordes, None, iterations=1)
bordes = cv2.erode(bordes, None, iterations=1)
cv2.imshow("original",imagen)
cv2.imshow("Bordes detectados!",bordes)

contornos, jerarquia = cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)   

cv2.drawContours(imagen,contornos,-1, (0,255,0),2)

texto = "Contornos encontrados: "+str(len(contornos))
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 1)
cv2.putText(imagen, "Alerta al conductor", (60,215), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 1)
cv2.imshow("Objetos encontrados",imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()