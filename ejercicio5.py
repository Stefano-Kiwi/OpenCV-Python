#Actividad4: Escribir un script Python que permita conectarse a una WEB CAM
#o cámara USB conectada al equipo y reproduzca video (video straming) en una
#ventana con la descripción “En vivo”.
import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('En vivo', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

video.release()
cv2.destroyAllWindows()