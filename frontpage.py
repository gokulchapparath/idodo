from PyQt5 import QtCore, QtGui, QtWidgets
import st
from imageinfoUI import Ui_imginfo
import sys

class Ui_Mains(object):
    def openImginfo(self):
        dMain.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_imginfo()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, dMain):
        dMain.setObjectName("dMain")
        dMain.resize(1186, 885)
        dMain.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.label = QtWidgets.QLabel(dMain)
        self.label.setGeometry(QtCore.QRect(450, 80, 261, 341))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(
            "image: url(:/home/shafiya/Desktop/new_prv/logos/dodo.jpg/dodo.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dMain)
        self.label_2.setGeometry(QtCore.QRect(500, 460, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(dMain)
        self.pushButton.setGeometry(QtCore.QRect(500, 710, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Samyak Devanagari")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "\n""background-color: rgb(239, 41, 41);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openImginfo)

        self.retranslateUi(dMain)
        QtCore.QMetaObject.connectSlotsByName(dMain)

    def retranslateUi(self, dMain):
        _translate = QtCore.QCoreApplication.translate
        dMain.setWindowTitle(_translate("dMain", "IDODO"))
        self.label_2.setText(_translate("dMain", "I DODO"))
        self.pushButton.setText(_translate("dMain", "ENTER"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dMain = QtWidgets.QMainWindow()
    ui = Ui_Mains()
    ui.setupUi(dMain)
    dMain.show()
    sys.exit(app.exec_())
