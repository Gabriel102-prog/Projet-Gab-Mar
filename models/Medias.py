class Medias(ABC):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt):
        self.__identifiant = identifiant
        self.__titre = titre
        self.__annee_parution = annee_parution
        self.__genre = genre
        self.__disponible = disponible
        self.__date_emprunt = date_emprunt
        self.__date_retour = date_retour

    @property
    def date_emprunt(self):
        return self.__date_emprunt

    @date_emprunt.setter
    def date_emprunt(self, date_emprunt_2):
        self.__date_emprunt = date_emprunt_2

    @property
    def date_retour(self):
        return self.__date_retour

    @date_retour.setter
    def date_retour(self, date_retour_2):
        self.__date_retour = date_retour_2

    @property
    def identifiant(self):
        return self.__identifiant

    @property
    def titre(self):
        return self.__titre

    @property
    def annee_parution(self):
        return self.__annee_parution

    @property
    def genre(self):
        return self.__genre

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, nouvelle_valeur):
        self.__disponible = nouvelle_valeur

    @abstractmethod
    def afficher_media(self):
        pass