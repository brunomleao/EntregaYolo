import cv2 as cv;
from ultralytics import YOLO;

cam = cv.VideoCapture(0)
model = YOLO("./best.pt")

while True:
    ret, frame = cam.read()
    result = model.predict(frame, conf=0.6) 
    cv.imshow("Resultados", result[0].plot())
    if cv.waitKey(1) == ord('q'):
        break 
cam.release()
cv.destroyAllWindows()