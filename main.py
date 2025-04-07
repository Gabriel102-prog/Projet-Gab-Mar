import locale
from termcolor import colored
import os

# Configuration de la locale pour la gestion des dates en français
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
# Force l'affichage en couleur dans le terminal
os.environ["FORCE_COLOR"] = "1"

# Importation des classes nécessaires
from models.Livre import Livre
from models.DVD import DVD
from models.CD import CD
from models.Utilisateur import Utilisateur
from models.Mediatheque import Mediatheque

# Message d'accueil pour l'utilisateur
print(colored(" Bienvenue sur le site Web de Médiathèque.", "blue"))

# Initialisation des variables de comptage
nombre_utilisateur = 0
nombre_livre = 0
nombre_dvd = 0
nombre_cd = 0


# Fonction pour créer un identifiant unique pour un utilisateur
def cree_identifiant(u):  # Todo: ajouter un commentaire pour expliquer que c'est pour l'utilisateur
    nombre = u + 1
    return f"U{str(nombre).zfill(8)}"  # Retourne l'identifiant formaté avec des zéros à gauche


# Fonction pour créer un identifiant unique pour un livre
def cree_identifiant_livre(d):
    nombre = d + 1
    return f"L{str(nombre).zfill(8)}"  # Identifiant formaté pour un livre


# Fonction pour créer un identifiant unique pour un DVD
def cree_identifiant_dvd(f):
    nombre = f + 1
    return f"D{str(nombre).zfill(8)}"  # Identifiant formaté pour un DVD


# Fonction pour créer un identifiant unique pour un CD
def cree_identifiant_cd(e):
    nombre = e + 1
    return f"C{str(nombre).zfill(8)}"  # Identifiant formaté pour un CD


# Création d'une instance de la classe Mediatheque
mediatheque = Mediatheque()


# Fonction pour rechercher un média selon un critère
def checher_media_selon_caracteristique():
    liste_media = []  # Liste pour stocker les médias trouvés
    while True:
        print("Choisissez un critère de recherche :")
        print("1. Par titre")
        print("2. Par genre")
        print("3. Par année")
        print("4. Par disponibilité")

        # Initialisation de la variable de comptage
        w = 0
        critere_recherche = input(">").strip()  # Récupère le choix de l'utilisateur

        if critere_recherche == "1":  # Recherche par titre
            titre_recherche = input("Entrez le titre du média : ").lower()  # Demande à l'utilisateur d'entrer un titre
            for y in mediatheque.medias:
                if titre_recherche in y.titre.lower():  # Si le titre recherché est trouvé
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())  # Affiche les informations du média trouvé
                    liste_media.append(y)  # Ajoute le média à la liste des résultats
            if w == 0:
                print(colored("Aucun média trouvé avec ce titre.", "blue"))  # Si aucun média n'est trouvé
            break
        elif critere_recherche == "2":  # Recherche par genre
            genre_recherche = input("Entrez le genre du média : ").lower()  # Demande à l'utilisateur d'entrer un genre
            for y in mediatheque.medias:
                if genre_recherche in y.genre.lower():  # Si le genre recherché est trouvé
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())  # Affiche les informations du média trouvé
                    liste_media.append(y)  # Ajoute le média à la liste des résultats
            if w == 0:
                print(colored("Aucun média trouvé avec ce genre.", "blue"))  # Si aucun média n'est trouvé
            break
        elif critere_recherche == "3":  # Recherche par année de parution
            annee_recherche = input(
                "Entrez l'année de parution du média : ")  # Demande à l'utilisateur d'entrer une année
            if not annee_recherche.isdigit():  # Vérifie si l'année entrée est un nombre
                continue
            for y in mediatheque.medias:
                if str(y.annee_parution) == annee_recherche:  # Si l'année correspond
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())  # Affiche les informations du média trouvé
                    liste_media.append(y)  # Ajoute le média à la liste des résultats
            if w == 0:
                print(colored("Aucun média trouvé avec cette année.", "blue"))  # Si aucun média n'est trouvé
            break
        elif critere_recherche == "4":  # Recherche par disponibilité
            dispo_recherche = input(
                "Le média est-il disponible ? (oui/non) : ").lower()  # Demande la disponibilité du média
            dispo_bool = dispo_recherche == "oui"  # Convertit la réponse en booléen
            for y in mediatheque.medias:
                if y.disponible == dispo_bool:  # Si la disponibilité correspond
                    w += 1
                    print(colored(f"{w}e média trouvé", "yellow"))
                    print(y.afficher_media())  # Affiche les informations du média trouvé
                    liste_media.append(y)  # Ajoute le média à la liste des résultats
            if w == 0:
                print(colored("Aucun média trouvé avec cette disponibilité.", "blue"))  # Si aucun média n'est trouvé
            break
        else:  # Si le choix de l'utilisateur est invalide
            print(colored("Choix invalide, entrez une chiffre de 1 à 4", "red"))
            continue  # Recommence la boucle si le choix est invalide
    return liste_media  # Retourne la liste des médias trouvés


