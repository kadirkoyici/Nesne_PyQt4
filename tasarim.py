# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Jan 15 09:36:01 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(382, 258)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 321, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.birinci_sayi = QtGui.QLineEdit(self.gridLayoutWidget)
        self.birinci_sayi.setObjectName(_fromUtf8("birinci_sayi"))
        self.gridLayout.addWidget(self.birinci_sayi, 0, 1, 1, 2)
        self.ikinci_sayi = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ikinci_sayi.setObjectName(_fromUtf8("ikinci_sayi"))
        self.gridLayout.addWidget(self.ikinci_sayi, 1, 1, 1, 2)
        self.ucuncu_sayi = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ucuncu_sayi.setObjectName(_fromUtf8("ucuncu_sayi"))
        self.gridLayout.addWidget(self.ucuncu_sayi, 2, 1, 1, 2)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.sonuc = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Mangal"))
        font.setPointSize(14)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName(_fromUtf8("sonuc"))
        self.gridLayout.addWidget(self.sonuc, 4, 1, 1, 2)
        self.hesapla_butonu = QtGui.QPushButton(self.gridLayoutWidget)
        self.hesapla_butonu.setObjectName(_fromUtf8("hesapla_butonu"))
        self.gridLayout.addWidget(self.hesapla_butonu, 3, 0, 1, 3)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 271, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(120, 220, 261, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Temizle = QtGui.QPushButton(Form)
        self.Temizle.setGeometry(QtCore.QRect(30, 210, 75, 31))
        self.Temizle.setObjectName(_fromUtf8("Temizle"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Temizle, QtCore.SIGNAL(_fromUtf8("pressed()")), self.label_6.clear)
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*        
        QtCore.QObject.connect(self.hesapla_butonu, QtCore.SIGNAL(_fromUtf8("pressed()")), self.hesapYap)
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Üç Sayının Ortalamasını Alan Program", None))
        self.label.setText(_translate("Form", "1. Sayı : ", None))
        self.label_2.setText(_translate("Form", "2. Sayı : ", None))
        self.label_3.setText(_translate("Form", "3. Sayı : ", None))
        self.label_4.setText(_translate("Form", "Sonuç : ", None))
        self.sonuc.setText(_translate("Form", "0000", None))
        self.hesapla_butonu.setText(_translate("Form", "Hesapla", None))
        self.label_5.setText(_translate("Form", "Sayıların Ortalamasını Alan Program :", None))
        self.label_6.setText(_translate("Form", "Bu Yazıyı Temizlemek istiyorsan Temizle butonuna bas", None))
        self.Temizle.setText(_translate("Form", "Temizle", None))
        
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    def hesapYap(self):
        ortalama = 0
        try:
            sayi1 = int(self.birinci_sayi.text())
            sayi2 = int(self.ikinci_sayi.text())
            sayi3 = int(self.ucuncu_sayi.text())
            ortalama = (sayi1 + sayi2 + sayi3)/3
        except:
            self.sonuc.setText('<span style="color:red;font-weight:bold">Tam sayi giriniz!</span>')
            return
        self.sonuc.setText('<span style="color:red;font-weight:bold">%0.2f</span>' % ortalama)
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

