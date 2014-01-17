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
        img = QtGui.QImage(frame, width, height, QtGui.QImage.Format_RGB888)
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
            img = CC.getLatestThresholds()
        else:
            img = CC.getLatestHeatmaps()
        if len(img) > 0:
            self.ui.label1.setPixmap(convertImg(img[0]))
            self.ui.label1.mousePressEvent = self.getPos

            self.ui.label2.setPixmap(convertImg(img[1]))
            self.ui.label2.mousePressEvent = self.getPos

            self.ui.label3.setPixmap(convertImg(img[2]))   # QLabels hold images that we update
            self.ui.label3.mousePressEvent = self.getPos

            for t in gl.teams:
                t.update(img[t.label])   #<---FIX: NEED TO CONVERT TO GRAYSCALE FIRST!!! QPixMap ->grayscale  ---->     # pass in the correct image according to previous given label indentifier
            gl.sortTeams()                      # sort by intensity
            self.ui.tableWidget.clearContents() # clear widget
            for i in xrange(len(gl.teams)):    # display new order in widget
                item = QtGui.QTableWidgetItem(gl.teams[i].id) # widget item associated with display
                self.ui.tableWidget.setItem(i, 0, item)
        else:
            print "No images to pull!"

    def getPos(self , event):
        x = event.pos().x()
        y = event.pos().y() 
        print "x: ", x, " y:", y

    def clear_teams(self):
        gl.removeAll()

    def add_team(self):
        # d = QtGui.QInputDialog(self)
        # d.show()

        # Get user input: we figure out x,y coords by observing position of mouse click events over the images.
        # label is which box (camera display) its in 1,2, or 3 starting from top-left
        ans, ok = QtGui.QInputDialog.getText(self, "Team Info", "Enter exactly --> label:team_name:x1,y1:x2,y2")

        # OK was clicked with data
        if ok and len(ans) > 0:
            info = ans.split(":")
            label,_ = info[0].toInt()
            name = info[1]
            x1,y1 = info[2].split(",")
            x2,y2 = info[3].split(",")
            x1,_ = x1.toInt()
            x2,_ = x2.toInt()
            y1,_ = y1.toInt()
            y2,_ = y2.toInt()
            gl.addTeam(x1, x2, y1, y2, id = name, label = label )

    def remove_team(self):
        ans, ok = QtGui.QInputDialog.getText(self, "Remove Team", "Enter the team's ID'")
        if ok and len(ans) > 0:
            gl.removeTeam(ans)

    def reset(self):
        self.clear_teams()
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