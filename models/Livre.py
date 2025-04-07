from models.Medias import Medias
from models.Empruntable import Empruntable
from datetime import datetime, timedelta

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