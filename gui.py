#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jan 17 01:13:01 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(380, 260, 351, 221))
        self.tableView.setObjectName(_fromUtf8("tableView"))

        self.label1 = QtGui.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(10, 20, 351, 221))
        self.label1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label1.setFrameShadow(QtGui.QFrame.Raised)
        self.label1.setObjectName(_fromUtf8("label1"))

        self.label2 = QtGui.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(380, 20, 351, 221))
        self.label2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label2.setFrameShadow(QtGui.QFrame.Raised)
        self.label2.setObjectName(_fromUtf8("label2"))

        self.label3 = QtGui.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(10, 260, 351, 221))
        self.label3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label3.setFrameShadow(QtGui.QFrame.Raised)
        self.label3.setObjectName(_fromUtf8("label3"))

        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuRoomal = QtGui.QMenu(self.menuBar)
        self.menuRoomal.setObjectName(_fromUtf8("menuRoomal"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.actionStandard = QtGui.QAction(MainWindow)
        self.actionStandard.setObjectName(_fromUtf8("actionStandard"))
        self.actionMotion = QtGui.QAction(MainWindow)
        self.actionMotion.setObjectName(_fromUtf8("actionMotion"))
        self.actionHeat_Map = QtGui.QAction(MainWindow)
        self.actionHeat_Map.setObjectName(_fromUtf8("actionHeat_Map"))
        self.actionReset_Heat_Map = QtGui.QAction(MainWindow)
        self.actionReset_Heat_Map.setObjectName(_fromUtf8("actionReset_Heat_Map"))
        self.actionClear_Teams = QtGui.QAction(MainWindow)
        self.actionClear_Teams.setObjectName(_fromUtf8("actionClear_Teams"))
        self.actionAdd_Teams = QtGui.QAction(MainWindow)
        self.actionAdd_Teams.setObjectName(_fromUtf8("actionAdd_Teams"))
        self.menuRoomal.addAction(self.actionStandard)
        self.menuRoomal.addAction(self.actionMotion)
        self.menuRoomal.addAction(self.actionHeat_Map)
        self.menuFile.addAction(self.actionReset_Heat_Map)
        self.menuFile.addAction(self.actionClear_Teams)
        self.menuFile.addAction(self.actionAdd_Teams)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuRoomal.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuRoomal.setTitle(_translate("MainWindow", "View", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionFile.setText(_translate("MainWindow", "File", None))
        self.actionStandard.setText(_translate("MainWindow", "Standard", None))
        self.actionMotion.setText(_translate("MainWindow", "Motion", None))
        self.actionHeat_Map.setText(_translate("MainWindow", "Heat Map", None))
        self.actionReset_Heat_Map.setText(_translate("MainWindow", "Reset Heat Map", None))
        self.actionClear_Teams.setText(_translate("MainWindow", "Clear Teams", None))
        self.actionAdd_Teams.setText(_translate("MainWindow", "Add Team", None))

