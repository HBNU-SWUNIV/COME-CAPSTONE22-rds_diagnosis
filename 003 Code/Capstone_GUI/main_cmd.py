# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capstone_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, QSize, Qt
from PyQt5.QtGui import QPixmap

from CV_segmentation_visualize import inference
from img_crop import img_crop
from CV_gradcam_ensemble import gradcam

class Ui_MainWindow(QMainWindow):

    def upload_click(self):
        global input_img_path
        input_img_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        if input_img_path :
            input_pixmap = QPixmap(input_img_path)
            input_pixmap = input_pixmap.scaled(QSize(431, 641))
            self.input_image.setPixmap(input_pixmap)

    def result_click(self):
        global photo2, photo3

        seg_img_save_path = inference(input_img_path)
        crop_img_save_path = img_crop(seg_img_save_path)
        gradcam_save_path, pred, score = gradcam(crop_img_save_path)

        crop_pixmap = QPixmap(crop_img_save_path)
        crop_pixmap = crop_pixmap.scaled(QSize(300, 300))
        self.crop_image.setPixmap(crop_pixmap)

        gcam_pixmap = QPixmap(gradcam_save_path)
        gcam_pixmap = gcam_pixmap.scaled(QSize(300, 300))
        self.gcam_image.setPixmap(gcam_pixmap)

        pred = str(pred)
        score = str(score)

        _translate = QtCore.QCoreApplication.translate
        self.proba_result.setText(_translate("MainWindow",
                                             f"<html><head/><body><p align=\"center\"><span style=\" font-family:\'HY견고딕\'; font-size:24pt; color:#000000;\">{score}%</span></p></body></html>"))
        self.RDS_result.setText(_translate("MainWindow",
                                           f"<html><head/><body><p align=\"center\"><span style=\" font-family:\'HY견고딕\'; font-size:24pt; color:#ffffff;\">{pred}</span></p></body></html>"))

        if pred == "RDS":
            self.RDS_frame.setStyleSheet("QFrame{\n"
                                         "    background-color : rgb(255, 0, 0)\n"
                                         "}")
        else :
            self.RDS_frame.setStyleSheet("QFrame{\n"
                                         "    background-color : rgb(0, 0, 255)\n"
                                         "}")


    def exit_click(self):
        self.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1080)
        MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1440, 16777215))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.title_frame = QtWidgets.QFrame(self.centralwidget)
        self.title_frame.setGeometry(QtCore.QRect(0, -10, 1440, 101))
        self.title_frame.setStyleSheet("QFrame{\n"
"    background-color : rgb(47, 48, 48)\n"
"}")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.title_name = QtWidgets.QLabel(self.title_frame)
        self.title_name.setGeometry(QtCore.QRect(20, 0, 551, 121))
        self.title_name.setStyleSheet("font: 9pt \"HY견고딕\";")
        self.title_name.setObjectName("title_name")
        self.body_frame = QtWidgets.QFrame(self.centralwidget)
        self.body_frame.setGeometry(QtCore.QRect(-11, 89, 1480, 1080))
        self.body_frame.setStyleSheet("QFrame{\n"
"    background-color : rgb(238, 239, 239)\n"
"}")
        self.body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_frame.setObjectName("body_frame")
        self.label_dashboard = QtWidgets.QLabel(self.body_frame)
        self.label_dashboard.setGeometry(QtCore.QRect(50, 40, 340, 80))
        self.label_dashboard.setStyleSheet("QLabel{\n"
"    background-color : rgb(20, 21, 20)\n"
"}")
        self.label_dashboard.setObjectName("label_dashboard")
        self.btn_upload = QtWidgets.QPushButton(self.body_frame)
        self.btn_upload.setGeometry(QtCore.QRect(50, 120, 340, 80))
        self.btn_upload.setStyleSheet("QPushButton{\n"
"    background-color : rgb(47, 48, 48);\n"
"    color : rgb(255,255,255);\n"
"    font: 14pt \"HY견고딕\";\n"
"}")
        self.btn_upload.setObjectName("btn_upload")
        self.btn_upload.clicked.connect(self.upload_click)


        self.btn_result = QtWidgets.QPushButton(self.body_frame)
        self.btn_result.setGeometry(QtCore.QRect(50, 200, 340, 80))
        self.btn_result.setStyleSheet("QPushButton{\n"
"    background-color : rgb(47, 48, 48);\n"
"    color : rgb(255,255,255);    \n"
"    font: 14pt \"HY견고딕\";\n"
"\n"
"}")
        self.btn_result.setObjectName("btn_result")
        self.btn_result.clicked.connect(self.result_click)


        self.btn_exit = QtWidgets.QPushButton(self.body_frame)
        self.btn_exit.setGeometry(QtCore.QRect(50, 280, 340, 80))
        self.btn_exit.setStyleSheet("QPushButton{\n"
"    background-color : rgb(47, 48, 48);\n"
"    color : rgb(255,255,255);\n"
"    font: 14pt \"HY견고딕\";\n"
"\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(QCoreApplication.instance().quit)

        self.proba_frame = QtWidgets.QFrame(self.body_frame)
        self.proba_frame.setGeometry(QtCore.QRect(955, 40, 450, 190))
        self.proba_frame.setStyleSheet("QFrame{\n"
"    background-color : rgb(255, 255, 255)\n"
"}")
        self.proba_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.proba_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.proba_frame.setObjectName("proba_frame")
        self.proba_result = QtWidgets.QLabel(self.proba_frame)
        self.proba_result.setGeometry(QtCore.QRect(0, 0, 450, 191))
        self.proba_result.setStyleSheet("QLabel {\n"
"}")
        self.proba_result.setObjectName("proba_result")
        self.proba_title = QtWidgets.QLabel(self.proba_frame)
        self.proba_title.setGeometry(QtCore.QRect(0, 130, 450, 40))
        self.proba_title.setStyleSheet("QLabel{\n"
"}")
        self.proba_title.setObjectName("proba_title")
        self.prob_design = QtWidgets.QLabel(self.proba_frame)
        self.prob_design.setGeometry(QtCore.QRect(0, 0, 450, 25))
        self.prob_design.setStyleSheet("QLabel{\n"
"    background-color : rgb(76, 221, 133)\n"
"}")
        self.prob_design.setText("")
        self.prob_design.setObjectName("prob_design")
        self.RDS_frame = QtWidgets.QFrame(self.body_frame)
        self.RDS_frame.setGeometry(QtCore.QRect(450, 40, 450, 190))
        self.RDS_frame.setStyleSheet("QFrame{\n"
"    background-color : rgb(124, 124, 124)\n"
"}")
        self.RDS_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RDS_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RDS_frame.setObjectName("RDS_frame")
        self.RDS_result = QtWidgets.QLabel(self.RDS_frame)
        self.RDS_result.setGeometry(QtCore.QRect(0, 0, 450, 191))
        self.RDS_result.setObjectName("RDS_result")
        self.RDS_title = QtWidgets.QLabel(self.RDS_frame)
        self.RDS_title.setGeometry(QtCore.QRect(0, 130, 450, 41))
        self.RDS_title.setStyleSheet("QLabel{\n"
"}")
        self.RDS_title.setObjectName("RDS_title")
        self.line = QtWidgets.QFrame(self.body_frame)
        self.line.setGeometry(QtCore.QRect(440, 250, 981, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.input_image = QtWidgets.QLabel(self.body_frame)

        self.input_image.setGeometry(QtCore.QRect(480, 310, 431, 641))
        self.input_image.setStyleSheet("QLabel{\n"
"\n"
"}")
        self.input_image.setText("")
        self.input_image.setAlignment(QtCore.Qt.AlignCenter)
        self.input_image.setObjectName("input_image")
        self.crop_image = QtWidgets.QLabel(self.body_frame)
        self.crop_image.setGeometry(QtCore.QRect(1030, 310, 300, 300))
        self.crop_image.setStyleSheet("QLabel{\n"
"\n"
"}")
        self.crop_image.setText("")
        self.crop_image.setAlignment(QtCore.Qt.AlignCenter)
        self.crop_image.setObjectName("crop_image")
        self.gcam_image = QtWidgets.QLabel(self.body_frame)
        self.gcam_image.setGeometry(QtCore.QRect(1030, 650, 300, 300))
        self.gcam_image.setStyleSheet("QLabel{\n"
"}")
        self.gcam_image.setText("")
        self.gcam_image.setAlignment(QtCore.Qt.AlignCenter)
        self.gcam_image.setObjectName("gcam_image")
        self.label_input = QtWidgets.QLabel(self.body_frame)
        self.label_input.setGeometry(QtCore.QRect(480, 270, 211, 40))
        self.label_input.setObjectName("label_input")
        self.label_crop = QtWidgets.QLabel(self.body_frame)
        self.label_crop.setGeometry(QtCore.QRect(1030, 270, 211, 40))
        self.label_crop.setObjectName("label_crop")
        self.label_gcam = QtWidgets.QLabel(self.body_frame)
        self.label_gcam.setGeometry(QtCore.QRect(1030, 613, 211, 41))
        self.label_gcam.setObjectName("label_gcam")
        self.label_dashboard.raise_()
        self.btn_upload.raise_()
        self.btn_result.raise_()
        self.btn_exit.raise_()
        self.proba_frame.raise_()
        self.RDS_frame.raise_()
        self.line.raise_()
        self.input_image.raise_()
        self.label_input.raise_()
        self.label_crop.raise_()
        self.label_gcam.raise_()
        self.gcam_image.raise_()
        self.crop_image.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RDS diagnotor"))
        self.title_frame.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.title_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">RDS Diagnosis</span></p></body></html>"))
        self.label_dashboard.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'HY견고딕\'; font-size:16pt; color:#ffffff;\">Dashboard</span></p></body></html>"))
        self.btn_upload.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_upload.setText(_translate("MainWindow", "Upload Image"))
        self.btn_result.setText(_translate("MainWindow", "Result"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.proba_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'HY견고딕\'; font-size:24pt; color:#000000;\">No Result</span></p></body></html>"))
        self.proba_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'HY견고딕\'; font-size:12pt;\">Probability</span></p></body></html>"))
        self.RDS_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'HY견고딕\'; font-size:24pt; color:#ffffff;\">No Result</span></p></body></html>"))
        self.RDS_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'HY견고딕\'; font-size:12pt; color:#d1d1d1;\">RDS/Non RDS</span></p></body></html>"))
        self.label_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'HY견고딕\'; font-size:12pt;\">Input Image</span></p></body></html>"))
        self.label_crop.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'HY견고딕\'; font-size:12pt;\">Crop Image</span></p></body></html>"))
        self.label_gcam.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'HY견고딕\'; font-size:12pt;\">Grad CAM</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

