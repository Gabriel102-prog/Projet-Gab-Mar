from models.Medias import Medias  # Importation de la classe Medias pour que CD puisse l'hériter
from models.Empruntable import Empruntable  # Importation de la classe Empruntable pour l'implémentation de l'emprunt
from datetime import datetime, timedelta  # Importation des modules nécessaires pour la gestion de la date


class CD(Medias, Empruntable):
    """Classe représentant un CD, un type spécifique de média empruntable."""

    def __init__(self, identifiant, titre, annee_parution, genre, disponible, artiste, nombre_pistes, date_retour,
                 date_emprunt):
        """
        Constructeur de la classe CD. Il initialise les attributs de base du CD et appelle le constructeur de la classe Medias.

        :param identifiant: Identifiant unique du CD
        :param titre: Titre du CD
        :param annee_parution: Année de parution du CD
        :param genre: Genre du CD
        :param disponible: Indique si le CD est disponible pour l'emprunt
        :param artiste: Artiste interprète du CD
        :param nombre_pistes: Nombre de pistes sur le CD
        :param date_retour: Date limite de retour du CD
        :param date_emprunt: Date de l'emprunt
        """
        # Initialisation des propriétés de base à partir de la classe Medias
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__artiste = artiste  # Propriété spécifique au CD, l'artiste interprète
        self.__nombre_pistes = nombre_pistes  # Propriété spécifique au CD, le nombre de pistes

    @property
    def date_retour_max(self):
        """
        Calcule et retourne la date limite de retour du CD.
        La durée d'emprunt pour un CD est de 14 jours à partir de la date d'emprunt.

        :return: La date limite de retour du CD
        """
        self.date_emprunt = datetime.now()  # Met à jour la date d'emprunt à la date actuelle
        return self.date_emprunt + timedelta(days=14)  # Retourne la date limite (14 jours après l'emprunt)

    def emprunter(self):
        """
        Permet d'emprunter le CD.
        Cette méthode met à jour la disponibilité du CD, enregistre la date d'emprunt,
        et affiche un message avec la date limite de retour.
        """
        self.disponible = False  # Le CD devient indisponible après l'emprunt
        self.date_emprunt = datetime.now()  # Mise à jour de la date d'emprunt à la date actuelle
        print(
            f"Le CD est disponible, vous l'avez emprunté.\nLa date limite de retour est le {self.date_retour_max.day} {self.date_retour_max.strftime('%B')} {self.date_retour_max.year}")

    def retourner(self):
        """
        Permet de retourner le CD.
        Cette méthode met à jour la disponibilité du CD et la date de retour.
        Elle calcule également les jours de retard si la date de retour est dépassée.

        :return: Le nombre de jours de retard si le CD est retourné en retard, 0 sinon.
        """
        self.disponible = True  # Le CD devient disponible après le retour
        self.date_retour = datetime.now()  # Mise à jour de la date de retour à la date actuelle
        if self.date_retour_max >= self.date_retour:  # Si le CD est retourné avant ou à la date limite
            print("Merci d'avoir emprunté ce CD, à la prochaine.")
            return 0  # Retourne 0 jours de retard
        else:
            # Si le CD est retourné après la date limite
            print("Attention, vous avez remis votre CD en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.date_retour).days} jours")
            return (self.date_retour_max - self.date_retour).days  # Retourne le nombre de jours de retard

    @property
    def artiste(self):
        """
        Getter pour l'attribut 'artiste'. Retourne le nom de l'artiste du CD.
        """
        return self.__artiste

    @property
    def nombre_pistes(self):
        """
        Getter pour l'attribut 'nombre_pistes'. Retourne le nombre de pistes sur le CD.
        """
        return self.__nombre_pistes

    def afficher_media(self):
        """
        Affiche les informations détaillées sur le CD : titre, artiste, genre, nombre de pistes,
        année de parution, identifiant et disponibilité.

        :return: Une chaîne de caractères avec les informations du CD.
        """
        if self.disponible:
            v = "Ce CD est disponible"
        else:
            v = "Ce CD n'est pas disponible"
        # Retourne une chaîne formatée contenant toutes les informations du CD
        return (f"CD: {self.titre}, Artiste: {self.artiste}, Genre: {self.genre},\n"
                f"Nombre de pistes: {self.nombre_pistes}, Année de parution: {self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {v}")