class Local:
    """
    Classe parent Local

    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_type_local="", p_num_local="", p_lieu_local="", p_dimension_local="", p_nbr_places=0):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un local
        """
        self.Type_local = p_type_local
        self.__num_local = p_num_local
        self.Lieu_local = p_lieu_local
        self.__dimension_local = p_dimension_local
        self.__nbr_places = p_nbr_places

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété NumLocal
    def _get_num_local(self):
        """
        Accesseur de l'attribut privée __num_local
        """
        return self.__num_local

    def _set_num_local(self, p_num_local):
        """
        Mutateur de l'attribut privée __num_local
        """
        if len(p_num_local) == 5 and p_num_local[0].isalpha() and p_num_local[1] == "-" and p_num_local[2:4].isnumeric():
            self.__num_local = p_num_local

    NumLocal = property(_get_num_local, _set_num_local)

    # Propriété DimensionLocal
    def _get_dimension_local(self):
        """
        Accesseur de l'attribut privée __dimension_local
        """
        return self.__dimension_local

    def _set_dimension_local(self, p_dimension_local):
        """
        Mutateur de l'attribut privée __dimension_local
        """
        if p_dimension_local > 0:
            self.__dimension_local = p_dimension_local

    DimensionLocal = property(_get_dimension_local, _set_dimension_local)

    # Propriété NbrPlaces
    def _get_nbr_places(self):
        """
        Accesseur de l'attribut privée __nbr_places
        """
        return self.__nbr_places

    def _set_nbr_places(self, p_nbr_places):
        """
        Mutateur de l'attribut privée __nbr_places
        """
        if p_nbr_places > 0 and p_nbr_places < 25:
            self.__nbr_places =p_nbr_places

    NbrPlaces = property(_get_nbr_places, _set_nbr_places)