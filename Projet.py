from termcolor import colored
import os
from datetime import datetime, timedelta

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

    def __init__(self):
        self.__medias = []
        self.__utilisateurs = []
        self.__emprunts = []
        self.__total_emprunts = 0
        self.__total_retours = 0

    def ajouter_utilisateur(self, nouveau_utilisateur):
        """Méthode pour ajouter un article à la liste"""
        self.__utilisateurs.append(nouveau_utilisateur)

    def ajouter_medias(self, nouveau_medias):
        """Méthode pour ajouter un article à la liste"""
        self.__medias.append(nouveau_medias)

    def afficher_tous_utilisateurs(self):
        if len(self.__utilisateurs) > 0:
            print("Liste des utilisateurs :")
            print("nom       prénom")
            for i in range(len(self.__utilisateurs)):
                print(self.__utilisateurs[i])
        else:
            print("Aucun utilisateur n'est enregistré.")

    # TODO possible de réutiliser
    # def afficher_utilisateurs(self):
    #     """Méthode pour afficher tous les utilisateurs de la médiathèque"""
    #     if self.__utilisateurs:
    #         print("Liste des utilisateurs :")
    #         for utilisateur in self.__utilisateurs:
    #             print(f"{utilisateur.identifiant}: {utilisateur.nom} {utilisateur.prenom}")
    #     else:
    #         print("Aucun utilisateur enregistré.")


class Empruntable(ABC):
    @abstractmethod
    def date_retour_max(self):
        pass

    @abstractmethod
    def retourner(self):
        pass

    @abstractmethod
    def emprunter(self):
        pass


class Medias(ABC):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt):
        self.__identifiant = identifiant
        self.__titre = titre
        self.__annee_parution = annee_parution
        self.__genre = genre
        self.__disponible = disponible
        self.__date_retour = datetime.now
        self.__date_emprunt = date_emprunt
        self.__date_retour = date_retour

    @property
    def date_emprunt(self):
        return self.__date_emprunt

    @property
    def date_retour(self):
        return self.__date_retour

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


class Livre(Medias, Empruntable):  # TODO vérifier si Empruntable est implanter
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, auteur, nombre_pages, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour,
                         date_emprunt)
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__date_emprunt = date_emprunt

    @property
    def date_retour_max(self):
        self.__date_emprunt = datetime.now()
        return self.__date_emprunt + timedelta(days=21)

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            self.__date_emprunt = datetime.now()
            print("Le Livre est disponible, vous l'avez emprunté.")
        else:
            print("Le Livre que vous voulez emprunter est actuellement indisponible.")

    def retourner(self):
        self.__disponible = True
        self.__date_retour = datetime.now()
        if self.date_retour_max >= self.__date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # retourne le nb de jours de retard
        else:
            print("Attention, vous avez remis votre livre en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.__date_retour).days} jours")
            return (self.date_retour_max - self.__date_retour).days  # retourne le nb de jours de retard

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
        return (f"Livre: {self.titre}, Auteur: {self.auteur}, Genre: {self.genre},\n"
                f"Pages: {self.nb_pages}, Année de parution: {self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {i}")


class DVD(Medias):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, realisateur, duree_minutes, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__realisateur = realisateur
        self.__duree_minutes = duree_minutes
        self.__date_emprunt = date_emprunt

    @property
    def date_retour_max(self):
        self.__date_emprunt = datetime.now()
        return self.__date_emprunt + timedelta(days=14)

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            self.__date_emprunt = datetime.now()
            print("Le DVD est disponible, vous l'avez emprunté.")
        else:
            print("Le DVD que vous voulez emprunter est actuellement indisponible.")

    def retourner(self):
        self.__disponible = True
        self.__date_retour = datetime.now()
        if self.date_retour_max >= self.__date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # retourne le nb de jours de retard
        else:
            print("Attention, vous avez remis votre DVD en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.__date_retour).days} jours")
            return (self.date_retour_max - self.__date_retour).days  # retourne le nb de jours de retard

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
        return (f"DVD: {self.titre}, Réalisateur: {self.realisateur}, Genre: {self.genre},\n"
                f"Durée: {self.duree_minutes}, Année de parution:{self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponiblité: {i}")


