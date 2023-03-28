class Personne:
    def __init__(self, firstName: str, name: str):
        self.name = name
        self.firstName = firstName

class Auteur(Personne):

    oeuvres: list = []

    def __init__(self, firstName: str, name: str, oeuvres: list = []):
        super().__init__(firstName, name)
        self.oeuvres = oeuvres
    
    def ecrireUnLivre(self, titre: str) -> None:
        self.oeuvres.append(Livre(titre, self))
    
    def listerOeuvres(self) -> None:
        for livre in self.oeuvres:
            print(livre.print)

class Livre: 
    def __init__(self, titre: str, Auteur: Auteur) -> None: 
        self.auteur = Auteur
        self.titre = titre

    @property
    def print(self) -> str:
        return self.titre

auteur1 = Auteur("Lucien", "ZAK")
auteur1.ecrireUnLivre("Le livre de Lucien")
auteur1.ecrireUnLivre("Le livre de Lucien 2")
auteur1.listerOeuvres()
