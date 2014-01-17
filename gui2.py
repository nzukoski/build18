import cv2
import numpy as np

class gui():
    def __init__(self, parent=None):
        self.nImgs  = 4
        self.winName    = "Roomal"
        self.winWidth   = 600
        self.winHeight  = 600
        self.window = cv2.namedWindow("Roomal")
        cv2.ResizeWindow(self.winName, self.winWidth, self.winHeight)
    
#   drawRect: creates a rectangle on this gui's window
#   x1, x2, y1, y2: coordinates
#   color: array (size 4) with rgba color values for rectangle
    def drawRect(x1, x2, y1, y2, color)
    
def main():
    app = gui()
    