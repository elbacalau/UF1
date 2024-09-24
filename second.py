class Person:
    def __init__(self, firstname, lastname):
        self.abilities_list = []
        self.firstname = firstname
        self.lastname = lastname
        
    def add_ability(self, ability):
        self.abilities_list.append(ability)

class Candidate(Person):
    def __init__(self, firstname, lastname, gender):
        self.gender = gender
        super().__init__(firstname, lastname)
        
    def info(self):
        if self.gender == "male":
            print(f"He is {self.firstname} {self.lastname}.")
        else:
            print(f"She is {self.firstname} {self.lastname}.")
        
        if len(self.abilities_list) == 0:
            print("No te habilitats")
        else:
            print(self.abilities_list)

c1 = Candidate('Manel', 'Cantells', 'male')
c1.add_ability('Python')
c1.add_ability('Java')

c2 = Candidate('Maria', 'Girones', 'female')
c2.add_ability('PHP')

c1.info()
c2.info()