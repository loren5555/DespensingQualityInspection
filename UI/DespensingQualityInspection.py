# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DespensingQualityInspection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1323, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.adddirbutton = QtWidgets.QPushButton(self.centralwidget)
        self.adddirbutton.setObjectName("adddirbutton")
        self.gridLayout.addWidget(self.adddirbutton, 1, 3, 1, 1)
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setObjectName("Cancel")
        self.gridLayout.addWidget(self.Cancel, 2, 3, 1, 1)
        self.addimgbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addimgbutton.setObjectName("addimgbutton")
        self.gridLayout.addWidget(self.addimgbutton, 0, 3, 1, 1)
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setObjectName("label_output")
        self.gridLayout.addWidget(self.label_output, 1, 0, 1, 1)
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setObjectName("label_pic")
        self.gridLayout.addWidget(self.label_pic, 0, 0, 1, 1)
        self.label_wait = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_wait.setFont(font)
        self.label_wait.setText("")
        self.label_wait.setObjectName("label_wait")
        self.gridLayout.addWidget(self.label_wait, 2, 0, 1, 1)
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setObjectName("OK")
        self.gridLayout.addWidget(self.OK, 2, 2, 1, 1)
        self.outputdir = QtWidgets.QLineEdit(self.centralwidget)
        self.outputdir.setText("")
        self.outputdir.setObjectName("outputdir")
        self.gridLayout.addWidget(self.outputdir, 1, 1, 1, 2)
        self.picdir = QtWidgets.QLineEdit(self.centralwidget)
        self.picdir.setObjectName("picdir")
        self.gridLayout.addWidget(self.picdir, 0, 1, 1, 2)
        self.showimg = QtWidgets.QPushButton(self.centralwidget)
        self.showimg.setObjectName("showimg")
        self.gridLayout.addWidget(self.showimg, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.imgviewer = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgviewer.sizePolicy().hasHeightForWidth())
        self.imgviewer.setSizePolicy(sizePolicy)
        self.imgviewer.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.imgviewer.setScaledContents(True)
        self.imgviewer.setObjectName("imgviewer")
        self.horizontalLayout.addWidget(self.imgviewer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Cancel.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.picdir, self.addimgbutton)
        MainWindow.setTabOrder(self.addimgbutton, self.outputdir)
        MainWindow.setTabOrder(self.outputdir, self.adddirbutton)
        MainWindow.setTabOrder(self.adddirbutton, self.Cancel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DespensingQualityInspector"))
        self.adddirbutton.setText(_translate("MainWindow", "???????????????"))
        self.Cancel.setText(_translate("MainWindow", "Exit"))
        self.addimgbutton.setText(_translate("MainWindow", "????????????"))
        self.label_output.setText(_translate("MainWindow", "?????????????????????"))
        self.label_pic.setText(_translate("MainWindow", "?????????????????????"))
        self.OK.setText(_translate("MainWindow", "OK"))
        self.showimg.setText(_translate("MainWindow", "showimg"))
        self.imgviewer.setText(_translate("MainWindow", "TextLabel"))
