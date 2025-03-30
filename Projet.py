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
        self.__disponible = disponible

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


class Livre(Medias):  # TODO vérifier si Empruntable est implanter
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, auteur, nombre_pages):
        super().__init__(identifiant, titre, annee_parution, genre, disponible)
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    @property
    def nb_pages(self):
        return self.__nombre_pages

    @property
    def auteur(self):
        return self.__auteur

    def afficher_media(self):
        if Livre.disponible:
            i = "Ce Livre est disponible"
        else:
            i = "Ce Livre n'est pas disponible"
        return f"Livre: {Livre.titre}, Auteur: {Livre.auteur}, Genre: {Livre.genre},\nPages: {Livre.nb_pages}, Année de parution: {Livre.annee_parution}, Identifiant: {Livre.identifiant}, Disponibilité: {i}"


class DVD(Medias):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, realisateur, duree_minutes):
        super().__init__(identifiant, titre, annee_parution, genre, disponible)
        self.__realisateur = realisateur
        self.__duree_minutes = duree_minutes

    @property
    def realisateur(self):
        return self.__realisateur

    @property
    def duree_minutes(self):
        return self.__duree_minutes

    def afficher_media(self):
        if DVD.disponible:
            i = "Ce DVD est disponible"
        else:
            i = "Ce DVD n'est pas disponible"
        return f"DVD: {DVD.titre}, Réalisateur: {DVD.realisateur}, Genre: {DVD.genre},\nDurée: {DVD.duree_minutes}, Année de parution:{DVD.annee_parution}, Identifiant: {DVD.identifiant}, Disponiblité: {i}"


class CD(Medias):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, artiste, nombre_pistes):
        super().__init__(identifiant, titre, annee_parution, genre, disponible)
        self.__artiste = artiste
        self.__nombre_pistes = nombre_pistes

    @property
    def artiste(self):
        return self.__artiste

    @property
    def nombre_pistes(self):
        return self.__nombre_pistes

    def afficher_media(self):
        if CD.disponible:
            i = "Ce CD est disponible"
        else:
            i = "Ce CD n'est pas disponible"
        return f"CD: {CD.titre}, Artiste: {CD.artiste}, Genre: {CD.genre},\nNombre de pistes: {CD.nombre_pistes}, Année de parution:{CD.annee_parution}, Identifiant: {CD.identifiant}, Disponibilité: {i}"



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
