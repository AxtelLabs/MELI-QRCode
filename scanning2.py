#import cv2
#from pyzbar.pyzbar import decode
#img = cv2.imread('qr_test.png')
#print(decode(img))


#import pyqrcode
#from qrtools import QR

#qr = qrtools.QR()
#qr = QR()
#qr.decode("qr_test.png")
#print(qr.data)


from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('qr_test.png')
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))