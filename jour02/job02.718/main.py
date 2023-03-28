class Personne:
    def __init__(self, firstName: str, name: str):
        self.name = name
        self.firstName = firstName


class Auteur(Personne):
    oeuvres: list = []

    def __init__(self, firstName: str, name: str, oeuvres: list = []):
        super().__init__(firstName, name)
        self.oeuvres = oeuvres

    def ecrireUnLivre(self, titre: str):
        self.oeuvres.append(Livre(titre, self))

    def listerOeuvres(self):
        for livre in self.oeuvres:
            print(livre.print)


class Livre:
    def __init__(self, titre: str, Auteur: Auteur):
        self.auteur = Auteur
        self.titre = titre

    @property
    def print(self):
        return self.titre


class Client(Personne):
    collection: Livre = {}

    def __init__(self, firstName: str, name: str):
        super().__init__(firstName, name)

    def inventaire(self):
        for livre in self.collection:
            print(livre.print + ": " + str(self.collection[livre]) + " exemplaires")


class Bibliotheque:
    def __init__(self, nom: str, livres: dict = {Livre: int}):
        self.nom = nom
        self.livres = livres

    def acheterUnLivre(self, livre: Livre, quantite: int):
        self.livres[livre] -= quantite

    def inventaire(self):
        for livre in self.livres:
            print(livre.print + ": " + str(self.livres[livre]) + " exemplaires")

    def louerUnLivre(self, livre: Livre, client: Client):
        self.livres[livre] -= 1
        client.collection[livre] = 1

    def rendreLivre(self, client: Client):
        for livre in client.collection:
            self.livres[livre] += 1
        client.collection = {}


auteur1 = Auteur("Lucien", "ZAK")
auteur1.ecrireUnLivre("Le livre de Lucien")
auteur1.ecrireUnLivre("Le livre de Lucien 2")
bibliotheque1 = Bibliotheque(
    "Bibliotheque1", {auteur1.oeuvres[0]: 20, auteur1.oeuvres[1]: 10}
)

client1 = Client("Eric", "CARTMAN")
bibliotheque1.louerUnLivre(auteur1.oeuvres[0], client1)

bibliotheque1.rendreLivre(client1)
client1.inventaire()
