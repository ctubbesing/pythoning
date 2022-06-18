from unicodedata import name
from xml.dom.minidom import NamedNodeMap


class Ingredient():
  def __init__(self, name, amount, units):
    self.name = name.lower()
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

class Pantry():
  def __init__(self):
    self.ingredientsDict = {}
  
  def addIngredient(self, ingredient):
    if ingredient in self.ingredientsDict:
      self.ingredientsDict[ingredient.name].amount += ingredient.amount
    else:
      self.ingredientsDict[ingredient.name] = ingredient
  
  def subtractIngredient(self, name, amount):
    if name.lower() in self.ingredientsDict:
      ingredientCount = self.ingredientsDict[name.lower()].amount
      if ingredientCount > amount:
        self.ingredientsDict[name.lower()].amount -= amount
        return -1
      elif ingredientCount == amount:
        self.ingredientsDict.pop(name.lower())
        return -1
    return self.ingredientsDict[name.lower()].amount
  
  def printInfo(self):
    print("Pantry ingredients:")
    for ing in self.ingredientsDict:
      self.ingredientsDict[ing].printInfo()
