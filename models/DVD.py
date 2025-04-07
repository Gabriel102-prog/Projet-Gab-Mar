from models.Medias import Medias
from models.Empruntable import Empruntable
from datetime import datetime, timedelta

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
