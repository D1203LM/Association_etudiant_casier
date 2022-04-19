class Casier:
    """
     Classe Casier

    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_casier="", p_taille_casier="", p_localisation_casier=""):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs d'un casier
        """
        self.__num_casier = p_num_casier
        self.Taille_casier = p_taille_casier
        self.Localisation_casier = p_localisation_casier
        self.__prix_casier = 20

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété NumCasier
    def _get_num_casier(self):
        """
                Accesseur de l'attribut privé  __num_casier
        """
        return self.__num_casier

    def _set_num_casier(self, p_num_casier):
        """
                Mutateur de l'attribut privé __num_casier
        """
        if len(p_num_casier) == 5 and p_num_casier[0].isalpha() and p_num_casier[1:4].isnumeric():
            self.__num_casier = p_num_casier

    NumCasier = property(_get_num_casier, _set_num_casier)

    # Propriété PrixCasier
    def _get_prix_casier(self):
        """
                Accesseur de l'attribut privé __prix_casier
        """
        return self.__prix_casier

    PrixCasier = property(_get_prix_casier)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine = "\nNuméro du casier : " + self.__num_casier
        chaine += "\nTaille du casier : " + self.Taille_casier
        chaine += "\nLocalisation du casier : " + self.Localisation_casier
        chaine += "\nPrix du casier : " + str(self.__prix_casier)

        return chaine