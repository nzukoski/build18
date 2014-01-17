import cv2
import numpy as np
import threading
import json
from time import time, sleep

class ColorMap:

    jet_mapping = np.uint8(np.array([(0, 0, 127), (0, 0, 127), (0, 0, 131), (0, 0, 135), (0, 0, 139), (0, 0, 143), (0, 0, 147), (0, 0, 151), (0, 0, 155), (0, 0, 159), (0, 0, 163), (0, 0, 167), (0, 0, 171), (0, 0, 175), (0, 0, 179), (0, 0, 183), (0, 0, 187), (0, 0, 191), (0, 0, 195), (0, 0, 199), (0, 0, 203), (0, 0, 207), (0, 0, 211), (0, 0, 215), (0, 0, 219), (0, 0, 223), (0, 0, 227), (0, 0, 231), (0, 0, 235), (0, 0, 239), (0, 0, 243), (0, 0, 247), (0, 0, 251), (0, 0, 255), (0, 4, 255), (0, 8, 255), (0, 12, 255), (0, 16, 255), (0, 20, 255), (0, 24, 255), (0, 28, 255), (0, 32, 255), (0, 36, 255), (0, 40, 255), (0, 44, 255), (0, 48, 255), (0, 52, 255), (0, 56, 255), (0, 60, 255), (0, 64, 255), (0, 68, 255), (0, 72, 255), (0, 76, 255), (0, 80, 255), (0, 84, 255), (0, 88, 255), (0, 92, 255), (0, 96, 255), (0, 100, 255), (0, 104, 255), (0, 108, 255), (0, 112, 255), (0, 116, 255), (0, 120, 255), (0, 124, 255), (0, 128, 255), (0, 132, 255), (0, 136, 255), (0, 140, 255), (0, 144, 255), (0, 148, 255), (0, 152, 255), (0, 156, 255), (0, 160, 255), (0, 164, 255), (0, 168, 255), (0, 172, 255), (0, 176, 255), (0, 180, 255), (0, 184, 255), (0, 188, 255), (0, 192, 255), (0, 196, 255), (0, 200, 255), (0, 204, 255), (0, 208, 255), (0, 212, 255), (0, 216, 255), (0, 220, 255), (0, 224, 255), (0, 228, 255), (0, 232, 255), (0, 236, 255), (0, 240, 255), (0, 244, 255), (0, 248, 255), (0, 252, 255), (1, 255, 253), (5, 255, 249), (9, 255, 245), (13, 255, 241), (17, 255, 237), (21, 255, 233), (25, 255, 229), (29, 255, 225), (33, 255, 221), (37, 255, 217), (41, 255, 213), (45, 255, 209), (49, 255, 205), (53, 255, 201), (57, 255, 197), (61, 255, 193), (65, 255, 189), (69, 255, 185), (73, 255, 181), (77, 255, 177), (81, 255, 173), (85, 255, 169), (89, 255, 165), (93, 255, 161), (97, 255, 157), (101, 255, 153), (105, 255, 149), (109, 255, 145), (113, 255, 141), (117, 255, 137), (121, 255, 133), (125, 255, 129), (129, 255, 125), (133, 255, 121), (137, 255, 117), (141, 255, 113), (145, 255, 109), (149, 255, 105), (153, 255, 101), (157, 255, 97), (161, 255, 93), (165, 255, 89), (169, 255, 85), (173, 255, 81), (177, 255, 77), (181, 255, 73), (185, 255, 69), (189, 255, 65), (193, 255, 61), (197, 255, 57), (201, 255, 53), (205, 255, 49), (209, 255, 45), (213, 255, 41), (217, 255, 37), (221, 255, 33), (225, 255, 29), (229, 255, 25), (233, 255, 21), (237, 255, 17), (241, 255, 13), (245, 255, 9), (249, 255, 5), (253, 255, 1), (255, 252, 0), (255, 248, 0), (255, 244, 0), (255, 240, 0), (255, 236, 0), (255, 232, 0), (255, 228, 0), (255, 224, 0), (255, 220, 0), (255, 216, 0), (255, 212, 0), (255, 208, 0), (255, 204, 0), (255, 200, 0), (255, 196, 0), (255, 192, 0), (255, 188, 0), (255, 184, 0), (255, 180, 0), (255, 176, 0), (255, 172, 0), (255, 168, 0), (255, 164, 0), (255, 160, 0), (255, 156, 0), (255, 152, 0), (255, 148, 0), (255, 144, 0), (255, 140, 0), (255, 136, 0), (255, 132, 0), (255, 128, 0), (255, 124, 0), (255, 120, 0), (255, 116, 0), (255, 112, 0), (255, 108, 0), (255, 104, 0), (255, 100, 0), (255, 96, 0), (255, 92, 0), (255, 88, 0), (255, 84, 0), (255, 80, 0), (255, 76, 0), (255, 72, 0), (255, 68, 0), (255, 64, 0), (255, 60, 0), (255, 56, 0), (255, 52, 0), (255, 48, 0), (255, 44, 0), (255, 40, 0), (255, 36, 0), (255, 32, 0), (255, 28, 0), (255, 24, 0), (255, 20, 0), (255, 16, 0), (255, 12, 0), (255, 8, 0), (255, 4, 0), (255, 0, 0), (251, 0, 0), (247, 0, 0), (243, 0, 0), (239, 0, 0), (235, 0, 0), (231, 0, 0), (227, 0, 0), (223, 0, 0), (219, 0, 0), (215, 0, 0), (211, 0, 0), (207, 0, 0), (203, 0, 0), (199, 0, 0), (195, 0, 0), (191, 0, 0), (187, 0, 0), (183, 0, 0), (179, 0, 0), (175, 0, 0), (171, 0, 0), (167, 0, 0), (163, 0, 0), (159, 0, 0), (155, 0, 0), (151, 0, 0), (147, 0, 0), (143, 0, 0), (139, 0, 0), (135, 0, 0), (131, 0, 0)]))
    jet_mapping = jet_mapping[::-1]
    jet_red = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121, 125, 129, 133, 137, 141, 145, 149, 153, 157, 161, 165, 169, 173, 177, 181, 185, 189, 193, 197, 201, 205, 209, 213, 217, 221, 225, 229, 233, 237, 241, 245, 249, 253, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 251, 247, 243, 239, 235, 231, 227, 223, 219, 215, 211, 207, 203, 199, 195, 191, 187, 183, 179, 175, 171, 167, 163, 159, 155, 151, 147, 143, 139, 135, 131])
    jet_green = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236, 240, 244, 248, 252, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 248, 244, 240, 236, 232, 228, 224, 220, 216, 212, 208, 204, 200, 196, 192, 188, 184, 180, 176, 172, 168, 164, 160, 156, 152, 148, 144, 140, 136, 132, 128, 124, 120, 116, 112, 108, 104, 100, 96, 92, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    jet_blue = np.array([127, 131, 135, 139, 143, 147, 151, 155, 159, 163, 167, 171, 175, 179, 183, 187, 191, 195, 199, 203, 207, 211, 215, 219, 223, 227, 231, 235, 239, 243, 247, 251, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 253, 249, 245, 241, 237, 233, 229, 225, 221, 217, 213, 209, 205, 201, 197, 193, 189, 185, 181, 177, 173, 169, 165, 161, 157, 153, 149, 145, 141, 137, 133, 129, 125, 121, 117, 113, 109, 105, 101, 97, 93, 89, 85, 81, 77, 73, 69, 65, 61, 57, 53, 49, 45, 41, 37, 33, 29, 25, 21, 17, 13, 9, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    def convertToJet(self, image):
        output = np.array(map(self.lookup, image))
        return output

    def lookup(self, num):
        return self.jet_mapping[num]

class CameraControl:

    #remoteHosts = [ "http://192.168.2.131:8081/video1.mjpeg",
    #                "http://192.168.2.136:8081/video1.mjpeg"]# "http://192.168.2.6:8081/video1.mjpeg"]
    remoteHosts = ["testVideo.mov", "testVideo.mov", "testVideo.mov"]
    numHosts = len(remoteHosts)
    captureSources = []
    frames = []
    prevGrayFrames = []
    thresholds = []
    pretty_heatmaps = []
    raw_heatmaps = []
    videoRecorders = []
    width = 640
    height = 480
    run = True # loop control
    record = False
    colorMapper = ColorMap()
    curFrames = [0,0,0,0]

    def convertToPrettyHeatMap(self, raw_heatmap):
        max = np.max(raw_heatmap)
        normalized = np.uint8(raw_heatmap*(np.floor(255/max)))
        colorized =  self.colorMapper.convertToJet(normalized)
        return cv2.cvtColor(colorized, cv2.cv.CV_BGR2RGB)

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
        return self.pretty_heatmaps

    def getLatestFrames(self):
        return self.frames

    def getLatestThresholds(self):
        return self.thresholds

    def getLatestRawHeatmaps(self):
        return self.raw_heatmaps

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
            self.raw_heatmaps.append(np.zeros((width,height), np.uint32))
            self.pretty_heatmaps.append(self.colorMapper.convertToJet(np.zeros((width,height), np.uint8)))
            self.frames.append(frame)
            self.thresholds.append(frame)

        #readBackups()
        for i in xrange(self.numHosts):
            newThread = threading.Thread(target=self.mainLoopForCam, args=(i,))
            newThread.start()

    # the meat
    def mainLoopForCam(self, camNumber):
        # Main Loop
        self.run = True
        frameToShow = 0
        while (self.run):
            self.curFrames[camNumber] += 1
            startTime = time()
            capture = self.captureSources[camNumber]
            prevGray = np.float32(self.prevGrayFrames[camNumber])

            success, frame = capture.read()
            if (not success):
                print "capture failed on host " + str(camNumber)  + " continuing..."
                continue

            if (self.record):
                videoRecorders[camNumber].write(frame)

            self.frames[camNumber] = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prevGray, gray, 0.5, 1, 20, 3, 5, 1.2, 0)
            self.prevGrayFrames[camNumber] = gray

            # building flow magnitude
            fx, fy = flow[:,:,0], flow[:,:,1]
            v = np.sqrt(fx*fx+fy*fy)
            normalized = np.uint8(np.minimum(v*4, 255))
            retval, threshold = cv2.threshold(normalized, 20, 1, cv2.THRESH_BINARY)
            self.thresholds[camNumber] = np.dstack((threshold, threshold, threshold))
            self.raw_heatmaps[camNumber] += threshold
            self.pretty_heatmaps[camNumber] = self.convertToPrettyHeatMap(self.raw_heatmaps[camNumber])

            if (self.curFrames[camNumber] % 20) == 0:
                np.save("heatmap_backup_" + str(camNumber), self.raw_heatmaps[camNumber].data)
    
    def shutdown(self):
        self.run = False
        for c in self.captureSources:
            c.release()

    def readBackups(self):
        for i in xrange(self.numHosts):
            self.raw_heatmaps[i].data = np.load("heatmap_backup_" + str(i) + ".npy")

if __name__ == "__main__":
    cc = CameraControl()
    cc.connectToAllHosts()
    cc.startMotionDetection()
    cc.readBackups()
    frameToShow = 0
    colorMapper = ColorMap()
    while (True):
        k = cv2.waitKey(100)

        if k == 49: # 1
            frameToShow = 0
        if k == 50: # 2
            frameToShow = 1
        if k == 51: # 3
            frameToShow = 2

        if k == 27: # esc
            cc.shutdown()
            break

        for i in xrange(cc.numHosts):
            if (frameToShow == 0):
                cv2.imshow("host_" + str(i), cc.getLatestFrames()[i])
            elif (frameToShow == 1):
                cv2.imshow("host_" + str(i), cc.getLatestHeatmaps()[i])
            elif (frameToShow == 2):
                cv2.imshow("host_" + str(i), cc.getLatestThresholds()[i] * 255)


            
    



