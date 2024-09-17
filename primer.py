class Pare:
    def __init__(self, firstName, lastName):
      self.firstName = firstName
      self.lastName = lastName
      
    
    def getDadFirstName(self):
        return f"El nom del pare es: {self.firstName}"
    
    
    def getDadFullName(self):
        return f"Nom complet Pare: {self.firstName} {self.lastName}"


class Mare:
    def __init__(self, firstName, lastName):
      self.firstName = firstName
      self.lastName = lastName
      
    
    def getMomFirstName(self):
        return f"El nom de la mare es: {self.firstName}"
    
    
    def getMomFullName(self):
        return f"Nom complet Mare: {self.firstName} {self.lastName}"



class Child(Mare, Pare):
    def __init__(self, firstNameFill, firstNamePare, lastNamePare, firstNameMom, lastNameMom):
      self.firstNameFill = firstNameFill
      self.firstNamePare = firstNamePare
      self.lastNamePare = lastNamePare
      self.firstNameMom = firstNameMom
      self.lastNameMom = lastNameMom
      
      
      Pare.__init__(self, firstNamePare, lastNamePare)
      Mare.__init__(self, firstNameMom, lastNameMom)
      
      
    def getFullName(self):
        return f"El meu nom complet es {self.firstNameFill} {self.lastNamePare} {self.lastNameMom}"
    



child = Child("Oriol", "Josep", "Reverte", "Joana", "Martinez")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())
