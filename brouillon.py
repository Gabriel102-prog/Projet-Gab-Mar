import locale

from termcolor import colored
import os
from datetime import datetime, timedelta

os.environ["FORCE_COLOR"] = "1"
from abc import ABC, abstractmethod

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

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
        self.__total_emprunts = 0
        self.__total_retours = 0

    @property
    def utilisateurs(self):
        return self.__utilisateurs

    @property
    def medias(self):
        return self.__medias

    @property
    def total_emprunts(self):
        """Retourne le nombre total d'emprunts"""
        return self.__total_emprunts

    @property
    def total_retours(self):
        """Retourne le nombre total de retours"""
        return self.__total_retours

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
            for e in range(len(self.__utilisateurs)):
                print(self.__utilisateurs[e])
        else:
            print("Aucun utilisateur n'est enregistré.")

    def afficher_nombres_utilisateurs(self):
        nombres_utilisateur = 0
        if len(self.__utilisateurs) > 0:
            for _ in range(len(self.__utilisateurs)):
                nombres_utilisateur += 1
            print(f"Il y a {nombres_utilisateur} utilisateurs enregistré.")
        else:
            print("Il n'y a aucun utilisateur enregistré.")

    def afficher_tous_medias(self):
        """Méthode pour afficher tous les médias"""
        if len(self.__medias) > 0:
            print("Liste des médias :")
            for media1 in self.__medias:
                print(media1.afficher_media())  # Affiche le résultat retourné par la méthode
        else:
            print("Aucun média n'est enregistré.")


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


class Livre(Medias, Empruntable):  # TODO vérifier si Empruntable est implanter
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, auteur, nombre_pages, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour,
                         date_emprunt)
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    @property
    def date_retour_max(self):
        self.date_emprunt = datetime.now()
        return self.date_emprunt + timedelta(days=21)

    def emprunter(self):
        self.disponible = False
        self.date_emprunt = datetime.now()
        print(
            f"Le Livre est disponible, vous l'avez emprunté.\nLa date limite de retour est le {self.date_retour_max.day} {self.date_retour_max.strftime("%B")} {self.date_retour_max.year}")

    def retourner(self):
        self.disponible = True
        self.date_retour = datetime.now()
        if self.date_retour_max >= self.date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # retourne le nb de jours de retard
        else:
            print("Attention, vous avez remis votre livre en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.date_retour).days} jours")
            return (self.date_retour_max - self.date_retour).days  # retourne le nb de jours de retard

    @property
    def nombre_pages(self):
        return self.__nombre_pages

    @property
    def auteur(self):
        return self.__auteur

    def afficher_media(self):
        if self.disponible:
            v = "Ce Livre est disponible"
        else:
            v = "Ce Livre n'est pas disponible"
        return (f"Livre: {self.titre}, Auteur: {self.auteur}, Genre: {self.genre},\n"
                f"Nombre pages: {self.nombre_pages}, Année de parution: {self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {v}")


class DVD(Medias, Empruntable):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, realisateur, duree_minutes, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__realisateur = realisateur
        self.__duree_minutes = duree_minutes

    @property
    def date_retour_max(self):
        self.date_emprunt = datetime.now()
        return self.date_emprunt + timedelta(days=14)

    def emprunter(self):
        self.disponible = False
        self.date_emprunt = datetime.now()
        print(
            f"Le DVD est disponible, vous l'avez emprunté.\nLa date limite de retour est le {self.date_retour_max.day} {self.date_retour_max.strftime("%B")} {self.date_retour_max.year}")

    def retourner(self):
        self.disponible = True
        self.date_retour = datetime.now()
        if self.date_retour_max >= self.date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # retourne le nb de jours de retard
        else:
            print("Attention, vous avez remis votre DVD en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.date_retour).days} jours")
            return (self.date_retour_max - self.date_retour).days  # retourne le nb de jours de retard

    @property
    def realisateur(self):
        return self.__realisateur

    @property
    def duree_minutes(self):
        return self.__duree_minutes

    def afficher_media(self):
        if self.disponible:
            v = "Ce DVD est disponible"
        else:
            v = "Ce DVD n'est pas disponible"
        return (f"DVD: {self.titre}, Réalisateur: {self.realisateur}, Genre: {self.genre},\n"
                f"Durée: {self.duree_minutes}, Année de parution:{self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponiblité: {v}")


