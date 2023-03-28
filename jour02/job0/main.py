class Person: 
    
    def __init__(self, firstName: str, name: str):
        self.name = name
        self.firstName = firstName
    
    @property
    def firstName(self):
        return self._firstName
    
    @firstName.setter
    def firstName(self, value):
        self._firstName = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    def sePresenter(self):
        print("Bonjour, je m'appelle " + self.name + " " + self.firstName)

lucien = Person("Lucien", "ZAK")
cartman = Person("Eric", "CARTMAN")
lucien.sePresenter()
lucien.firstName = "Lucienne"
lucien.sePresenter()
cartman.sePresenter()
print(lucien.firstName)