from Local import *

class Local_technique (Local):
    """
    Classe Local_technique, dérivée de la classe parent Local
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_type_local="", p_num_local="", p_lieu_local="", p_dimension_local="", p_nbr_places=0,
                p_marque_ordi="", p_nb_ordi=0, p_projecteur=""):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un local technique
        """
        Local.__init__(self, p_type_local, p_num_local, p_lieu_local, p_dimension_local, p_nbr_places)
        self.__marque_ordi = p_marque_ordi
        self.__nb_ordi = p_nb_ordi
        self.Projecteur = p_projecteur

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété MarqueOrdi
    def _get_marque_ordi(self):
        """
        Accesseur de l'attribut privée __marque_ordi
        """
        return self.__marque_ordi

    def _set_marque_ordi(self, p_marque_ordi):
        """
        Mutateur de l'attribut privée __marque_ordi
        """
        if len(p_marque_ordi) < 100:
            self.__marque_ordi = p_marque_ordi

    MarqueOrdi = property(_get_marque_ordi, _set_marque_ordi)

    # Propriété NbOrdi
    def _get_nb_ordi(self):
        """
        Accesseur de l'attribut privée __nb_ordi
        """
        return self.__nb_ordi

    def _set_nb_ordi(self, p_nb_ordi):
        """
        Mutateur de l'attribut privée __nb_ordi
        """
        if p_nb_ordi > 0 and p_nb_ordi < 25:
            self.__nb_ordi = p_nb_ordi

    NbOrdi = property(_get_nb_ordi, _set_nb_ordi)