# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import formulaire_dialogue_ajouter_local


# Déclarer une liste de locaux
ls_Locaux = []

##########################################################
###### DÉFINITIONS DE LA CLASSE Fenetreajouterlocal ######
##########################################################

class Fenetreajouterlocal(QtWidgets.QDialog, formulaire_dialogue_ajouter_local.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetreajouterlocal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Local")

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()