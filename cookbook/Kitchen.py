class Ingredient():
  def __init__(self, name, amount, units):
    self.name = name
    self.amount = amount
    self.units = units
  
  def printInfo(self):
    print("{ " + self.name + ": " + str(self.amount) + " " + self.units + " }")