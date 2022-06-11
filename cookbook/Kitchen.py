class Ingredient():
  def __init__(self, name, amount, units):
    self.name = name
    self.amount = amount
    self.units = units
  
  def printInfo(self):
    print("{ " + self.name + ": " + str(self.amount) + " " + self.units + " }")

class Pantry():
  def __init__(self):
    self.ingredients = []
  
  def addIngredient(self, ingredient):
    self.ingredients += [ingredient]
  
  def printInfo(self):
    print("Pantry ingredients:")
    for ing in self.ingredients:
      ing.printInfo()