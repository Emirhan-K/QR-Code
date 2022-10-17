import numpy as np
import cv2
from pyzbar.pyzbar import decode
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ornek1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_dosyaOku = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dosyaOku.setGeometry(QtCore.QRect(200, 10, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dosyaOku.setFont(font)
        self.btn_dosyaOku.setObjectName("btn_dosyaOku")
        self.btn_kameraOku = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kameraOku.setGeometry(QtCore.QRect(30, 10, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_kameraOku.setFont(font)
        self.btn_kameraOku.setObjectName("btn_kameraOku")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbl_qr = QtWidgets.QLabel(self.centralwidget)
        self.lbl_qr.setGeometry(QtCore.QRect(30, 150, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qr.setFont(font)
        self.lbl_qr.setText("")
        self.lbl_qr.setObjectName("lbl_qr")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR KOD"))
        self.btn_dosyaOku.setText(_translate("MainWindow", "Dosyadan QR Oku"))
        self.btn_kameraOku.setText(_translate("MainWindow", "Kameradan QR Oku"))
        self.label.setText(_translate("MainWindow", "QR İçeriği :"))
        self.btn_dosyaOku.clicked.connect(self.decode_file)
        self.btn_kameraOku.clicked.connect(self.decode_camera)

    def decode_camera(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)

        while True:
            
            succes, img = cap.read()
            
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                
                pts =np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(250,0,250),5)
                pts2= barcode.rect
                cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(250,0,250),2)
                self.lbl_qr.setText(myData)

                
            cv2.imshow('Bilgisayar Kamerası', img)
            cv2.waitKey(1)  
            
            

    def decode_file(self):
        file = filedialog.askopenfilename(filetypes=(("resim", "*.png"),))
        img = cv2.imread(file)
        for barcode in decode(img):
            myData = barcode.data.decode('ascii')
            self.lbl_qr.setText(myData)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
