# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import formulaire_dialogue_listcours


#####################################################
##### DÉFINITIONS DE LA CLASSE Fenetrelistcours #####
#####################################################

class Fenetrelistcours(QtWidgets.QDialog, formulaire_dialogue_listcours.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetrelistcours, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des cours")

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()