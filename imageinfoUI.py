from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import mysqlconnection
import os
from datetime import datetime
from PIL import Image
from PIL import ImageEnhance
from dlg import Ui_Algrthm

mydb = mysql.connector.connect(
    host="localhost",
    user="idodo",
    passwd="idodo123",
    database="image"
)
mycursor = mydb.cursor(buffered=True)

class Ui_imginfo(object):
    # def openImginfo(self):
    #     dImginfo.close()
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_Algrthm()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    def imgInfo(self):
        CASENO=self.caseedit.text()
        AGENCY=self.agentedit.text()
        INVESTIGATOR=self.investedit.text()
        IMGTYPE=self.type_box.currentText()
        IMGDES=self.des_text.toPlainText()
        print(CASENO)
        print(AGENCY)
        print(INVESTIGATOR)
        print(IMGTYPE)
        print(IMGDES)
        print(dir)
        mySql = """INSERT INTO imageinfo (caseno, agency, investigator, type, description, file)
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """, (CASENO, AGENCY, INVESTIGATOR, IMGTYPE, IMGDES, dir)
        mycursor.execute(*mySql)
        mydb.commit()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Algrthm()
        self.ui.setupUi(self.window)
        self.window.show()




    def setupUi(self, dImginfo):
        dImginfo.setObjectName("dImginfo")
        dImginfo.resize(1182, 870)
        dImginfo.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.label = QtWidgets.QLabel(dImginfo)
        self.label.setGeometry(QtCore.QRect(50, 190, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dImginfo)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dImginfo)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dImginfo)
        self.label_4.setGeometry(QtCore.QRect(50, 370, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.type_box = QtWidgets.QComboBox(dImginfo)
        self.type_box.setGeometry(QtCore.QRect(340, 380, 131, 31))
        self.type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.label_5 = QtWidgets.QLabel(dImginfo)
        self.label_5.setGeometry(QtCore.QRect(50, 430, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.des_text = QtWidgets.QTextEdit(dImginfo)
        self.des_text.setGeometry(QtCore.QRect(340, 450, 421, 101))
        self.des_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.des_text.setObjectName("des_text")
        self.label_6 = QtWidgets.QLabel(dImginfo)
        self.label_6.setGeometry(QtCore.QRect(220, 600, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.browse = QtWidgets.QPushButton(dImginfo)
        self.browse.setGeometry(QtCore.QRect(340, 620, 141, 31))
        self.browse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse.setObjectName("browse")
        self.next = QtWidgets.QPushButton(dImginfo)
        self.next.setGeometry(QtCore.QRect(470, 730, 141, 31))
        self.next.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next.setObjectName("next")
        self.caseedit = QtWidgets.QLineEdit(dImginfo)
        self.caseedit.setGeometry(QtCore.QRect(340, 200, 401, 31))
        self.caseedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.caseedit.setObjectName("caseedit")
        self.agentedit = QtWidgets.QLineEdit(dImginfo)
        self.agentedit.setGeometry(QtCore.QRect(340, 250, 401, 31))
        self.agentedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.agentedit.setObjectName("agentedit")
        self.investedit = QtWidgets.QLineEdit(dImginfo)
        self.investedit.setGeometry(QtCore.QRect(340, 310, 401, 31))
        self.investedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.investedit.setObjectName("investedit")

        self.next.clicked.connect(self.imgInfo)
        self.browse.clicked.connect(self.setImage)
        self.retranslateUi(dImginfo)
        QtCore.QMetaObject.connectSlotsByName(dImginfo)


    def setImage(self):
        global fileName,dir,time
        time = datetime.now().strftime("%d:%m:%Y:%H:%M:%S")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        image = Image.open(fileName)
        image.save("temp/"+ time +".png")
        global dir
        dir = "temp/"+ time +".png"
        self.browse.setText(dir)


    def retranslateUi(self, dImginfo):
        _translate = QtCore.QCoreApplication.translate
        dImginfo.setWindowTitle(_translate("dImginfo", "dImginfo"))
        self.label.setText(_translate("dImginfo", "CASE NO:"))
        self.label_2.setText(_translate("dImginfo", "AGENCY:"))
        self.label_3.setText(_translate("dImginfo", "INVESTIGATOR:"))
        self.label_4.setText(_translate("dImginfo", "IMAGE TYPE:"))
        self.type_box.setItemText(0, _translate("dImginfo", ".JPG"))
        self.type_box.setItemText(1, _translate("dImginfo", ".PNG"))
        self.type_box.setItemText(2, _translate("dImginfo", ".GIF"))
        self.type_box.setItemText(3, _translate("dImginfo", ".BMP"))
        self.label_5.setText(_translate("dImginfo", "IMAGE DESCRIPTION:"))
        self.label_6.setText(_translate("dImginfo", "IMAGE:"))
        self.browse.setText(_translate("dImginfo", "BROWSE"))
        self.next.setText(_translate("dImginfo", "NEXT"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dImginfo = QtWidgets.QMainWindow()
    ui = Ui_imginfo()
    ui.setupUi(dImginfo)
    dImginfo.show()
    sys.exit(app.exec_())

