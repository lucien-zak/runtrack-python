class Person: 
    
    def __init__(self, firstName: str, name: str) -> None:
        self.name = name
        self.firstName = firstName
    
    @property
    def firstName(self) -> str:
        return self._firstName
    
    @firstName.setter
    def firstName(self, value) -> None:
        self._firstName = value
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value) -> None:
        self._name = value
    
    def sePresenter(self) -> None:
        print("Bonjour, je m'appelle " + self.name + " " + self.firstName)

lucien = Person("Lucien", "ZAK")
cartman = Person("Eric", "CARTMAN")
lucien.sePresenter()
lucien.firstName = "Lucienne"
lucien.sePresenter()
cartman.sePresenter()
print(lucien.firstName)