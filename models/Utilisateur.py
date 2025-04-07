class Utilisateur:
    # Constructeur de la classe, initialise un utilisateur avec ses informations personnelles
    def __init__(self, identifiant, nom, prenom, email, historique=None):
        self.__identifiant = identifiant  # Identifiant unique de l'utilisateur
        self.__nom = nom  # Nom de l'utilisateur
        self.__prenom = prenom  # Prénom de l'utilisateur
        self.__email = email  # Adresse email de l'utilisateur
        self.__historique = historique if historique is not None else []  # Historique des actions (emprunts) de l'utilisateur

    # Getter pour l'identifiant de l'utilisateur (c'est une propriété qui permet d'accéder à l'attribut)
    @property
    def identifiant(self):
        return self.__identifiant

    # Getter pour le nom de l'utilisateur
    @property
    def nom(self):
        return self.__nom

    # Getter pour le prénom de l'utilisateur
    @property
    def prenom(self):
        return self.__prenom

    # Getter pour l'email de l'utilisateur
    @property
    def email(self):
        return self.__email

    # Getter pour l'historique des actions de l'utilisateur (par exemple les médias empruntés)
    @property
    def historique(self):
        return self.__historique

    @historique.setter
    def historique(self, value):
        self.__historique = value

    # Méthode pour afficher l'utilisateur sous une forme plus lisible
    def __str__(self):
        # Retourne une chaîne de caractères formatée avec le nom et prénom de l'utilisateur
        return f"{self.nom}, {self.prenom}"