from Kitchen import Ingredient
from Kitchen import Pantry

def main():
  # create some ingredients
  carrots = Ingredient('carrot', 12, 'sticks')
  carrots.printInfo()
  milk = Ingredient('milk', 3, 'oz')
  milk.printInfo()
  
  # create pantry
  pantry = Pantry()
  print("\nAdding carrots to pantry...")
  pantry.addIngredient(carrots)
  pantry.printInfo()
  print("\nAdding milk to pantry...")
  pantry.addIngredient(milk)
  pantry.printInfo()
  print("\nAdding MORE carrots to pantry...")
  pantry.addIngredient(carrots)
  pantry.printInfo()
  # pantry.addIngredient(ingredientA)
  # pantry.addIngredient(ingredientA)

main()