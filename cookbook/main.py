from Kitchen import Ingredient, Recipe, Pantry

def main():
  # create some ingredients
  carrots = Ingredient('carrot', 12, 'sticks')
  carrots.printInfo()
  milk = Ingredient('milk', 3, 'oz')
  milk.printInfo()
  celery = Ingredient('celery', 3, 'sticks')
  
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
  print("\nSubtracting 5 carrots from pantry...")
  pantry.subtractIngredient('carrot', 5)
  pantry.printInfo()
  print("\nSubtracting 5 oz milk from pantry...")
  result = pantry.subtractIngredient('milk', 5)
  if result != -1:
    units = pantry.ingredientsDict['milk'].units
    print('ERROR: Insufficient funds. only ' + str(result) + ' ' + units + ' available.')
  pantry.printInfo()

  ingredientsList = [carrots, celery]
  recipeA = Recipe('A', ingredientsList, ['pan', 'bowl'], 300, 400, ['Do the thing to the food'])
  recipeA.printInfo()

main()