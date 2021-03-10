import cv2 
import os

# define the name of the directory to be created
# for storing frames
tmp_frames_folder = "/tmp_frames"

box_img = cv2.imread("qr_box.png")
box_img = cv2.resize(box_img, (0,0), fx=0.5, fy=0.5)
print("[INFO]: the qr box image is size: h,w: ", \
    box_img.shape[0],box_img.shape[1])
    
conveyor_img = cv2.imread("MEASUREMENT.jpg")

y_offset = 230

total_x_dist = conveyor_img.shape[1]-box_img.shape[1]
print(total_x_dist)
for x_offset in range(0,total_x_dist,20):
#x_offset = 0
    #try:
    conveyor_img[y_offset:y_offset+box_img.shape[0], \
        x_offset:x_offset+box_img.shape[1]] = box_img

    cv2.imshow("large_img", conveyor_img)
    cv2.waitKey(1)
    #except:
    #    break
    conveyor_img = cv2.imread("MEASUREMENT.jpg")
"""
try:
    os.mkdir(tmp_frames_folder)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)"""