class CD(Medias):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, artiste, nombre_pistes, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__artiste = artiste
        self.__nombre_pistes = nombre_pistes
        self.__date_emprunt = date_emprunt

    @property
    def date_retour_max(self):
        self.__date_emprunt = datetime.now()
        return self.__date_emprunt + timedelta(days=14)

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            self.__date_emprunt = datetime.now()
            print("Le CD est disponible, vous l'avez emprunté.")
        else:
            print("Le CD que vous voulez emprunter est actuellement indisponible.")

    def retourner(self):
        self.__disponible = True
        self.__date_retour = datetime.now()
        if self.date_retour_max >= self.__date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # retourne le nb de jours de retard
        else:
            print("Attention, vous avez remis votre CD en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.__date_retour).days} jours")
            return (self.date_retour_max - self.__date_retour).days  # retourne le nb de jours de retard

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
        return (f"CD: {self.titre}, Artiste: {self.artiste}, Genre: {self.genre},\n"
                f"Nombre de pistes: {self.nombre_pistes}, Année de parution:{self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {i}")


class Utilisateur:
    def __init__(self, identifiant, nom, prenom, email, historique={}):  # TODO voir le probleme
        self.__identifiant = identifiant
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__historique = historique

    @property
    def identifiant(self):
        return self.__identifiant

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def email(self):
        return self.__email

    @property
    def historique(self):
        return self.__historique


    def __str__(self):
        return f"{self.nom}, {self.prenom}"


# Menu interactif
print(colored(" Bienvenue sur le site Web de Médiathèque.", "blue"))
nombre_utilisateur = 0
nombre_livre = 0
nombre_dvd = 0
nombre_cd = 0


def cree_identifiant(nombre_utilisateurs):
    nombre = nombre_utilisateurs + 1
    return f"U{str(nombre).zfill(8)}"


def cree_identifiant_livre(nombre_livre):
    nombre = nombre_livre + 1
    return f"L{str(nombre).zfill(8)}"


def cree_identifiant_dvd(nombre_dvd):
    nombre = nombre_dvd + 1
    return f"D{str(nombre).zfill(8)}"


def cree_identifiant_cd(nombre_cd):
    nombre = nombre_cd + 1
    return f"C{str(nombre).zfill(8)}"


