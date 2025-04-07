from models.Medias import Medias  # Importation de la classe Medias pour que DVD puisse l'hériter
from models.Empruntable import Empruntable  # Importation de la classe Empruntable pour l'implémentation de l'emprunt
from datetime import datetime, timedelta  # Importation des modules nécessaires pour la gestion de la date


class DVD(Medias, Empruntable):
    """Classe représentant un DVD, un type spécifique de média empruntable."""

    def __init__(self, identifiant, titre, annee_parution, genre, disponible, realisateur, duree_minutes, date_retour,
                 date_emprunt):
        """
        Constructeur de la classe DVD. Il initialise les attributs de base du DVD et appelle le constructeur de la classe Medias.

        :param identifiant: Identifiant unique du DVD
        :param titre: Titre du DVD
        :param annee_parution: Année de parution du DVD
        :param genre: Genre du DVD
        :param disponible: Indique si le DVD est disponible pour l'emprunt
        :param realisateur: Réalisateur du DVD
        :param duree_minutes: Durée du DVD en minutes
        :param date_retour: Date limite de retour du DVD
        :param date_emprunt: Date de l'emprunt
        """
        # Initialisation des propriétés de base à partir de la classe Medias
        super().__init__(identifiant, titre, annee_parution, genre, disponible, date_retour, date_emprunt)
        self.__realisateur = realisateur  # Propriété spécifique au DVD, le réalisateur
        self.__duree_minutes = duree_minutes  # Propriété spécifique au DVD, la durée en minutes

    @property
    def date_retour_max(self):
        """
        Calcule et retourne la date limite de retour du DVD.
        La durée d'emprunt pour un DVD est de 14 jours à partir de la date d'emprunt.

        :return: La date limite de retour du DVD
        """
        self.date_emprunt = datetime.now()  # Met à jour la date d'emprunt à la date actuelle
        return self.date_emprunt + timedelta(days=14)  # Retourne la date limite (14 jours après l'emprunt)

    def emprunter(self):
        """
        Permet d'emprunter le DVD.
        Cette méthode met à jour la disponibilité du DVD, enregistre la date d'emprunt,
        et affiche un message avec la date limite de retour.
        """
        self.disponible = False  # Le DVD devient indisponible après l'emprunt
        self.date_emprunt = datetime.now()  # Mise à jour de la date d'emprunt à la date actuelle
        print(
            f"Le DVD est disponible, vous l'avez emprunté.\nLa date limite de retour est le {self.date_retour_max.day} {self.date_retour_max.strftime('%B')} {self.date_retour_max.year}")

    def retourner(self):
        """
        Permet de retourner le DVD.
        Cette méthode met à jour la disponibilité du DVD et la date de retour.
        Elle calcule également les jours de retard si la date de retour est dépassée.

        :return: Le nombre de jours de retard si le DVD est retourné en retard, 0 sinon.
        """
        self.disponible = True  # Le DVD devient disponible après le retour
        self.date_retour = datetime.now()  # Mise à jour de la date de retour à la date actuelle
        if self.date_retour_max >= self.date_retour:  # Si le DVD est retourné avant ou à la date limite
            print("Merci d'avoir emprunté ce DVD, à la prochaine.")
            return 0  # Retourne 0 jours de retard
        else:
            # Si le DVD est retourné après la date limite
            print("Attention, vous avez remis votre DVD en retard.")
            print(f"Jours de retard: {(self.date_retour_max - self.date_retour).days} jours")
            return (self.date_retour_max - self.date_retour).days  # Retourne le nombre de jours de retard

    @property
    def realisateur(self):
        """
        Getter pour l'attribut 'realisateur'. Retourne le nom du réalisateur du DVD.
        """
        return self.__realisateur

    @property
    def duree_minutes(self):
        """
        Getter pour l'attribut 'duree_minutes'. Retourne la durée du DVD en minutes.
        """
        return self.__duree_minutes

    def afficher_media(self):
        """
        Affiche les informations détaillées sur le DVD : titre, réalisateur, genre, durée,
        année de parution, identifiant et disponibilité.

        :return: Une chaîne de caractères avec les informations du DVD.
        """
        if self.disponible:
            v = "Ce DVD est disponible"
        else:
            v = "Ce DVD n'est pas disponible"
        # Retourne une chaîne formatée contenant toutes les informations du DVD
        return (f"DVD: {self.titre}, Réalisateur: {self.realisateur}, Genre: {self.genre},\n"
                f"Durée: {self.duree_minutes} minutes, Année de parution: {self.annee_parution}, "
                f"Identifiant: {self.identifiant}, Disponibilité: {v}")
