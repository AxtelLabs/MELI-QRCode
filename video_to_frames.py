#video_to_frames.py
# convert video into frames

import cv2

vidcap = cv2.VideoCapture('/Users/israel/Downloads/WIN_20210318_07_06_59_Pro.mp4')

success, image = vidcap.read()

count = 0

while success:

  cv2.imwrite("/Users/israel/Downloads/frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1