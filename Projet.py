from termcolor import colored
import os

os.environ["FORCE_COLOR"] = "1"
from abc import ABC, abstractmethod

# Projet 1 / Gabriel Bertrand et Marius Séguin / 2025-03-21
# Système de Gestion de Médiathèque
# Contexte
"""
Vous êtes chargé(e) de développer un système de gestion pour une médiathèque municipale.
Cette application en ligne de commande permettra aux employés de gérer les différents types de
médias (livres, DVDs, CDs), les utilisateurs, ainsi que les emprunts et retours.
"""


class Mediatheque:
    """Classe sevant à la gestion globale du programme"""
    pass


class Medias(ABC):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible):
        self.__identifiant = identifiant
        self.__titre = titre
        self.__annee_parution = annee_parution
        self.__genre = genre
        self.__empruntable = disponible

    def get_identifiant(self):
        return self.__identifiant

    def get_titre(self):
        return self.__titre

    def get_annee_parution(self):
        return self.__annee_parution

    def get_genre(self):
        return self.__genre

    @abstractmethod
    def afficher_info(self):
        pass

    pass


class Livre(Medias):  # TODO vérifier si Empruntable est implanter
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, auteur, nombre_pages):
        super().__init__(identifiant, titre, annee_parution, genre, disponible)
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    def afficher_info(self):
        return f"Livre: {self.__titre} de {self.__auteur}, Genre: {self.__genre}, Pages: {self.__nombre_pages}"  # TODO get nombres pages avant et finir la ligne

    pass


class DVD(Medias):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, realisateur, duree_minutes):
        super().__init__(identifiant, titre, annee_parution, genre, disponible)
        self.__realisateur = realisateur
        self.__duree_minutes = duree_minutes

    pass


class CD(Medias):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, artiste, nombre_pistes):
        super().__init__(identifiant, titre, annee_parution, genre, disponible)
        self.__artiste = artiste
        self.__nombre_pistes = nombre_pistes

    pass


# Menu interactif
print(colored(" Bienvenue sur le site Web de Médiathèque.", "blue"))
while True:
    print(
        "\n Veuillez entrer le numéro de l'option souhaitée\n 0. Quitter le programme 1. Ajouter un média (livre, DVD ou CD)\n "
        "2. Rechercher des médias (par titre, genre, année, disponibilité)\n 3.Afficher les détails d'un média spécifique\n "
        "4.Ajouter un nouvel utilisateur\n 5. Emprunter un média\n 6. Retourner un média\n "
        "7. Afficher l'historique d'un utilisateur\n 8. Consulter les statistiques de la médiathèque")

    choix_action = input(">")
    if choix_action == "0":
        print("Il a été un plaisir de vous servir.Aure voir!")
        break
    elif choix_action == "1":
        pass
    elif choix_action == "2":
        pass
    elif choix_action == "3":
        pass
    elif choix_action == "4":
        pass
    elif choix_action == "5":
        pass
    elif choix_action == "6":
        pass
    elif choix_action == "7":
        pass
    else:
        print(colored("Vous avez entrer un choix inexistant ou invalide.Veuillez entrez un nombre entre 0 et 7", "red"))
