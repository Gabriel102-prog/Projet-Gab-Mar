class Empruntable(ABC):
    @abstractmethod
    def date_retour_max(self):
        pass

    @abstractmethod
    def retourner(self):
        pass

    @abstractmethod
    def emprunter(self):
        pass