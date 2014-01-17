import cv2
import numpy as np
import threading
from time import time, sleep

class CameraControl:

    #remoteHosts = ["http://192.168.2.4:8081/video1.mjpeg",
    #                "http://192.168.2.5:8081/video1.mjpeg", "http://192.168.2.6:8081/video1.mjpeg"]
    remoteHosts = ["testVideo.mov", "testVideo.mov", "testVideo.mov", "testVideo.mov"]
    numHosts = len(remoteHosts)
    captureSources = []
    frames = []
    prevGrayFrames = []
    thresholds = []
    heatmaps = []
    videoRecorders = []
    width = 640
    height = 480
    run = True # loop control
    record = False

    def connectToHost(self, hostName):
        captureSource = cv2.VideoCapture(hostName)
        self.captureSources.append(captureSource)

    def connectToAllHosts(self):
        # Connect to to remote hosts
        threads = []
        for host in self.remoteHosts:
            newThread = threading.Thread(target=self.connectToHost, args= (host,))
            threads.append(newThread)
            newThread.start()

        # Wait for the threads
        for t in threads:
            t.join()

        print "Connected to all hosts!"

    def getLatestHeatmaps(self):
        return self.heatmaps

    def getLatestFrames(self):
        return self.frames

    def getLatestThresholds(self):
        return self.thresholds

    # Initialize video recording
    def initVideoRecording(self):
        # Set up recording
        record = True # Set true to record
        fps = 15
        capSize = (height,width)
        fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
        for i in xrange(numHosts):
            testVideoWriter = cv2.VideoWriter()
            success = testVideoWriter.open('recorded_host' + str(i) + '.mov',fourcc, fps, capSize, True)
            self.videoRecorders.append(testVideoWriter)

    # Initialize motion detection
    def startMotionDetection(self):
        for i in xrange(self.numHosts):
            capture = self.captureSources[i]
            success, frame = capture.read()
            if (not success):
                print "capture failed on host " + str(i)  + " continuing..."
                continue

            # grab the width and height
            if (i == 0):
                width, height, _ = frame.shape

            self.prevGrayFrames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            self.heatmaps.append(np.zeros((width,height), np.uint8))
            self.frames.append(frame)
            self.thresholds.append(np.zeros((width,height), np.uint8))

        newThread = threading.Thread(target=self.mainLoop, args=())
        newThread.start()

    # the meat
    def mainLoop(self):
        # Main Loop
        self.run = True
        frameToShow = 0
        while (self.run):
            for i in xrange(self.numHosts):
                startTime = time()
                capture = self.captureSources[i]
                prevGray = np.float32(self.prevGrayFrames[i])

                success, frame = capture.read()
                if (not success):
                    print "capture failed on host " + str(i)  + " continuing..."
                    continue

                if (self.record):
                    videoRecorders[i].write(frame)

                self.frames[i] = frame
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                flow = cv2.calcOpticalFlowFarneback(prevGray, gray, 0.5, 1, 20, 3, 5, 1.2, 0)
                self.prevGrayFrames[i] = gray

                # building flow magnitude
                fx, fy = flow[:,:,0], flow[:,:,1]
                v = np.sqrt(fx*fx+fy*fy)
                normalized = np.uint8(np.minimum(v*4, 255))
                retval, threshold = cv2.threshold(normalized, 20, 1, cv2.THRESH_BINARY)
                self.thresholds[i] = threshold
                self.heatmaps[i] += threshold

        for c in self.captureSources:
            c.release()

cc = CameraControl()
cc.connectToAllHosts()
cc.startMotionDetection()
frameToShow = 0

while (True):
    k = cv2.waitKey(100)

    if k == 49: # 1
        frameToShow = 0
    if k == 50: # 2
        frameToShow = 1
    if k == 51: # 3
        frameToShow = 2

    if k == 27: # esc
        cc.run = False
        break

    for i in xrange(cc.numHosts):
        if (frameToShow == 0):
            cv2.imshow("host_" + str(i), cc.getLatestFrames()[i])
        elif (frameToShow == 1):
            cv2.imshow("host_" + str(i), cc.getLatestHeatmaps()[i])
        elif (frameToShow == 2):
            cv2.imshow("host_" + str(i), cc.getLatestThresholds()[i] * 255)


            
    