# Boucle principale du programme qui permet à l'utilisateur de choisir différentes actions dans la médiathèque
while True:
    # Affichage du menu avec les options disponibles
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
        "10. Afficher tous les médias"
    )

    choix_action = input(">")  # Demande à l'utilisateur de choisir une option

    if choix_action == "0":
        # Si l'utilisateur choisit "0", le programme se termine
        print("Il a été un plaisir de vous servir. Au revoir!")
        break  # Sortie de la boucle et fin du programme

    elif choix_action == "1":
        # Option 1: Ajouter un nouveau média à la médiathèque
        while True:
            print("Entrer le numéro correspondant au média que vous souhaitez ajouter :"
                  "\n 1. Livre\n 2. DVD\n 3. CD")
            sorte_media = input(">")  # Demande à l'utilisateur de choisir le type de média à ajouter

            # Si l'utilisateur choisit "1", il ajoute un livre
            if sorte_media == "1":
                identifiant_identification = cree_identifiant_livre(
                    nombre_livre)  # Création de l'identifiant pour le livre
                nombre_livre += 1  # Incrémentation du nombre de livres dans la médiathèque
                titre_identification = input("Quel est le titre du livre? :")
                annee_parution_identification = input("Quel est l'année de parution du livre? :")
                genre_identification = input("Quel est le genre du livre? :")
                auteur_identification = input("Quel est l'auteur du livre? :")
                nombre_pages_identification = input("Quel est le nombre de pages du livre? :")

                # Création d'un objet Livre avec les informations saisies par l'utilisateur
                livre = Livre(identifiant_identification, titre_identification, annee_parution_identification,
                              genre_identification, True, auteur_identification, nombre_pages_identification,
                              None, None)
                mediatheque.ajouter_medias(livre)  # Ajout du livre à la médiathèque
                print(colored(f"L'identifiant du livre est maintenant :{identifiant_identification}", "blue"))
                break  # On sort de la boucle une fois le livre ajouté

            # Si l'utilisateur choisit "2", il ajoute un DVD
            elif sorte_media == "2":
                identifiant_identification = cree_identifiant_dvd(nombre_dvd)  # Création de l'identifiant pour le DVD
                nombre_dvd += 1  # Incrémentation du nombre de DVDs dans la médiathèque
                titre_identification = input("Quel est le titre du DVD? :")
                annee_parution_identification = input("Quel est l'année de parution du DVD? :")
                genre_identification = input("Quel est le genre du DVD? :")
                realisateur_identification = input("Qui est le réalisateur du DVD? :")
                duree_minutes_identification = input("Quel est la durée du DVD? :")

                # Création d'un objet DVD avec les informations saisies
                dvd = DVD(identifiant_identification, titre_identification, annee_parution_identification,
                          genre_identification, True, realisateur_identification, duree_minutes_identification
                          , None, None)
                mediatheque.ajouter_medias(dvd)  # Ajout du DVD à la médiathèque
                print(colored(f"L'identifiant du DVD est maintenant :{identifiant_identification}", "blue"))
                break  # On sort de la boucle une fois le DVD ajouté

            # Si l'utilisateur choisit "3", il ajoute un CD
            elif sorte_media == "3":
                identifiant_identification = cree_identifiant_cd(nombre_cd)  # Création de l'identifiant pour le CD
                nombre_cd += 1  # Incrémentation du nombre de CDs dans la médiathèque
                titre_identification = input("Quel est le titre du CD? :")
                annee_parution_identification = input("Quel est l'année de parution du CD? :")
                genre_identification = input("Quel est le genre du CD? :")
                artiste_identification = input("Qui est l'artiste de ce CD? :")
                nombre_pistes_identification = input("Combien de pistes à ce CD? :")

                # Création d'un objet CD avec les informations saisies
                cd = CD(identifiant_identification, titre_identification, annee_parution_identification,
                        genre_identification, True, artiste_identification, nombre_pistes_identification,
                        None, None)
                mediatheque.ajouter_medias(cd)  # Ajout du CD à la médiathèque
                print(colored(f"L'identifiant du CD est maintenant :{identifiant_identification}", "blue"))
                break  # On sort de la boucle une fois le CD ajouté

            else:
                # Si l'utilisateur entre un choix invalide
                print(colored("Vous avez entré un choix inexistant ou invalide. Veuillez entrer un nombre entre "
                              "1 et 3", "red"))

    elif choix_action == "2":
        # Option 2: Rechercher des médias dans la médiathèque selon certains critères
        checher_media_selon_caracteristique()  # Cette fonction permet de filtrer et rechercher des médias

    elif choix_action == "3":
        # Option 3: Afficher les détails d'un média spécifique en fonction de son identifiant
        identifiant_media = input("Entrez l'identifiant du média : ").strip()
        media_trouve = False  # Variable pour vérifier si le média a été trouvé

        # Recherche du média dans la liste de tous les médias de la médiathèque
        for media in mediatheque.medias:
            if media.identifiant == identifiant_media:  # Si l'identifiant du média correspond
                print(media.afficher_media())  # Affiche les détails du média
                media_trouve = True  # Indique que le média a été trouvé
                break  # On sort de la boucle une fois le média trouvé

        if not media_trouve:
            # Si le média n'a pas été trouvé avec l'identifiant fourni
            print(colored("Média non trouvé. Vérifiez l'identifiant et essayez à nouveau.", "red"))

    elif choix_action == "4":
        # Option 4 : Ajouter un nouvel utilisateur
        identifiant_identification = cree_identifiant(
            nombre_utilisateur)  # Création de l'identifiant pour l'utilisateur
        nombre_utilisateur += 1  # Incrémentation du nombre d'utilisateurs dans la médiathèque
        nom_identification = input("Quel est votre nom? :")
        prenom_identification = input("Quel est votre prénom? :")
        email_identification = input("Quel est votre email? :")

        # Création d'un objet Utilisateur avec les informations saisies
        utilisateur = Utilisateur(identifiant_identification, nom_identification, prenom_identification,
                                  email_identification,
                                  {"Médias empruntés": [], "Médias retournés": [], "Frais de retard total": 0, })
        mediatheque.ajouter_utilisateur(utilisateur)  # Ajout de l'utilisateur à la médiathèque
        print(colored(f"Votre identifiant est {identifiant_identification}", "blue"))

    elif choix_action == "5":
        # Option 5: Emprunter un média
        while True:
            identifiant_emprunt = input("Quel est votre identifiant? :")
            utilisateur_emprunt = None
            for i in mediatheque.utilisateurs:
                if i.identifiant == identifiant_emprunt:  # Recherche de l'utilisateur dans la médiathèque
                    utilisateur_emprunt = i
                    break
            if utilisateur_emprunt is None:
                # Si l'identifiant de l'utilisateur n'est pas trouvé
                print(colored("L'identifiant entré n'est pas reconnu dans la base de donnée", "red"))
                break  # On quitte la boucle
            else:
                liste_media1 = checher_media_selon_caracteristique()  # Recherche des médias disponibles à l'emprunt
                if mediatheque.calculer_nombre_medias == 0:
                    # Si aucun média n'est disponible
                    print(colored("Aucun média trouvé", "red"))
                else:
                    while True:
                        choix_media = int(
                            input("Quel média voulez-vous emprunter ? (le premier :1, deuxième: 2, etc.):"))
                        if choix_media < 1 or len(liste_media1) < choix_media:
                            # Si l'utilisateur entre un choix invalide
                            print(colored("Option invalide, veuillez recommencer", "red"))
                            continue
                        media_choisi = liste_media1[choix_media - 1]  # Choix du média à emprunter
                        if not media_choisi.disponible:
                            # Si le média choisi est déjà emprunté
                            print(colored("Le média que vous voulez emprunter est actuellement indisponible.", "blue"))
                            break
                        else:
                            mediatheque.total_emprunts += 1  # Incrémentation du nombre total d'emprunts
                            media_choisi.emprunter()  # Marque le média comme emprunté
                            utilisateur_emprunt.historique["Médias empruntés"].append(
                                media_choisi)  # Ajout de l'emprunt à l'historique
                            break  # On quitte la boucle une fois l'emprunt effectué
                    break  # On quitte la boucle externe après un emprunt réussi
    elif choix_action == "6":
        # Option 6 : Retourner un média emprunté
        while True:
            # Demande à l'utilisateur son identifiant pour retrouver son historique
            identifiant_retour = input("Quel est votre identifiant? :")
            utilisateur_retour = None

            # Recherche de l'utilisateur dans la liste des utilisateurs de la médiathèque
            for i in mediatheque.utilisateurs:
                if i.identifiant == identifiant_retour:
                    utilisateur_retour = i
                    break  # Si trouvé, on arrête la recherche

            if utilisateur_retour is None:
                # Si l'utilisateur n'est pas trouvé dans la base de données
                print(colored("L'identifiant entré n'est pas reconnu dans la base de donnée", "red"))
                break  # Quitte la boucle si l'identifiant est incorrect
            else:
                # Si l'utilisateur est trouvé, on vérifie s'il a des médias empruntés
                liste_emprunt = utilisateur_retour.historique["Médias empruntés"]
                if len(liste_emprunt) == 0:
                    # Si l'utilisateur n'a pas d'emprunt
                    print(colored("Aucun média emprunté", "red"))
                    break  # On quitte la boucle si aucun emprunt n'est effectué
                else:
                    # Si l'utilisateur a des emprunts
                    while True:
                        q = 0
                        # Affichage des médias empruntés par l'utilisateur
                        for p in range(len(liste_emprunt)):
                            q += 1
                            print(
                                f"{q}e emprunt :{liste_emprunt[p].afficher_media()}")  # Affiche les détails du média emprunté
                        choix_emprunt = int(
                            input("Quel média voulez-vous retourner ? (le premier :1, deuxième: 2, etc.):"))

                        # Vérification que le choix de l'utilisateur est valide
                        if choix_emprunt < 1 or len(liste_emprunt) < choix_emprunt:
                            print(colored("option invalide veuillez recommencer", "red"))
                            continue  # Redemande un choix valide

                        # Enregistrement du retour du média
                        mediatheque.total_retours += 1  # Incrémente le compteur des retours
                        media_choisi = liste_emprunt[choix_emprunt - 1]  # Récupère le média choisi
                        nb_jours_retard = media_choisi.retourner()  # Retourne le média et calcule les jours de retard
                        frais_retard = nb_jours_retard * 0.25  # Calcul des frais de retard
                        # Mise à jour de l'historique de l'utilisateur avec le média retourné et les frais de retard
                        utilisateur_retour.historique["Médias retournés"].append(media_choisi)
                        utilisateur_retour.historique["Frais de retard total"] += frais_retard
                        break  # Quitte la boucle une fois le retour effectué
                    break  # Quitte la boucle principale après un retour effectué

    elif choix_action == "7":
        # Option 7 : Afficher l'historique d'un utilisateur
        while True:
            # Demande à l'utilisateur son identifiant pour afficher son historique
            identifiant_historique = input("Quel est votre identifiant? :")
            utilisateur_hisorique = None

            # Recherche de l'utilisateur dans la liste des utilisateurs
            for i in mediatheque.utilisateurs:
                if i.identifiant == identifiant_historique:
                    utilisateur_hisorique = i
                    break  # Si trouvé, on arrête la recherche

            if utilisateur_hisorique is None:
                # Si l'utilisateur n'est pas trouvé dans la base de données
                print(colored("L'identifiant entré n'est pas reconnu dans la base de donnée", "red"))
                break  # Quitte la boucle si l'identifiant est incorrect
            else:
                # Si l'utilisateur est trouvé, on affiche son historique
                print("Médias empruntés:")
                if not utilisateur_hisorique.historique["Médias empruntés"]:
                    # Si l'utilisateur n'a pas emprunté de médias
                    print(
                        f"Aucun média n'a été emprunté par {utilisateur_hisorique.prenom} {utilisateur_hisorique.nom}.")
                else:
                    # Si l'utilisateur a des médias empruntés, on les affiche
                    for x in utilisateur_hisorique.historique["Médias empruntés"]:
                        print(x.afficher_media())  # Affiche les détails des médias empruntés

                print("Médias retournés:")
                if not utilisateur_hisorique.historique["Médias retournés"]:
                    # Si l'utilisateur n'a pas retourné de médias
                    print(
                        f"Aucun média n'a été retourné par {utilisateur_hisorique.prenom} {utilisateur_hisorique.nom}.")
                else:
                    # Si l'utilisateur a retourné des médias, on les affiche
                    for x in utilisateur_hisorique.historique["Médias retournés"]:
                        print(x.afficher_media())  # Affiche les détails des médias retournés

                # Affiche les frais de retard totaux de l'utilisateur
                print(f"Frais de retard total depuis la création de cet utilisateur: "
                      f"{utilisateur_hisorique.historique['Frais de retard total']}$")
                break  # Quitte la boucle après l'affichage de l'historique

    elif choix_action == "8":
        # Option 8 : Afficher les statistiques de la médiathèque
        print("Medias".center(60, "*"))
        # Calcul du nombre de livres, DVDs et CDs dans la médiathèque
        nombre_livres = sum(1 for media in mediatheque.medias if isinstance(media, Livre))
        print(f"Il y a actuellement dans la médiathèque:\n- {nombre_livres} livre(s)")

        nombre_dvd = sum(1 for media in mediatheque.medias if isinstance(media, DVD))
        print(f"- {nombre_dvd} DVD(s)")

        nombre_cd = sum(1 for media in mediatheque.medias if isinstance(media, CD))
        print(f"- {nombre_cd} CD(s)")

        # Calcul du nombre total de médias
        total_medias = (nombre_livres + nombre_cd + nombre_dvd)
        print(f"Total des médias = {total_medias}")

        print("Utilisateur".center(60, "*"))
        # Affichage du nombre total d'utilisateurs dans la médiathèque
        mediatheque.afficher_nombres_utilisateurs()

        print("Emprunt et retour".center(60, "*"))
        # Affichage du nombre total d'emprunts et de retours dans la médiathèque
        print(f"Il y a eu au total:\n- {mediatheque.total_emprunts} emprunts ")
        print(f"- {mediatheque.total_retours} retours ")

    elif choix_action == "9":
        # Option 9 : Afficher tous les utilisateurs
        mediatheque.afficher_tous_utilisateurs()  # Affiche la liste de tous les utilisateurs

    elif choix_action == "10":
        # Option 10 : Afficher tous les médias
        mediatheque.afficher_tous_medias()  # Affiche la liste de tous les médias dans la médiathèque

    else:
        # Si l'utilisateur entre un choix invalide
        print(
            colored("Vous avez entré un choix inexistant ou invalide. Veuillez entrer un nombre entre 0 et 10", "red"))