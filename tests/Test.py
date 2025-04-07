
from models.Livre import Livre
from models.DVD import DVD
from models.CD import CD
from models.Utilisateur import Utilisateur
from models.Mediatheque import Mediatheque
import pytest
from datetime import datetime


# Fixture pour initialiser les objets nécessaires pour les tests
@pytest.fixture
def setup_mediatheque():
    # Créer une instance de la médiathèque
    mediatheque = Mediatheque()

    # Créer des utilisateurs
    utilisateur1 = Utilisateur("U001", "Bertrand", "Gabriel", "gabriel@example.com")
    utilisateur2 = Utilisateur("U002", "Seguin", "Marius", "marius@example.com")

    # Ajouter des utilisateurs à la médiathèque
    mediatheque.ajouter_utilisateur(utilisateur1)
    mediatheque.ajouter_utilisateur(utilisateur2)

    # Créer des médias
    livre1 = Livre("L001", "Le Petit Prince", 1943, "Aventure", True, "Antoine de Saint-Exupéry", 96, None, None)
    dvd1 = DVD("D001", "Inception", 2010, "Science-Fiction", True, "Christopher Nolan", 148, None, None)
    cd1 = CD("C001", "Thriller", 1982, "Pop", True, "Michael Jackson", 9, None, None)

    # Ajouter des médias à la médiathèque
    mediatheque.ajouter_medias(livre1)
    mediatheque.ajouter_medias(dvd1)
    mediatheque.ajouter_medias(cd1)

    return mediatheque, utilisateur1, utilisateur2, livre1, dvd1, cd1


# Test de l'affichage des médias
def test_affichage_medias(setup_mediatheque):
    mediatheque, utilisateur1, utilisateur2, livre1, dvd1, cd1 = setup_mediatheque
    assert len(mediatheque.medias) == 3  # Vérifier qu'il y a 3 médias
    assert livre1.afficher_media() == "Livre: Le Petit Prince, Auteur: Antoine de Saint-Exupéry, Genre: Aventure,\n" \
                                      "Nombre pages: 96, Année de parution: 1943, Identifiant: L001, Disponibilité: Ce Livre est disponible"
    assert dvd1.afficher_media() == "DVD: Inception, Réalisateur: Christopher Nolan, Genre: Science-Fiction,\n" \
                                    "Durée: 148 minutes, Année de parution: 2010, Identifiant: D001, Disponibilité: Ce DVD est disponible"
    assert cd1.afficher_media() == "CD: Thriller, Artiste: Michael Jackson, Genre: Pop,\n" \
                                   "Nombre de pistes: 9, Année de parution: 1982, Identifiant: C001, Disponibilité: Ce CD est disponible"


# Test de l'emprunt de médias
def test_emprunt(setup_mediatheque):
    mediatheque, utilisateur1, utilisateur2, livre1, dvd1, cd1 = setup_mediatheque

    livre1.emprunter()
    assert not livre1.disponible  # Vérifier que le livre est maintenant emprunté
    assert livre1.date_emprunt is not None  # Vérifier que la date d'emprunt a été enregistrée
    assert livre1.date_retour_max > datetime.now()  # Vérifier que la date limite de retour est dans le futur

    dvd1.emprunter()
    assert not dvd1.disponible  # Vérifier que le DVD est maintenant emprunté
    assert dvd1.date_emprunt is not None  # Vérifier que la date d'emprunt a été enregistrée
    assert dvd1.date_retour_max > datetime.now()  # Vérifier que la date limite de retour est dans le futur

    cd1.emprunter()
    assert not cd1.disponible  # Vérifier que le CD est maintenant emprunté
    assert cd1.date_emprunt is not None  # Vérifier que la date d'emprunt a été enregistrée
    assert cd1.date_retour_max > datetime.now()  # Vérifier que la date limite de retour est dans le futur


# Test du retour des médias
def test_retour(setup_mediatheque):
    mediatheque, utilisateur1, utilisateur2, livre1, dvd1, cd1 = setup_mediatheque

    livre1.emprunter()
    livre1.retourner()  # Retourner le livre
    assert livre1.disponible is True  # Le livre devrait être disponible après le retour
    assert livre1.date_retour is not None  # Vérifier que la date de retour a été enregistrée

    dvd1.emprunter()
    dvd1.retourner()  # Retourner le DVD
    assert dvd1.disponible is True  # Le DVD devrait être disponible après le retour
    assert dvd1.date_retour is not None  # Vérifier que la date de retour a été enregistrée

    cd1.emprunter()
    cd1.retourner()  # Retourner le CD
    assert cd1.disponible is True  # Le CD devrait être disponible après le retour
    assert cd1.date_retour is not None  # Vérifier que la date de retour a été enregistrée


# Test de l'historique des utilisateurs
def test_historique_utilisateur(setup_mediatheque):
    mediatheque, utilisateur1, utilisateur2, livre1, dvd1, cd1 = setup_mediatheque

    # Emprunter des médias pour les utilisateurs
    utilisateur1.historique = {"Médias empruntés": []}
    utilisateur2.historique = {"Médias empruntés": []}

    # Ajouter des médias à l'historique des utilisateurs
    utilisateur1.historique["Médias empruntés"].append(livre1)
    utilisateur2.historique["Médias empruntés"].append(dvd1)
    utilisateur2.historique["Médias empruntés"].append(cd1)

    assert len(utilisateur1.historique["Médias empruntés"]) == 1  # Vérifier que l'utilisateur 1 a un emprunt
    assert len(utilisateur2.historique["Médias empruntés"]) == 2  # Vérifier que l'utilisateur 2 a deux emprunts

    assert livre1 in utilisateur1.historique[
        "Médias empruntés"]  # Vérifier que le livre est dans l'historique de l'utilisateur 1
    assert dvd1 in utilisateur2.historique[
        "Médias empruntés"]  # Vérifier que le DVD est dans l'historique de l'utilisateur 2
    assert cd1 in utilisateur2.historique[
        "Médias empruntés"]  # Vérifier que le CD est dans l'historique de l'utilisateur 2


# Test d'initialisation de la médiathèque
def test_initialisation_mediatheque(setup_mediatheque):
    mediatheque, utilisateur1, utilisateur2, livre1, dvd1, cd1 = setup_mediatheque
    assert len(mediatheque.utilisateurs) == 2  # Vérifier qu'il y a 2 utilisateurs dans la médiathèque
    assert len(mediatheque.medias) == 3  # Vérifier qu'il y a 3 médias dans la médiathèque