from abc import ABC, abstractmethod

class Empruntable(ABC):
    @abstractmethod
    def date_retour_max(self):
        """Retourne la date limite de retour du média emprunté."""
        pass

    @abstractmethod
    def retourner(self):
        """Méthode pour retourner le média emprunté."""
        pass

    @abstractmethod
    def emprunter(self):
        """Méthode pour emprunter un média."""
        pass