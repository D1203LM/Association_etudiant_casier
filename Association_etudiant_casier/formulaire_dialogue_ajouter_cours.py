# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogue_listcours.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(586, 671)
        self.label_numero_etudiant = QtWidgets.QLabel(Dialog)
        self.label_numero_etudiant.setGeometry(QtCore.QRect(100, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numero_etudiant.setFont(font)
        self.label_numero_etudiant.setObjectName("label_numero_etudiant")
        self.lineEdit_numero_etudiant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numero_etudiant.setGeometry(QtCore.QRect(100, 70, 201, 41))
        self.lineEdit_numero_etudiant.setObjectName("lineEdit_numero_etudiant")
        self.label_erreur_numero_etudiant = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero_etudiant.setGeometry(QtCore.QRect(100, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_numero_etudiant.setFont(font)
        self.label_erreur_numero_etudiant.setObjectName("label_erreur_numero_etudiant")
        self.label_cours = QtWidgets.QLabel(Dialog)
        self.label_cours.setGeometry(QtCore.QRect(100, 160, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cours.setFont(font)
        self.label_cours.setObjectName("label_cours")
        self.comboBox_cours = QtWidgets.QComboBox(Dialog)
        self.comboBox_cours.setGeometry(QtCore.QRect(100, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_cours.setFont(font)
        self.comboBox_cours.setObjectName("comboBox_cours")
        self.comboBox_cours.addItem("")
        self.comboBox_cours.addItem("")
        self.comboBox_cours.addItem("")
        self.pushButton_ajouter = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter.setGeometry(QtCore.QRect(100, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter.setFont(font)
        self.pushButton_ajouter.setObjectName("pushButton_ajouter")
        self.pushButton_quitter = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter.setGeometry(QtCore.QRect(350, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter.setFont(font)
        self.pushButton_quitter.setObjectName("pushButton_quitter")
        self.listView_cours = QtWidgets.QListView(Dialog)
        self.listView_cours.setGeometry(QtCore.QRect(100, 310, 361, 192))
        self.listView_cours.setObjectName("listView_cours")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_numero_etudiant.setText(_translate("Dialog", "Numéro étudiant"))
        self.label_erreur_numero_etudiant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant n\'existe pas.</span></p></body></html>"))
        self.label_cours.setText(_translate("Dialog", "Cours"))
        self.comboBox_cours.setItemText(0, _translate("Dialog", "Programmation orientée objet"))
        self.comboBox_cours.setItemText(1, _translate("Dialog", "Infrastructure et services réseaux"))
        self.comboBox_cours.setItemText(2, _translate("Dialog", "Outils et carrière"))
        self.pushButton_ajouter.setText(_translate("Dialog", "Ajouter"))
        self.pushButton_quitter.setText(_translate("Dialog", "Quitter"))