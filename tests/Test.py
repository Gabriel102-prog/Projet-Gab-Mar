
from models.Livre import Livre
from models.DVD import DVD
from models.CD import CD
from models.Utilisateur import Utilisateur
from models.Mediatheque import Mediatheque

# Création d'une instance de la médiathèque
mediatheque = Mediatheque()

# Ajout des utilisateurs
utilisateur1 = Utilisateur("U001", "Gabriel", "Bertrand", "gabriel@exemple.com",
                           {"Médias empruntés": [], "Médias retournés": [], "Frais de retard total": 0})
utilisateur2 = Utilisateur("U002", "Marius", "Séguin", "marius@exemple.com",
                           {"Médias empruntés": [], "Médias retournés": [], "Frais de retard total": 0})


mediatheque.ajouter_utilisateur(utilisateur1)
mediatheque.ajouter_utilisateur(utilisateur2)

# Ajout de médias (livres, DVD, CD)
livre1 = Livre("L001", "Le Petit Prince", 1943, "Aventure", True, "Antoine de Saint-Exupéry", 96, None, None)
dvd1 = DVD("D001", "Inception", 2010, "Science-Fiction", True, "Christopher Nolan", 148, None, None)
cd1 = CD("C001", "Thriller", 1982, "Pop", True, "Michael Jackson", 9, None, None)

mediatheque.ajouter_medias(livre1)
mediatheque.ajouter_medias(dvd1)
mediatheque.ajouter_medias(cd1)

# Variable pour suivre les tests
tests_reussis = 0
tests_echoues = 0


# Fonction pour tester l'affichage des médias
def tester_affichage_medias():
    global tests_reussis, tests_echoues
    print("\n=== Liste des médias avant l'emprunt ===")
    mediatheque.afficher_tous_medias()

    if len(mediatheque.medias) == 3:  # Vérifie que 3 médias ont été ajoutés
        tests_reussis += 1
        print("Test d'affichage des médias réussi.")
    else:
        tests_echoues += 1
        print("Test d'affichage des médias échoué.")


# Fonction pour tester l'emprunt des médias
def tester_emprunt():
    global tests_reussis, tests_echoues
    livre1.emprunter()
    dvd1.emprunter()
    cd1.emprunter()

    if livre1.disponible == False and dvd1.disponible == False and cd1.disponible == False:
        tests_reussis += 1
        print("Test d'emprunt des médias réussi.")
    else:
        tests_echoues += 1
        print("Test d'emprunt des médias échoué.")


# Fonction pour tester le retour des médias
def tester_retour():
    global tests_reussis, tests_echoues
    livre1.retourner()
    dvd1.retourner()
    cd1.retourner()

    if livre1.disponible == True and dvd1.disponible == True and cd1.disponible == True:
        tests_reussis += 1
        print("Test de retour des médias réussi.")
    else:
        tests_echoues += 1
        print("Test de retour des médias échoué.")


# Fonction pour tester l'historique des utilisateurs
def tester_historique_utilisateur():
    global tests_reussis, tests_echoues
    utilisateur1.historique["Médias empruntés"].append(livre1)
    utilisateur2.historique["Médias empruntés"].append(dvd1)

    if len(utilisateur1.historique["Médias empruntés"]) == 1 and len(utilisateur2.historique["Médias empruntés"]) == 1:
        tests_reussis += 1
        print("Test d'historique des utilisateurs réussi.")
    else:
        tests_echoues += 1
        print("Test d'historique des utilisateurs échoué.")


# Fonction pour afficher le résumé des tests
def afficher_resultats_tests():
    global tests_reussis, tests_echoues
    if tests_echoues == 0:
        print("\nTous les tests ont réussi ! Le programme fonctionne comme prévu.")
    else:
        print(f"\n{tests_reussis} test(s) réussi(s), {tests_echoues} test(s) échoué(s).")


# Exécution des tests
tester_affichage_medias()
tester_emprunt()
tester_retour()
tester_historique_utilisateur()

# Résumé des résultats
afficher_resultats_tests()