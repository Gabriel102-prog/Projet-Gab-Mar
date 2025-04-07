from models.Medias import Medias  # Import de la classe Medias depuis le module models. Medias
from models.Empruntable import Empruntable  # Import de la classe Empruntable depuis le module models. Empruntable
from datetime import datetime, timedelta  # Import de datetime et timedelta pour manipuler les dates


# La classe Livre hérite de Medias et Empruntable
class Livre(Medias, Empruntable):
    # Constructeur de la classe Livre, qui initialise tous les attributs nécessaires
    def __init__(self, identifiant, titre, annee_parution, genre, disponible, auteur, nombre_pages, date_retour,
                 date_emprunt):
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__auteur = auteur  # Auteur du livre
        self.__nombre_pages = nombre_pages  # Nombre de pages du livre

    # Propriété pour calculer la date de retour maximale (21 jours après l'emprunt)
    @property
    def date_retour_max(self):
        self.date_emprunt = datetime.now()  # Définit la date d'emprunt à la date actuelle
        return self.date_emprunt + timedelta(days=21)  # Retourne la date d'emprunt + 21 jours

    # Méthode pour emprunter le livre
    def emprunter(self):
        self.disponible = False  # Le livre devient indisponible
        self.date_emprunt = datetime.now()  # Met à jour la date d'emprunt avec la date actuelle
        print(
            f"Le Livre est disponible, vous l'avez emprunté.\nLa date limite de retour est le "
            f"{self.date_retour_max.day} {self.date_retour_max.strftime('%B')} {self.date_retour_max.year}")

    # Méthode pour retourner le livre
    def retourner(self):
        self.disponible = True  # Le livre devient disponible après le retour.
        self.date_retour = datetime.now()  # Enregistre la date du retour
        # Si la date de retour est avant ou égale à la date limite
        if self.date_retour_max >= self.date_retour:
            print("Merci d'avoir emprunté ce livre, à la prochaine.")
            return 0  # Aucune pénalité (retour à temps)
        else:
            # Si le livre est retourné en retard
            print("Attention, vous avez remis votre livre en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.date_retour).days} jours")
            return (self.date_retour_max - self.date_retour).days  # Retourne le nombre de jours de retard

    # Propriété pour obtenir le nombre de pages du livre
    @property
    def nombre_pages(self):
        return self.__nombre_pages

    # Propriété pour obtenir l'auteur du livre
    @property
    def auteur(self):
        return self.__auteur

    # Méthode pour afficher les informations du livre
    def afficher_media(self):
        if self.disponible:  # Vérifie si le livre est disponible
            v = "Ce Livre est disponible"
        else:
            v = "Ce Livre n'est pas disponible"
        # Retourne une chaîne de caractères détaillant les informations du livre
        return (f"Livre: {self.titre}, Auteur: {self.auteur}, Genre: {self.genre},\n"
                f"Nombre pages: {self.nombre_pages}, Année de parution: {self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {v}")