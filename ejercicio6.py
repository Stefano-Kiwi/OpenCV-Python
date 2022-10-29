
#Actividad5: Descargar un video (en formato .mp4 o .avi) de un repositorio libre
#y escribir un script Python que lo reproduzca mostrando sus propiedades
#básicas:
#Ejemplo: Frame Por Second

import cv2
from cv2 import CAP_PROP_FPS
import time

prev_frame_time = 0
new_frame_time = 0

cap = cv2.VideoCapture("video/videoGranja.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
while (cap.isOpened()):
    ret, frame = cap.read()
    new_frame_time = time.time()

    if ret==True:
        #Display the resulting frame
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        textoAMostrar = ("Fps: {0}".format(fps))
        cv2.putText(frame, textoAMostrar, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.imshow("Reproducir video", frame)
        if cv2.waitKey(30) == ord("s"):
            break
        
    else: break
    
cap.release()
cv2.destroyAllWindows()