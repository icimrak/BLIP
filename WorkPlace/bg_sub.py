import numpy as np
import matplotlib.pyplot as plt
import cv2 

print ("start")

# nFrames remembers the number of frames inside average
nFrames = 1
imgCnt = 50
# load new image 
pic = cv2.imread("src/frame_%d.jpg" %nFrames)
picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
# avg is our average picture
avg = np.float32(picGray)
#avg = picGray.copy()
nFrames += 1

# create avg image
while nFrames <= imgCnt:
    pic = cv2.imread("src/frame_%d.jpg" %nFrames)
    picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    nFrames += 1
    cv2.accumulateWeighted(picGray, avg, 1.0/nFrames)
    pass

cv2.imwrite("dest/background.jpg", avg)


#avg2 = cv2.imread("dest/background.jpg")
#avg2 = cv2.cvtColor(avg2, cv2.COLOR_BGR2GRAY)

nFrames = 1
while nFrames <= 1:
    pic = cv2.imread("src/frame_%d.jpg" %nFrames)
    picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("dest/orig.jpg", picGray)

    picGray = picGray - avg



    cv2.normalize(picGray,picGray,0,255,cv2.NORM_MINMAX)
    cv2.imwrite("dest/odcitane.jpg", picGray)

    print(picGray.dtype)
    picGray = picGray.astype(np.uint8)
#    cv2.imwrite("dest/4pretypovane.jpg", picGray)
#    print(picGray.dtype)
#    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(picGray)
#    print(minVal,maxVal)
#    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(picGray)
#    print(minVal,maxVal)
    #picGray2 = cv2.cvtColor(picGray, cv2.COLOR_BGR2GRAY)
#    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(picGray)
#    print(minVal,maxVal)
    ret, cbim = cv2.threshold(picGray,110,255,cv2.THRESH_BINARY)
    
    
    picGray = cv2.Laplacian(picGray, cv2.CV_64F)
    cv2.normalize(picGray,picGray,0,255,cv2.NORM_MINMAX)

    # cv2.imwrite("dest/frame_%d.jpg" %nFrames, cbim)

    cv2.imwrite("dest/laplacian.jpg", picGray)
    nFrames += 1
    pass

print ("end")
