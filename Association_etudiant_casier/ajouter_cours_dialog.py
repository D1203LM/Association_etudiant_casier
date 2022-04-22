# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import formulaire_dialogue_ajouter_cours


# Déclarer une liste de cours
ls_Cours = []

#####################################################
##### DÉFINITIONS DE LA CLASSE Fenetrelistcours #####
#####################################################

class Fenetreajoutercours(QtWidgets.QDialog, formulaire_dialogue_ajouter_cours.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetreajoutercours, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter cours")

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()