class Mediatheque:
    """Classe servant à la gestion globale du programme"""

    def __init__(self):
        # Initialisation des attributs
        self.__medias = []  # Liste pour stocker les médias (livres, DVDs, etc.)
        self.__utilisateurs = []  # Liste pour stocker les utilisateurs
        self.__emprunts = []  # Liste pour suivre les emprunts
        self.__total_emprunts = 0  # Nombre total d'emprunts
        self.__total_retours = 0  # Nombre total de retours

    # Propriétés pour accéder aux données
    @property
    def utilisateurs(self):
        """Retourne la liste des utilisateurs"""
        return self.__utilisateurs

    @property
    def medias(self):
        """Retourne la liste des médias"""
        return self.__medias

    @property
    def total_emprunts(self):
        """Retourne le nombre total d'emprunts"""
        return self.__total_emprunts

    @total_emprunts.setter
    def total_emprunts(self, total_emprunts2):
        """Met à jour le nombre total d'emprunts"""
        self.__total_emprunts = total_emprunts2

    @property
    def total_retours(self):
        """Retourne le nombre total de retours"""
        return self.__total_retours

    @total_retours.setter
    def total_retours(self, total_retours2):
        """Met à jour le nombre total de retours"""
        self.__total_retours = total_retours2

    # Méthodes pour ajouter des utilisateurs et des médias
    def ajouter_utilisateur(self, nouveau_utilisateur):
        """Ajoute un utilisateur à la liste des utilisateurs"""
        self.__utilisateurs.append(nouveau_utilisateur)

    def ajouter_medias(self, nouveau_medias):
        """Ajoute un média à la liste des médias"""
        self.__medias.append(nouveau_medias)

    # Méthodes pour afficher les utilisateurs et les médias
    def afficher_tous_utilisateurs(self):
        """Affiche la liste de tous les utilisateurs"""
        if len(self.__utilisateurs) > 0:
            print("Liste des utilisateurs :")
            print("Nom       Prénom")
            for e in self.__utilisateurs:
                print(e)  # Affiche chaque utilisateur
        else:
            print("Aucun utilisateur n'est enregistré.")

    def afficher_nombres_utilisateurs(self):
        """Affiche le nombre total d'utilisateurs"""
        nombres_utilisateur = len(self.__utilisateurs)
        if nombres_utilisateur > 0:
            print(f"Il y a {nombres_utilisateur} utilisateurs enregistrés.")
        else:
            print("Il n'y a aucun utilisateur enregistré.")

    def afficher_tous_medias(self):
        """Affiche la liste de tous les médias"""
        if len(self.__medias) > 0:
            print("Liste des médias :")
            for media in self.__medias:
                print(media.afficher_media())  # Affiche le résultat retourné par la méthode afficher_media()
        else:
            print("Aucun média n'est enregistré.")

    def calculer_nombre_medias(self):
        """Retourne le nombre total de médias dans la médiathèque"""
        return len(self.__medias)