mediatheque = Mediatheque()
while True:
    print(
        "\n  Veuillez entrer le numéro de l'option souhaitée\n "
        " 0. Quitter le programme \n "
        " 1. Ajouter un média (livre, DVD ou CD)\n "
        " 2. Rechercher des médias (par titre, genre, année, disponibilité)\n "
        " 3. Afficher les détails d'un média spécifique\n "
        " 4. Ajouter un nouvel utilisateur\n "
        " 5. Emprunter un média\n "
        " 6. Retourner un média\n "
        " 7. Afficher l'historique d'un utilisateur\n "
        " 8. Consulter les statistiques de la médiathèque\n "
        " 9. Afficher tous les utilisateurs\n "
        "10. Afficher tous les médias")

    choix_action = input(">").strip
    if choix_action == "0":
        print("Il a été un plaisir de vous servir. Au revoir!")
        break
    elif choix_action == "1":
        while True:
            print("Entrer le numéro correspondant au médias que vous souhaiter entrer:"
                  "\n 1. Livre\n 2. DVD\n 3. CD")
            sorte_media = input(">").strip

            if sorte_media == "1":
                identifiant_identification = cree_identifiant_livre(nombre_livre)
                nombre_livre += 1
                titre_identification = input("Qu'elle est le titre du livre? :")
                annee_parution_identification = input("Qu'elle est l'année de parution du livre? :")
                genre_identification = input("Qu'elle est le genre du livre? :")
                auteur_identification = input("Qu'elle est l'auteur du livre? :")
                nombre_pages_identification = input("Qu'elle est le nombre de pages du livre? :")
                livre = Livre("a définir", titre_identification, annee_parution_identification,
                              genre_identification, True, auteur_identification, nombre_pages_identification)
                mediatheque.ajouter_medias(livre)
                print(f"L'identifiant du livre est maintenant :{identifiant_identification}")
                break
            elif sorte_media == "2":
                identifiant_identification = cree_identifiant_dvd(nombre_dvd)
                nombre_dvd += 1
                titre_identification = input("Qu'elle est le titre du DVD? :")
                annee_parution_identification = input("Qu'elle est l'année de parution du DVD? :")
                genre_identification = input("Qu'elle est le genre du DVD? :")
                realisateur_identification = input("Qui est le réalisateur du DVD? :")
                duree_minutes_identification = input("Qu'elle est la durée du DVD? :")
                dvd = DVD("a définir", titre_identification, annee_parution_identification,
                          genre_identification, True, realisateur_identification, duree_minutes_identification)
                mediatheque.ajouter_medias(dvd)
                print(f"L'identifiant du DVD est maintenant :{identifiant_identification}")
                break
            elif sorte_media == "3":
                identifiant_identification = cree_identifiant_cd(nombre_cd)
                nombre_cd += 1
                titre_identification = input("Qu'elle est le titre du CD? :")
                annee_parution_identification = input("Qu'elle est l'année de parution du CD? :")
                genre_identification = input("Qu'elle est le genre du CD? :")
                artiste_identification = input("Qui est l'artiste de ce CD? :")
                nombre_pistes_identification = input("Combien de piste à ce CD? :")
                cd = CD("a définir", titre_identification, annee_parution_identification,
                        genre_identification, True, artiste_identification, nombre_pistes_identification)
                mediatheque.ajouter_medias(cd)
                print(f"L'identifiant du CD est maintenant :{identifiant_identification}")
                break
            else:
                print(colored("Vous avez entrer un choix inexistant ou invalide.Veuillez entrez un nombre entre "
                              "1 et 3", "red"))

    elif choix_action == "2":
        print("Choisissez un critère de recherche :")
        print("1. Par titre")
        print("2. Par genre")
        print("3. Par année")
        print("4. Par disponibilité")
        critere_recherche = input(">").strip()

        if critere_recherche == "1":
            titre_recherche = input("Entrez le titre du média : ").lower()
            for media in mediatheque._Mediatheque__medias:
                if titre_recherche in media.titre.lower():
                    print(media.afficher_media())

        elif critere_recherche == "2":
            genre_recherche = input("Entrez le genre du média : ").lower()
            for media in mediatheque._Mediatheque__medias:
                if genre_recherche in media.genre.lower():
                    print(media.afficher_media())

        elif critere_recherche == "3":
            annee_recherche = input("Entrez l'année de parution du média : ")
            for media in mediatheque._Mediatheque__medias:
                if str(media.annee_parution) == annee_recherche:
                    print(media.afficher_media())

        elif critere_recherche == "4":
            dispo_recherche = input("Le média est-il disponible ? (oui/non) : ").lower()
            dispo_bool = dispo_recherche == "oui"
            for media in mediatheque._Mediatheque__medias:
                if media.disponible == dispo_bool:
                    print(media.afficher_media())
    elif choix_action == "3":
        identifiant_media = input("Entrez l'identifiant du média : ").strip()
        media_trouve = False

        for media in mediatheque._Mediatheque__medias:
            if media.identifiant == identifiant_media:
                print(media.afficher_media())
                media_trouve = True
                break

        if not media_trouve:
            print(colored("Média non trouvé. Vérifiez l'identifiant et essayez à nouveau.", "red"))

    elif choix_action == "4":
        # Entrée
        identifiant_identification = cree_identifiant(nombre_utilisateur)
        nombre_utilisateur += 1
        nom_identification = input("Qu'elle est votre nom? :")
        prenom_identification = input("Qu'elle est votre prenom? :")
        email_identification = input("Qu'elle est votre email? :")
        # Class
        utilisateur = Utilisateur(identifiant_identification, nom_identification, prenom_identification,
                                  email_identification, {})
        mediatheque.ajouter_utilisateur(utilisateur)
        print(f"Votre identifiant est {identifiant_identification}")
    elif choix_action == "5":
        pass
    elif choix_action == "6":
        pass
    elif choix_action == "7":
        pass
    elif choix_action == "8":
        pass
    elif choix_action == "9":
        mediatheque.afficher_tous_utilisateurs()
    elif choix_action == "10":
        pass
    else:
        print(
            colored("Vous avez entrer un choix inexistant ou invalide.Veuillez entrez un nombre entre 0 et 10", "red"))
