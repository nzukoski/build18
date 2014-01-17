import cv2
import numpy as np
import threading
from time import time, sleep
startTime = time()

#remoteHosts = ["http://192.168.2.4:8081/video1.mjpeg",
#                "http://192.168.2.5:8081/video1.mjpeg", "http://192.168.2.6:8081/video1.mjpeg"]
remoteHosts = ["testVideo.mov", "testVideo.mov", "testVideo.mov", "testVideo.mov"]
numHosts = len(remoteHosts)
captureSources = []
prevGrayFrames = []
heatmaps = []
width = 640
height = 480

def connectToHost(hostName):
    captureSource = cv2.VideoCapture(host)
    captureSources.append(captureSource)

# Connect to to remote hosts
threads = []
for host in remoteHosts:
    newThread = threading.Thread(target=connectToHost, args= (host,))
    newThread.daemon = True
    threads.append(newThread)
    newThread.start()

# Wait for the threads
for t in threads:
    t.join()

print "Connected to all hosts!"

# Set up recording
record = False # Set true to record
fps = 15
capSize = (height,width)
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
videoRecorders = []
for i in xrange(numHosts):
    testVideoWriter = cv2.VideoWriter()
    success = testVideoWriter.open('recorded_host' + str(i) + '.mov',fourcc, fps, capSize, True)
    videoRecorders.append(testVideoWriter)

# Initialize motion detection
for i in xrange(numHosts):
    capture = captureSources[i]
    success, frame = capture.read()
    if (not success):
        print "capture failed on host " + str(i)  + " continuing..."
        continue

    # grab the width and height
    if (i == 0):
        width, height, _ = frame.shape

    prevGrayFrames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    heatmaps.append(np.zeros((width,height), np.uint8))

# Timing stuff
totalTime = 0
numFrames = 0

# Main Loop
run = True
frameToShow = 0
while (run):
    for i in xrange(numHosts):
        startTime = time()
        capture = captureSources[i]
        prevGray = np.float32(prevGrayFrames[i])

        success, frame = capture.read()
        if (not success):
            print "capture failed on host " + str(i)  + " continuing..."
            print "average time: " + str( totalTime / numFrames)
            cv2.waitKey()
            continue

        if (record):
            videoRecorders[i].write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prevGray, gray, 0.5, 1, 20, 3, 5, 1.2, 0)
        prevGrayFrames[i] = gray

        # building flow magnitude
        fx, fy = flow[:,:,0], flow[:,:,1]
        v = np.sqrt(fx*fx+fy*fy)
        normalized = np.uint8(np.minimum(v*4, 255))
        retval, threshold = cv2.threshold(normalized, 20, 1, cv2.THRESH_BINARY)
        heatmaps[i] += threshold

        if (frameToShow == 0):
            cv2.imshow("host_" + str(i), frame)
        elif (frameToShow == 1):
            cv2.imshow("host_" + str(i), heatmaps[i])
        elif (frameToShow == 2):
            cv2.imshow("host_" + str(i), threshold * 255)

        totalTime += (time() - startTime)
        numFrames += 1

    k = cv2.waitKey(15)

    if k == 49: # 1
        frameToShow = 0
    if k == 50: # 2
        frameToShow = 1
    if k == 51: # 3
        frameToShow = 2

    if k == 27: # esc
        run = False

# cleanup
if (record):
    for recorder in videoRecorders:
        recorder.release()

for c in captureSources:
    c.release()
cv2.destroyAllWindows()

            
    



