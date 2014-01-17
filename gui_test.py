import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from gui import Ui_MainWindow

class Gui(QtGui.QMainWindow):
    def __init(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def play(self):
        

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()