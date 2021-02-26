import cv2
import numpy as np

from imutils.video import  FPS, WebcamVideoStream
import time

#video = cv2.VideoCapture(0)
video = WebcamVideoStream(src=0).start()
time.sleep(2.0)

fps = FPS().start()

while True:

    
    frame = video.read()

    #if not ret:
    #    break
    
    cv2.imshow("frame", frame)

    fps.update()

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

video.stop()#release()
fps.stop()

print("FPS: ", fps.fps(), "time elapsed: ", fps.elapsed())