class Utilisateur:
    def __init__(self, identifiant, nom, prenom, email, historique=None):
        self.__identifiant = identifiant
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__historique = historique

    @property
    def identifiant(self):
        return self.__identifiant

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def email(self):
        return self.__email

    @property
    def historique(self):
        return self.__historique

    def __str__(self):
        return f"{self.nom}, {self.prenom}"