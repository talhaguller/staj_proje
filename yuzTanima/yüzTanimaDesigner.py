# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Talha\Desktop\isYeri\yuzTanima\yüzTanimaDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1041, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Form.setFont(font)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setWindowOpacity(1.0)
        self.label_name_text = QtWidgets.QLabel(Form)
        self.label_name_text.setEnabled(True)
        self.label_name_text.setGeometry(QtCore.QRect(320, 640, 131, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name_text.sizePolicy().hasHeightForWidth())
        self.label_name_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_name_text.setFont(font)
        self.label_name_text.setObjectName("label_name_text")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(380, 710, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(460, 660, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.file_listWidget = QtWidgets.QListWidget(Form)
        self.file_listWidget.setGeometry(QtCore.QRect(30, 80, 361, 421))
        self.file_listWidget.setObjectName("file_listWidget")
        self.yon_lbl = QtWidgets.QLabel(Form)
        self.yon_lbl.setGeometry(QtCore.QRect(310, 560, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.yon_lbl.setFont(font)
        self.yon_lbl.setTextFormat(QtCore.Qt.PlainText)
        self.yon_lbl.setObjectName("yon_lbl")
        self.yon_degistir_btn = QtWidgets.QPushButton(Form)
        self.yon_degistir_btn.setGeometry(QtCore.QRect(630, 560, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.yon_degistir_btn.setFont(font)
        self.yon_degistir_btn.setObjectName("yon_degistir_btn")
        self.sayac_lbl = QtWidgets.QLabel(Form)
        self.sayac_lbl.setGeometry(QtCore.QRect(730, 570, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sayac_lbl.setFont(font)
        self.sayac_lbl.setText("")
        self.sayac_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.sayac_lbl.setObjectName("sayac_lbl")
        self.file_name_comboBox = QtWidgets.QComboBox(Form)
        self.file_name_comboBox.setGeometry(QtCore.QRect(30, 40, 201, 31))
        self.file_name_comboBox.setObjectName("file_name_comboBox")
        self.file_open_btn = QtWidgets.QPushButton(Form)
        self.file_open_btn.setGeometry(QtCore.QRect(250, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.file_open_btn.setFont(font)
        self.file_open_btn.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color : lightgreen;\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font: 18pt \"Rage Italic\";\n"
"color: rgb(85, 33, 255);\n"
"background-color : #ff6cc7;\n"
"\n"
"}\n"
"")
        self.file_open_btn.setCheckable(True)
        self.file_open_btn.setObjectName("file_open_btn")
        self.image_lbl = QtWidgets.QLabel(Form)
        self.image_lbl.setGeometry(QtCore.QRect(530, 100, 401, 351))
        self.image_lbl.setText("")
        self.image_lbl.setScaledContents(True)
        self.image_lbl.setObjectName("image_lbl")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "yüzTanima"))
        self.label_name_text.setText(_translate("Form", "İSİM GİRİNİZ:"))
        self.pushButton.setText(_translate("Form", "Dosya Oluşturun"))
        self.yon_lbl.setText(_translate("Form", "Ön Yüzünüzü Dönün"))
        self.yon_degistir_btn.setText(_translate("Form", "BAŞLA"))
        self.file_open_btn.setText(_translate("Form", "Dosya Aç"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
