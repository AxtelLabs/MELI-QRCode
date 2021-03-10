import cv2
import numpy as np
from pyzbar import pyzbar
from imutils.video import FPS, WebcamVideoStream
import time
import datetime
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

video = WebcamVideoStream(src=0).start()
time.sleep(2.0)

# Escribir en cvs QRs detectados
csv = open(args["output"], "w")
found = set()

fps = FPS().start()

while True:

    frame = video.read()

    cv2.imshow("frame", frame)

    # Encontrar los barcodes en el frame y decodificar cada uno
    barcodes = pyzbar.decode(frame)

    # loop over the detected barcodes
    for barcode in barcodes:
        # Bounding box alrededor del barcode
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #conversión a string
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #Se escribe CSV en texto con timestamp
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(), barcodeData))
            csv.flush()
            found.add(barcodeData)

    fps.update()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.stop()
fps.stop()

print("FPS: ", fps.fps(), "time elapsed: ", fps.elapsed())