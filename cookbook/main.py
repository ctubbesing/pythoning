from Kitchen import Ingredient, Recipe

def main():
  ingredientA = Ingredient('carrot', 12, 'sticks')
  ingredientB = Ingredient('celery', 3, 'sticks')
  #ingredientA.printInfo()
  ingredientsList = [ingredientA, ingredientB]
  recipeA = Recipe('A', ingredientsList, ['pan', 'bowl'], 300, 400, ['Do the thing to the food'])
  recipeA.printInfo()

main()