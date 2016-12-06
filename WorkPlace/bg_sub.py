import numpy as np
import matplotlib.pyplot as plt
import cv2 

print ("start")

# nFrames remembers the number of frames inside average
nFrames = 1
imgCnt = 120
# load new image 
pic = cv2.imread("src/frame_%d.jpg" %nFrames)
picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
# avg is our average picture
avg = np.float32(picGray)
nFrames += 1

# create avg image
while nFrames <= imgCnt:
	pic = cv2.imread("src/frame_%d.jpg" %nFrames)
	picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
	nFrames += 1
	cv2.accumulateWeighted(picGray, avg, 1.0/nFrames)
	pass

cv2.imwrite("dest/background.jpg", avg)

nFrames = 1
while nFrames <= 1:
	pic = cv2.imread("src/frame_%d.jpg" %nFrames)
	picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
	picGray = picGray - avg	
	# picGray = cv2.cvtColor(picGray, cv2.COLOR_BGR2GRAY)

	# cbim = cv2.adaptiveThreshold(picGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	# cv2.imwrite("dest/frame_%d.jpg" %nFrames, cbim)

	cv2.imwrite("dest/frame_%d.jpg" %nFrames, picGray)
	nFrames += 1
	pass

print ("end")