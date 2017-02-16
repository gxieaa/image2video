import cv2
import os
import re

dir_path = '/home/yy/image/pcl_image_all/'
images = []
for i in range(3,200):
    img_name = str(i).rjust(6, '0')
    img_name = dir_path + img_name + '.png' 
    images.append(img_name)

frame = cv2.imread(images[0])
#cv2.imshow('first frame', frame)
#cv2.waitKey(0)
height, width, channels = frame.shape
#print height
#print width
#print channels
fourcc = cv2.cv.CV_FOURCC(*'mp4v')
out = cv2.VideoWriter('test.avi', fourcc, 5.0, (width, height))
for img in images:
    frame = cv2.imread(img)
    out.write(frame)
    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
out.release()
cv2.destroyAllWindows()

