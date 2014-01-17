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
    newWidth = 427
    newHeight = 320
    scaledImage = cv2.resize(frame,(newWidth,newHeight))
    # try:
    height, width, bytesPerComponent= scaledImage.shape
    bytesPerLine = bytesPerComponent*width
    img = QtGui.QImage(scaledImage.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    img = QtGui.QPixmap.fromImage(img)
    return img
    # except:
    #     print "failed to convert img"
    #     return None

class ControlMainWindow(QtGui.QMainWindow):
    #used to limit how often its updated
    currentFrame = 0
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
        self.currentFrame += 1
        rawHeatmap = CC.getLatestRawHeatmaps()
        if self.view == 0:
            img = CC.getLatestFrames()
        elif self.view == 1:
            img = CC.getLatestThresholds()
        else:
            img = CC.getLatestHeatmaps()
        if len(img) > 0:
            self.ui.label1.setPixmap(convertImg(img[0]))
            self.ui.label1.mousePressEvent = self.getPos
        if len(img) > 1:
            self.ui.label2.setPixmap(convertImg(img[1]))
            self.ui.label2.mousePressEvent = self.getPos
        if len(img) > 2:
            self.ui.label3.setPixmap(convertImg(img[2]))   # QLabels hold images that we update
            self.ui.label3.mousePressEvent = self.getPos
        if len(img) > 3:
            self.ui.label4.setPixmap(convertImg(img[3]))
            self.ui.label4.mousePressEvent = self.getPos

            if ((self.currentFrame % 10) == 0):
                for t in gl.teams:
                    t.update(rawHeatmap[0])   
                gl.sortTeams()                      # sort by intensity
                self.ui.tableWidget.clearContents() # clear widget
                for i in xrange(len(gl.teams)):    # display new order in widget
                    item = QtGui.QTableWidgetItem(gl.teams[i].id) # widget item associated with display
                    intensityString = '%.2f' % gl.teams[i].intensity
                    intensity = QtGui.QTableWidgetItem(intensityString)
                    self.ui.tableWidget.setItem(i, 0, item)
                    self.ui.tableWidget.setItem(i, 1, intensity)

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

        if (ok and len(ans) > 0):
            insert_team(ans)

    def insert_team(self, ans):
        # OK was clicked with data
        info = ans.split(":")
        label = int(info[0])
        name = info[1]
        x1,y1 = info[2].split(",")
        x2,y2 = info[3].split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
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
    # for i in xrange(5):
    #    mySW.insert_team("0:hi" + str(i) + ":129,67:272,157")
    mySW.insert_team("0:team1" + ":0,0:100,100")
    mySW.insert_team("0:team2" + ":100,100:200,200")
    mySW.insert_team("0:team3" + ":150,100:150,250")
    mySW.insert_team("0:team4" + ":200,100:300,300")
    mySW.show()
    sys.exit(app.exec_())

