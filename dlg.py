# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
#from PIL import Image
#from PIL import ImageEnhance
import numpy as np
from cv2 import cv2
# from matplotlib import pyplot as plt
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
import fn
import histogram as h
import cumulative_histogram as ch
from report import Ui_Report

class Ui_Algrthm(object):
    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Report()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, algowin):
        algowin.setObjectName("algowin")
        algowin.resize(1000, 800)
        algowin.setStyleSheet("background:rgb(100, 89, 255)")
        self.imagelab1 = QtWidgets.QLabel(algowin)
        self.imagelab1.setGeometry(QtCore.QRect(10, 140, 411, 421))
        self.imagelab1.setFrameShape(QtWidgets.QFrame.Box)
        self.imagelab1.setObjectName("imagelab1")

        self.imagelab2 = QtWidgets.QLabel(algowin)
        self.imagelab2.setGeometry(QtCore.QRect(425, 140, 411, 421))
        self.imagelab2.setFrameShape(QtWidgets.QFrame.Box)
        self.imagelab2.setObjectName("imagelab2")

        self.uploadbtn = QtWidgets.QPushButton(algowin)
        self.uploadbtn.setGeometry(QtCore.QRect(10, 580, 141, 51))
        self.uploadbtn.setStyleSheet("background-color:rgb(255, 123, 8);\n""color:rgb(255, 255, 255);")
        self.uploadbtn.setObjectName("uploadbtn")

        self.pushButton_3 = QtWidgets.QPushButton(algowin)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 580, 141, 51))
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 123, 8);\n""color:rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("savebtn")

        # self.pushButton_4 = QtWidgets.QPushButton(algowin)
        # self.pushButton_4.setGeometry(QtCore.QRect(280, 580, 141, 51))
        # self.pushButton_4.setStyleSheet("background-color:rgb(255, 123, 8);\n""color:rgb(255, 255, 255);")
        # self.pushButton_4.setObjectName("convertbtn")

        self.noisebtn= QtWidgets.QPushButton(algowin)
        self.noisebtn.setGeometry(QtCore.QRect(850, 210, 141, 51))
        self.noisebtn.setStyleSheet("Background-color:rgb(255, 255, 255);\n""font-size\n""font: 63 9pt \"Samyak Devanagari\";")
        self.noisebtn.setObjectName("noisebtn")

        self.macbtn = QtWidgets.QPushButton(algowin)
        self.macbtn.setGeometry(QtCore.QRect(850, 270, 141, 51))
        self.macbtn.setStyleSheet("Background-color:rgb(255, 255, 255);\n""font-size\n""font: 63 9pt \"Samyak Devanagari\";")
        self.macbtn.setObjectName("mac")

        self.sccbtn = QtWidgets.QPushButton(algowin)
        self.sccbtn.setGeometry(QtCore.QRect(850, 330, 141, 51))
        self.sccbtn.setStyleSheet("Background-color:rgb(255, 255, 255);\n""font-size\n""font: 63 9pt \"Samyak Devanagari\";")
        self.sccbtn.setObjectName("sccbtn")

        self.medianbtn = QtWidgets.QPushButton(algowin)
        self.medianbtn.setGeometry(QtCore.QRect(850, 390, 141, 51))
        self.medianbtn.setStyleSheet("Background-color:rgb(255, 255, 255);\n""font-size\n""font: 63 9pt \"Samyak Devanagari\";")
        self.medianbtn.setObjectName("medianbtn")

        self.max_btn = QtWidgets.QPushButton(algowin)
        self.max_btn.setGeometry(QtCore.QRect(850, 450, 141, 51))
        self.max_btn.setStyleSheet("Background-color:rgb(255, 255, 255);\n""font-size\n""font: 63 9pt \"Samyak Devanagari\";")
        self.max_btn.setObjectName("max_btn")

        self.min_btn = QtWidgets.QPushButton(algowin)
        self.min_btn.setGeometry(QtCore.QRect(850, 510, 141, 51))
        self.min_btn.setStyleSheet("Background-color:rgb(255, 255, 255);\n""font-size\n""font: 63 9pt \"Samyak Devanagari\";")
        self.min_btn.setObjectName("minbtn")

        self.label = QtWidgets.QLabel(algowin)
        self.label.setGeometry(QtCore.QRect(850, 130, 171, 51))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n""font-size:25px;\n""font: 63 20pt \"Samyak Devanagari\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(algowin)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 201, 51))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n""font-size:25px;\n""font: 63 20pt \"Samyak Devanagari\";")
        self.label_2.setObjectName("label_2")

        self.uploadbtn.clicked.connect(self.setImage)
        self.noisebtn.clicked.connect(self.noise)
        self.macbtn.clicked.connect(self.mac)
        self.sccbtn.clicked.connect(self.scc)
        self.medianbtn.clicked.connect(self.median)
        self.max_btn.clicked.connect(self.max)
        self.min_btn.clicked.connect(self.min)
        self.pushButton_3.clicked.connect(self.openwindow)

        self.retranslateUi(algowin)
        QtCore.QMetaObject.connectSlotsByName(algowin)

    def retranslateUi(self, algowin):
        _translate = QtCore.QCoreApplication.translate
        algowin.setWindowTitle(_translate("algowin", "algrthm"))
        self.uploadbtn.setText(_translate("algowin", "Show Image"))
        self.pushButton_3.setText(_translate("algowin", "Next"))
        # self.pushButton_4.setText(_translate("algowin", "Convert Again"))
        self.noisebtn.setText(_translate("algowin", "noise"))
        self.macbtn.setText(_translate("algowin", "mac"))
        self.sccbtn.setText(_translate("algowin", "scc"))
        self.medianbtn.setText(_translate("algowin", "median"))
        self.max_btn.setText(_translate("algowin", "max"))
        self.min_btn.setText(_translate("algowin", "min"))
        self.label.setText(_translate("algowin", "Filters"))
        self.label_2.setText(_translate("algowin", "I-dodo"))



    def setImage(self):
        fn.setImage(self)


    def noise(self):
        fn.noise(self)

    def mac(self):
        fn.mac(self)

    def scc(self):
        fn.scc(self)

    def median(self):
        fn.median_new(self)

    def max(self):
        fn.max(self)

    def min(self):
        fn.min(self)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    algowin = QtWidgets.QMainWindow()
    ui = Ui_Algrthm()
    ui.setupUi(algowin)
    algowin.show()
    sys.exit(app.exec_())

