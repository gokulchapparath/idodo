
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import mysqlconnection
from datetime import datetime
#from PyQt5.QtWidgets import QApplication, QMainWindow,  QAction, QTextEdit, QFontdReport, QColordReport, QFiledReport
import sys
#from PyQt5.QtGui import QIcon
#from PyQt5.QtPrintSupport import QPrintdReport, QPrinter, QPrintPreviewdReport
#from PyQt5.Qt import QFileInfo

mydb = mysql.connector.connect(
    host="localhost",
    user="idodo",
    passwd="idodo123",
    database="image"
)
mycursor = mydb.cursor(buffered=True)

class Ui_Report(object):
    def setupUi(self, dReport):
        global disps
        global time
        global algorithm
        display = """select * from imageinfo order by id desc"""
        mycursor.execute(display, )
        disp = mycursor.fetchone()
        disps = [row for row in disp]
        time = datetime.now().strftime("%H:%M:%S")
        algorithm = 'sha1'
        print(disps[0])
        print(disps[1])
        print(disps[2])
        print(disps[3])
        dir = "temp/a.png"
        dReport.setObjectName("dReport")
        dReport.resize(1114, 845)
        self.label = QtWidgets.QLabel(dReport)
        self.label.setGeometry(QtCore.QRect(300, 140, 291, 251))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dReport)
        self.label_2.setGeometry(QtCore.QRect(160, 420, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dReport)
        self.label_3.setGeometry(QtCore.QRect(160, 470, 171, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dReport)
        self.label_4.setGeometry(QtCore.QRect(160, 500, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dReport)
        self.label_5.setGeometry(QtCore.QRect(160, 540, 151, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(dReport)
        self.label_6.setGeometry(QtCore.QRect(420, 60, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(dReport)
        self.label_7.setGeometry(QtCore.QRect(160, 590, 141, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(dReport)
        self.label_8.setGeometry(QtCore.QRect(160, 630, 131, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(dReport)
        self.label_9.setGeometry(QtCore.QRect(320, 470, 171, 31))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(dReport)
        self.label_10.setGeometry(QtCore.QRect(320, 500, 131, 31))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(dReport)
        self.label_11.setGeometry(QtCore.QRect(320, 540, 151, 31))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(dReport)
        self.label_12.setGeometry(QtCore.QRect(320, 626, 131, 21))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(dReport)
        self.label_13.setGeometry(QtCore.QRect(320, 586, 151, 21))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(dReport)
        self.label_14.setGeometry(QtCore.QRect(320, 420, 161, 31))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")

        self.exportbtn = QtWidgets.QPushButton(dReport)
        self.exportbtn.setGeometry(QtCore.QRect(350, 700, 141, 51))
        self.exportbtn.setStyleSheet("background-color:rgb(255, 123, 8);\n""color:rgb(255, 255, 255);")
        self.exportbtn.setObjectName("export_btn")

        pixmap = QtGui.QPixmap("output/output.jpg") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.label.setPixmap(pixmap) # Set the pixmap onto the label
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.exportbtn.clicked.connect(self.pdf)

        self.retranslateUi(dReport)
        QtCore.QMetaObject.connectSlotsByName(dReport)

    def retranslateUi(self, dReport):
        _translate = QtCore.QCoreApplication.translate
        dReport.setWindowTitle(_translate("dReport", "dReport"))
        self.label.setText(_translate("dReport", ""))
        self.label_2.setText(_translate("dReport", "CASE NO                :"))
        self.label_3.setText(_translate("dReport", "AGENCY                  :"))
        self.label_4.setText(_translate("dReport", "INVESTIGATOR     :"))
        self.label_5.setText(_translate("dReport", "AGENCY                  :"))
        self.label_6.setText(_translate("dReport", "REPORT"))
        self.label_7.setText(_translate("dReport", "DATE & TIME         :"))
        self.label_8.setText(_translate("dReport", "ALGORITHM          :"))
        self.exportbtn.setText(_translate("dReport", "export_btn"))
        self.label_14.setText(_translate("dReport", str(disps[1])))
        self.label_9.setText(_translate("dReport", str(disps[2])))
        self.label_10.setText(_translate("dReport", str(disps[3])))
        self.label_11.setText(_translate("dReport", str(disps[4])))
        self.label_13.setText(_translate("dReport", str(time)))
        self.label_12.setText(_translate("dReport", str(algorithm)))

    def pdf(self):
        fn, _ = QFiledReport.getSaveFileName(self, 'export_btn', None, 'PDF files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() == "" : fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.label_2.document().print_(printer)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dReport = QtWidgets.QMainWindow()
    ui = Ui_Report()
    ui.setupUi(dReport)
    dReport.show()
    sys.exit(app.exec_())
