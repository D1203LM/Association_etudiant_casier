class Cours:
    """
    Classe Cours

    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_sigle_cours="", p_titre_cours="", p_nombre_heures_cours=0):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs d'un cours
        """
        self.__sigle_cours = p_sigle_cours
        self.__titre_cours = p_titre_cours
        self.__nombre_heures_cours = p_nombre_heures_cours

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété SigleCours
    def _get_sigle_cours(self):
        """
                Accesseur de l'attribut privé  __sigle_cours
        """
        return self.__sigle_cours

    def _set_sigle_cours(self, p_sigle_cours):
        """
                Mutateur de l'attribut privé  __sigle_cours
        """
        if len(p_sigle_cours) == 5 and p_sigle_cours[0].isalpha() and p_sigle_cours[1:4].isnumeric():
            self.__sigle_cours = p_sigle_cours

    SigeleCours = property(_get_sigle_cours, _set_sigle_cours)

    # Propriété TitreCours
    def _get_titre_cours(self):
        """
                Accesseur de l'attribut privé  __titre_cours
        """
        return self.__titre_cours

    def _set_titre_cours(self, p_titre_cours):
        """
                Mutateur de l'attribut privé  __titre_cours
        """
        if len(p_titre_cours) <= 60:
            self.__titre_cours = p_titre_cours

    TitreCours = property(_get_titre_cours, _set_titre_cours)

    # Propriété NombreHeureCours
    def _get_nombre_heures_cours(self):
        """
                Accesseur de l'attribut privé  __nombre_heures_cours
        """
        return self.__nombre_heures_cours

    def _set_nombre_heures_cours(self, p_nombre_heures_cours):
        """
                Mutateur de l'attribut privé  __nombre_heures_cours
        """
        if p_nombre_heures_cours > 0 :
            self.__nombre_heures_cours = p_nombre_heures_cours

    NombreHeuresCours = property(_get_nombre_heures_cours, _set_nombre_heures_cours)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine = "\nSigle du cours : " + self.__sigle_cours
        chaine += "\nTitre du cours : " + self.__titre_cours
        chaine += "\nNombre d'heures du cours : " + str(self.__nombre_heures_cours)

        return chaine