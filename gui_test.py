import sys
import cv2
import numpy as np
from PyQt4 import Qt, QtCore, QtGui
from gui import Ui_MainWindow

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
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())