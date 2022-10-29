#Actividad2: Realizar las 2 aplicaciones prácticos presentados en la clase 5:
# -Contando objetos
import cv2

imagen = cv2.imread("imagenes/monedas1.png")
imagenGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)    #La transformo a escala de grises
bordes = cv2.Canny(imagenGris,100,450)
bordes = cv2.dilate(bordes, None, iterations=1)
bordes = cv2.erode(bordes, None, iterations=0)
cv2.imshow("original",imagen)
cv2.imshow("Bordes detectados!",bordes)

contornos, jerarquia = cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)   #Tener en cuenta la jerarquía de contornos
#métodos de aproximación del contorno veremos:
#cv2.CHAIN_APPROX_NONE y cv2.CHAIN_APPROX_SIMPLE. En ambos casos se procederá a almacenar los puntos x e y,
#correspondientes a cada contorno encontrado, la diferencia está en la cantidad de puntos que se almacenan.
cv2.drawContours(imagen,contornos,-1, (0,0,255),2)#Se dibujan contornos de 2px de tamaño

texto = "Contornos encontrados: "+str(len(contornos))
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)
cv2.imshow("Objetos encontrados",imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()