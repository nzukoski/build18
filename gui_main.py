#!/usr/bin/env python
#http://wrdeoftheday.com/?page_id=2

import sys
import cv2
import numpy as np
from PyQt4 import Qt, QtCore, QtGui
from gui import Ui_MainWindow
from roomal_control import CameraControl
import gui_logic as gl

def convertImg(frame):
    try:
        height, width = frame.shape[:2]
        img = QtGui.QImage(frame, width, height,
                            QtGui.QImage.Format_RGB888)
        img = QtGui.QPixmap.fromImage(img)
        return img
    except:
        print "failed to convert img"
        return None

class ControlMainWindow(QtGui.QMainWindow):
    #attributes:
    #   view: 0=standard, 1=motion, 2=heatmap
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.view = 0;
        self.ui.setupUi(self)
        
        #SIGNALS
        self.ui.actionStandard.triggered.connect(self.view_standard)
        self.ui.actionMotion.triggered.connect(self.view_motion)
        self.ui.actionHeat_Map.triggered.connect(self.view_heat_map)
        self.ui.actionReset_Heat_Map.triggered.connect(self.reset)
        self.ui.actionClear_Teams.triggered.connect(self.clear_teams)
        self.ui.actionAdd_Teams.triggered.connect(self.add_team)
        
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
        
    #SLOTS (functions to bind signals to)
    def view_standard(self):
        self.view = 0
     
    def view_motion(self):
        self.view = 1
        
    def view_heat_map(self):
        self.view = 2
        
    def play(self):
        if self.view == 0:
            img = CC.getLatestFrames()
        elif self.view == 1:
            img = CC.getThreshholds()
        else:
            img = CC.getLatestHeatmaps()
        if len(img > 0):
            self.ui.label1.setPixmap(img[0])   # QLabels hold images that we update
            QLabel1.setPixmap(img[1])
            QLabel1.setPixmap(img[2])
        else:
            print "No images to pull!"

    def clear_teams(self):
        gl.removeAll()

    def add_team(self, x1, x2, y1, y2, color = None, id = None):
        gl.addTeam(self, x1, x2, y1, y2, color, id)

    def remove_team(self, id):
        gl.removeTeam(id)

    def reset(self):
        gl.removeAll()
        CC = CameraControl()
        CC.connectToAllHosts()       
        CC.startMotionDetection()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    CC = CameraControl()
    CC.connectToAllHosts()       
    CC.startMotionDetection()
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())