class CD(Medias, Empruntable):
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, artiste, nombre_pistes, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__artiste = artiste
        self.__nombre_pistes = nombre_pistes

    @property
    def date_retour_max(self):
        self.date_emprunt = datetime.now()
        return self.date_emprunt + timedelta(days=14)

    def emprunter(self):
        self.disponible = False
        self.date_emprunt = datetime.now()
        print(
            f"Le CD est disponible, vous l'avez emprunté.\nLa date limite de retour est le {self.date_retour_max.day} {self.date_retour_max.strftime("%B")} {self.date_retour_max.year}")

    def retourner(self):
        self.disponible = True
        self.date_retour = datetime.now()
        if self.date_retour_max >= self.date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # retourne le nb de jours de retard
        else:
            print("Attention, vous avez remis votre CD en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.date_retour).days} jours")
            return (self.date_retour_max - self.date_retour).days  # retourne le nb de jours de retard

    @property
    def artiste(self):
        return self.__artiste

    @property
    def nombre_pistes(self):
        return self.__nombre_pistes

    def afficher_media(self):
        if self.disponible:
            v = "Ce CD est disponible"
        else:
            v = "Ce CD n'est pas disponible"
        return (f"CD: {self.titre}, Artiste: {self.artiste}, Genre: {self.genre},\n"
                f"Nombre de pistes: {self.nombre_pistes}, Année de parution:{self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {v}")


class Utilisateur:
    def __init__(self, identifiant, nom, prenom, email, historique=None):
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


def cree_identifiant(x):  # Todo commenter pouir dire utilisateur
    nombre = x + 1
    return f"U{str(nombre).zfill(8)}"


def cree_identifiant_livre(x):
    nombre = x + 1
    return f"L{str(nombre).zfill(8)}"


def cree_identifiant_dvd(x):
    nombre = x + 1
    return f"D{str(nombre).zfill(8)}"


def cree_identifiant_cd(x):
    nombre = x + 1
    return f"C{str(nombre).zfill(8)}"


mediatheque = Mediatheque()


