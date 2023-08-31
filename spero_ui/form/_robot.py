# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1234, 887)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_auto = QtWidgets.QPushButton(self.centralwidget)
        self.pb_auto.setGeometry(QtCore.QRect(390, 230, 141, 51))
        self.pb_auto.setObjectName("pb_auto")
        self.pb_manual = QtWidgets.QPushButton(self.centralwidget)
        self.pb_manual.setGeometry(QtCore.QRect(220, 230, 141, 51))
        self.pb_manual.setObjectName("pb_manual")
        self.pb_uvon = QtWidgets.QPushButton(self.centralwidget)
        self.pb_uvon.setGeometry(QtCore.QRect(220, 150, 141, 51))
        self.pb_uvon.setObjectName("pb_uvon")
        self.pb_uvoff = QtWidgets.QPushButton(self.centralwidget)
        self.pb_uvoff.setGeometry(QtCore.QRect(390, 150, 141, 51))
        self.pb_uvoff.setObjectName("pb_uvoff")
        self.pb_roboton = QtWidgets.QPushButton(self.centralwidget)
        self.pb_roboton.setGeometry(QtCore.QRect(220, 80, 141, 51))
        self.pb_roboton.setObjectName("pb_roboton")
        self.pb_robotoff = QtWidgets.QPushButton(self.centralwidget)
        self.pb_robotoff.setGeometry(QtCore.QRect(390, 80, 141, 51))
        self.pb_robotoff.setObjectName("pb_robotoff")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(580, 50, 621, 561))
        self.mdiArea.setObjectName("mdiArea")
        self.pb_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.pb_shutdown.setGeometry(QtCore.QRect(304, 312, 151, 61))
        self.pb_shutdown.setObjectName("pb_shutdown")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1234, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionRobot_Properties = QtWidgets.QAction(MainWindow)
        self.actionRobot_Properties.setObjectName("actionRobot_Properties")
        self.actionRobot_Status = QtWidgets.QAction(MainWindow)
        self.actionRobot_Status.setObjectName("actionRobot_Status")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionDisconnect)
        self.menuFile.addSeparator()
        self.menuMain.addAction(self.actionRobot_Status)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_auto.setText(_translate("MainWindow", "Autonomous"))
        self.pb_manual.setText(_translate("MainWindow", "Manual"))
        self.pb_uvon.setText(_translate("MainWindow", "UV ON"))
        self.pb_uvoff.setText(_translate("MainWindow", "UV OFF"))
        self.pb_roboton.setText(_translate("MainWindow", "Robot ON"))
        self.pb_robotoff.setText(_translate("MainWindow", "Robot OFF"))
        self.pb_shutdown.setText(_translate("MainWindow", "Shut Down Robot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionRobot_Properties.setText(_translate("MainWindow", "Robot Properties"))
        self.actionRobot_Status.setText(_translate("MainWindow", "Robot Status (F5)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
