from Local import *

class Local_normal (Local):
    """
    Classe Locla_normal, dérivée de la classe parent Local
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_type_local="", p_num_local="", p_lieu_local="", p_dimension_local="", p_nbr_places=0,
                 p_nb_places_table=1):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un local normal
        """
        Local.__init__(self, p_type_local, p_num_local, p_lieu_local, p_dimension_local, p_nbr_places)
        self.__nb_places_table = p_nb_places_table

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété NbPlacesTable
    def _get_nb_places_table(self):
        """
        Accesseur de l'attribut privée __nb_places_table
        """
        return self.__nb_places_table

    def _set_nb_places_table(self, p_nb_places_table):
        """
        Mutateur de l'attribut privée __nb_places_table
        """
        if p_nb_places_table == 1 or p_nb_places_table == 2:
            self.__nb_places_table = p_nb_places_table

    NbPlacesTable = property(_get_nb_places_table, _set_nb_places_table)