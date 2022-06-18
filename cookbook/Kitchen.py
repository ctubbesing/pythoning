from unicodedata import name
from xml.dom.minidom import NamedNodeMap


class Ingredient():
  def __init__(self, name, amount, units):
    self.name = name
    self.amount = amount
    self.units = units
  
  def printInfo(self):
    print("{ " + self.name + ": " + str(self.amount) + " " + self.units + " }")

class Recipe():
  def __init__(self, recipeName, ingredientsList, cookwareList, prepTime, cookTime, instructionsList):
    self.name = recipeName
    self.ingredientsList = ingredientsList
    self.cookwareList = cookwareList
    self.prepTime = prepTime
    self.cookTime = cookTime
    self.instructionsList = instructionsList

  def printInfo(self):
    print("{ " + self.name + ", Prep time: " + str(self.prepTime) + ", Cook time: " + str(self.cookTime)  + " }")
    for ingredient in self.ingredientsList:
      ingredient.printInfo()
    print(self.cookwareList)
    print(self.instructionsList)