def checher_media_selon_caracteristique():
    while True:
        liste_media = []
        print("Choisissez un critère de recherche :")
        print("1. Par titre")
        print("2. Par genre")
        print("3. Par année")
        print("4. Par disponibilité")
        w = 0
        critere_recherche = input(">").strip()
        if critere_recherche == "1":
            titre_recherche = input("Entrez le titre du média : ").lower()
            for y in mediatheque.medias:
                if titre_recherche in y.titre.lower():
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())
                    liste_media.append(y)

            if w == 0:
                print(colored("Aucun média trouvé avec ce titre.", "blue"))
            break
        elif critere_recherche == "2":
            genre_recherche = input("Entrez le genre du média : ").lower()
            for y in mediatheque.medias:
                if genre_recherche in y.genre.lower():
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())
                    liste_media.append(y)
            if w == 0:
                print(colored("Aucun média trouvé avec ce titre.", "blue"))
            break
        elif critere_recherche == "3":
            annee_recherche = input("Entrez l'année de parution du média : ")
            for y in mediatheque.medias:
                if str(y.annee_parution) == annee_recherche:
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())
                    liste_media.append(y)
            if w == 0:
                print(colored("Aucun média trouvé avec ce titre.", "blue"))
            break
        elif critere_recherche == "4":
            dispo_recherche = input("Le média est-il disponible ? (oui/non) : ").lower()
            dispo_bool = dispo_recherche == "oui"
            for y in mediatheque.medias:
                if y.disponible == dispo_bool:
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())
                    liste_media.append(y)
            if w == 0:
                print(colored("Aucun média trouvé avec ce titre.", "blue"))
            break
        if liste_media:
            return liste_media
        else:
            print(colored("Choix invalide, entrez une chiffre de 1 à 4", "red"))
            continue


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

    choix_action = input(">")
    if choix_action == "0":
        print("Il a été un plaisir de vous servir. Au revoir!")
        break
    elif choix_action == "1":
        while True:
            print("Entrer le numéro correspondant au médias que vous souhaiter entrer:"
                  "\n 1. Livre\n 2. DVD\n 3. CD")
            sorte_media = input(">")

            if sorte_media == "1":
                identifiant_identification = cree_identifiant_livre(nombre_livre)
                nombre_livre += 1
                titre_identification = input("Qu'elle est le titre du livre? :")
                annee_parution_identification = input("Qu'elle est l'année de parution du livre? :")
                genre_identification = input("Qu'elle est le genre du livre? :")
                auteur_identification = input("Qu'elle est l'auteur du livre? :")
                nombre_pages_identification = input("Qu'elle est le nombre de pages du livre? :")
                livre = Livre(identifiant_identification, titre_identification, annee_parution_identification,
                              genre_identification, True, auteur_identification, nombre_pages_identification,
                              None, None)
                mediatheque.ajouter_medias(livre)
                print(colored(f"L'identifiant du livre est maintenant :{identifiant_identification}", "blue"))
                break
            elif sorte_media == "2":
                identifiant_identification = cree_identifiant_dvd(nombre_dvd)
                nombre_dvd += 1
                titre_identification = input("Qu'elle est le titre du DVD? :")
                annee_parution_identification = input("Qu'elle est l'année de parution du DVD? :")
                genre_identification = input("Qu'elle est le genre du DVD? :")
                realisateur_identification = input("Qui est le réalisateur du DVD? :")
                duree_minutes_identification = input("Qu'elle est la durée du DVD? :")
                dvd = DVD(identifiant_identification, titre_identification, annee_parution_identification,
                          genre_identification, True, realisateur_identification, duree_minutes_identification
                          , None, None)
                mediatheque.ajouter_medias(dvd)
                print(colored(f"L'identifiant du DVD est maintenant :{identifiant_identification}", "blue"))
                break
            elif sorte_media == "3":
                identifiant_identification = cree_identifiant_cd(nombre_cd)
                nombre_cd += 1
                titre_identification = input("Qu'elle est le titre du CD? :")
                annee_parution_identification = input("Qu'elle est l'année de parution du CD? :")
                genre_identification = input("Qu'elle est le genre du CD? :")
                artiste_identification = input("Qui est l'artiste de ce CD? :")
                nombre_pistes_identification = input("Combien de piste à ce CD? :")
                cd = CD(identifiant_identification, titre_identification, annee_parution_identification,
                        genre_identification, True, artiste_identification, nombre_pistes_identification,
                        None, None)
                mediatheque.ajouter_medias(cd)
                print(colored(f"L'identifiant du CD est maintenant :{identifiant_identification}", "blue"))
                break
            else:
                print(colored("Vous avez entrer un choix inexistant ou invalide.Veuillez entrez un nombre entre "
                              "1 et 3", "red"))

    elif choix_action == "2":
        checher_media_selon_caracteristique()
    elif choix_action == "3":
        identifiant_media = input("Entrez l'identifiant du média : ").strip()
        media_trouve = False

        for media in mediatheque.medias:
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
                                  email_identification,
                                  {"Médias empruntés": [], "Médias retournés": [], "Frais de retard total": 0, })
        mediatheque.ajouter_utilisateur(utilisateur)
        print(colored(f"Votre identifiant est {identifiant_identification}", "blue"))
    elif choix_action == "5":
        while True:
            identifiant_emprunt = input("Qu'elle est votre identifiant? :")
            utilisateur_emprunt = None
            for i in mediatheque.utilisateurs:
                if i.identifiant == identifiant_emprunt:
                    utilisateur_emprunt = i
                    break
            if utilisateur_emprunt is None:
                print(colored("L'identifiant entré n'est pas reconnu dans la base de donnée", "red"))
                break
            else:
                liste_media = checher_media_selon_caracteristique()
                if len(liste_media) == 0:
                    print(colored("Aucun média trouvé", "red"))
                else:
                    while True:
                        choix_media = int(
                            input("Quel média voulez vous emprunter ? (le premier :1, deuxième: 2, etc.):"))
                        if choix_media not in [i + 1 for i in range(len(liste_media))]:
                            print(colored("option invalide veuillez recommencer", "red"))
                            continue
                        media_choisi = liste_media[choix_media - 1]
                        if not media_choisi.disponible:
                            print(colored("Le média que vous voulez emprunter est actuellement indisponible.", "blue"))
                            break
                        else:
                            media_choisi.emprunter()
                            utilisateur_emprunt.historique["Médias empruntés"].append(media_choisi)
                            break

    elif choix_action == "6":
        while True:
            identifiant_retour = input("Qu'elle est votre identifiant? :")
            utilisateur_retour = None
            for i in mediatheque.utilisateurs:
                if i.identifiant == identifiant_retour:
                    utilisateur_retour = i
                    break
            if utilisateur_retour is None:
                print(colored("L'identifiant entré n'est pas reconnu dans la base de donnée", "red"))
                break
            else:
                liste_emprunt = utilisateur_retour.historique["Médias empruntés"]
                if len(liste_emprunt) == 0:
                    print(colored("Aucun média emprunté", "red"))
                else:
                    while True:
                        q = 0
                        for p in liste_emprunt:
                            q += 1
                            print(f"{q}e emprunt :{liste_emprunt[p]}")
                        choix_emprunt = int(
                            input("Quel média voulez vous retourner ? (le premier :1, deuxième: 2, etc.):"))
                        if choix_emprunt not in [i + 1 for i in range(len(liste_emprunt))]:
                            print(colored("option invalide veuillez recommencer", "red"))
                            continue
                        media_choisi = liste_emprunt[choix_emprunt - 1]
                        nb_jours_retard = media_choisi.retourner()
                        frais_retard = nb_jours_retard * 0.25
                        utilisateur_retour.historique["Médias retournés"].append(media_choisi)
                        utilisateur_retour.historique["Frais de retard total"] += frais_retard
                        break
    elif choix_action == "7":
        while True:
            identifiant_historique = input("Qu'elle est votre identifiant? :")
            utilisateur_hisorique = None
            for i in mediatheque.utilisateurs:
                if i.identifiant == identifiant_historique:
                    utilisateur_hisorique = i
                    break
            if utilisateur_hisorique is None:
                print(colored("L'identifiant entré n'est pas reconnu dans la base de donnée", "red"))
                break
            print("Médias empruntés:")
            if not utilisateur_hisorique.historique["Médias empruntés"]:
                print(f"Aucun média n'a été emprunté par {utilisateur_hisorique.prenom} {utilisateur_hisorique.nom}.")
            else:
                for x in utilisateur_hisorique.historique["Médias empruntés"]:
                    print(x)

            print("Médias retournés:")
            if not utilisateur_hisorique.historique["Médias retournés"]:
                print(f"Aucun média n'a été retourné par {utilisateur_hisorique.prenom} {utilisateur_hisorique.nom}.")
            else:
                for x in utilisateur_hisorique.historique["Médias retournés"]:
                    print(x)
            print(
                f"Frais de retard total depuis la création de cet utilisateur: {utilisateur_hisorique.historique["Frais de retard total"]}$")

    elif choix_action == "8":
        print("Medias".center(60, "*"))
        nombre_livres = sum(1 for media in mediatheque.medias if isinstance(media, Livre))
        print(f"Il y a actuellement dans la médiathèque:\n- {nombre_livres} livre(s)")
        nombre_dvd = sum(1 for media in mediatheque.medias if isinstance(media, DVD))
        print(f"- {nombre_dvd} DVD(s)")
        nombre_cd = sum(1 for media in mediatheque.medias if isinstance(media, CD))
        print(f"- {nombre_cd} CD(s)1")
        total_medias = (nombre_livres + nombre_cd + nombre_dvd)
        print(f"Total des médias = {total_medias} ")
        print("Utilisateur".center(60, "*"))
        mediatheque.afficher_nombres_utilisateurs()
        print("Emprunt et retour".center(60, "*"))
        print(f"Il y a eu au total:\n- {mediatheque.total_emprunts} emprunts ")
        print(f"- {mediatheque.total_retours} retours ")

    elif choix_action == "9":
        mediatheque.afficher_tous_utilisateurs()
    elif choix_action == "10":
        mediatheque.afficher_tous_medias()
    else:
        print(
            colored("Vous avez entrer un choix inexistant ou invalide.Veuillez entrez un nombre entre 0 et 10", "red"))
