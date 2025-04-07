
class Mediatheque:
    """Classe sevant à la gestion globale du programme"""

    def __init__(self):
        self.__medias = []
        self.__utilisateurs = []
        self.__emprunts = []
        self.__total_emprunts = 0
        self.__total_retours = 0

    @property
    def utilisateurs(self):
        return self.__utilisateurs

    @property
    def medias(self):
        return self.__medias

    @property
    def total_emprunts(self):
        """Retourne le nombre total d'emprunts"""
        return self.__total_emprunts

    @property
    def total_retours(self):
        """Retourne le nombre total de retours"""
        return self.__total_retours

    def ajouter_utilisateur(self, nouveau_utilisateur):
        """Méthode pour ajouter un article à la liste"""
        self.__utilisateurs.append(nouveau_utilisateur)

    def ajouter_medias(self, nouveau_medias):
        """Méthode pour ajouter un article à la liste"""
        self.__medias.append(nouveau_medias)

    def afficher_tous_utilisateurs(self):
        if len(self.__utilisateurs) > 0:
            print("Liste des utilisateurs :")
            print("nom       prénom")
            for e in range(len(self.__utilisateurs)):
                print(self.__utilisateurs[e])
        else:
            print("Aucun utilisateur n'est enregistré.")

    def afficher_nombres_utilisateurs(self):
        nombres_utilisateur = 0
        if len(self.__utilisateurs) > 0:
            for _ in range(len(self.__utilisateurs)):
                nombres_utilisateur += 1
            print(f"Il y a {nombres_utilisateur} utilisateurs enregistré.")
        else:
            print("Il n'y a aucun utilisateur enregistré.")

    def afficher_tous_medias(self):
        """Méthode pour afficher tous les médias"""
        if len(self.__medias) > 0:
            print("Liste des médias :")
            for media1 in self.__medias:
                print(media1.afficher_media())  # Affiche le résultat retourné par la méthode
        else:
            print("Aucun média n'est enregistré.")
