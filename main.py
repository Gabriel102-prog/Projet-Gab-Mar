from termcolor import colored
import os

os.environ["FORCE_COLOR"] = "1"
from models.Livre import Livre
from models.DVD import DVD
from models.CD import CD
from models.Utilisateur import Utilisateur
from models.Mediatheque import Mediatheque

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
                if mediatheque.calculer_nombre_medias == 0:
                    print(colored("Aucun média trouvé", "red"))
                else:
                    while True:
                        choix_media = int(
                            input("Quel média voulez vous emprunter ? (le premier :1, deuxième: 2, etc.):"))
                        if choix_media not in range(1, mediatheque.calculer_nombre_medias() + 1):
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
