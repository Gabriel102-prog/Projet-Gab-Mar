from abc import ABC, abstractmethod  # Importation des modules nécessaires pour utiliser des classes abstraites

class Medias(ABC):
    # Constructeur de la classe Medias, initialise les attributs de base de tous les médias
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt):
        self.__identifiant = identifiant  # Identifiant unique du média
        self.__titre = titre  # Titre du média
        self.__annee_parution = annee_parution  # Année de parution du média
        self.__genre = genre  # Genre du média (ex: roman, science-fiction, etc.)
        self.__disponible = disponible  # Disponibilité du média (True ou False)
        self.__date_emprunt = date_emprunt  # Date d'emprunt du média
        self.__date_retour = date_retour  # Date de retour du média (lorsqu'il est emprunté)

    # Propriétés pour accéder aux attributs privés de l'objet de manière sécurisée
    @property
    def date_emprunt(self):
        return self.__date_emprunt  # Retourne la date d'emprunt

    @date_emprunt.setter
    def date_emprunt(self, date_emprunt_2):
        self.__date_emprunt = date_emprunt_2  # Permet de modifier la date d'emprunt

    @property
    def date_retour(self):
        return self.__date_retour  # Retourne la date de retour du média

    @date_retour.setter
    def date_retour(self, date_retour_2):
        self.__date_retour = date_retour_2  # Permet de modifier la date de retour

    @property
    def identifiant(self):
        return self.__identifiant  # Retourne l'identifiant du média

    @property
    def titre(self):
        return self.__titre  # Retourne le titre du média

    @property
    def annee_parution(self):
        return self.__annee_parution  # Retourne l'année de parution du média

    @property
    def genre(self):
        return self.__genre  # Retourne le genre du média

    @property
    def disponible(self):
        return self.__disponible  # Retourne la disponibilité du média

    @disponible.setter
    def disponible(self, nouvelle_valeur):
        self.__disponible = nouvelle_valeur  # Permet de modifier la disponibilité du média (True ou False)

    # Méthode abstraite que toutes les sous-classes doivent implémenter
    @abstractmethod
    def afficher_media(self):
        # Cette méthode doit être définie dans les classes dérivées
        # Elle doit retourner des informations détaillées sur le média
        pass