
#Create ingredient lists
chickenSoup = ['Chicken Soup', 'chicken', 'chicken broth', 'carrots', 'celery', 'noodles']
spaghettiRecipe = ['Spaghetti','spaghetti noodles', 'pasta sauce', 'meatballs']
grilledCheese = ['Grilled Cheese','bread', 'butter', 'cheese']
gardenSalad = ['Garden Salad','lettuce', 'cucumber', 'carrots', 'olives']
trinitySpecial = ["Trinity's Special",'bananas', 'sour cream', 'sugar', 'flour', 'vanilla extract']
groceryList = []

recipeList = [chickenSoup, spaghettiRecipe, grilledCheese, gardenSalad, trinitySpecial]

def print_recipe(desiredRecipe):
  print("\n", desiredRecipe, "ingredients include:\n")
  for recipe in recipeList:
    if desiredRecipe == recipe[0]:
      print(*recipe[1:], sep=", ")
      for i in recipe[1:]:
        groceryList.append(i)
  return groceryList


#Display options
print("What are you feeling like eating today?\n")
for recipe in recipeList:
  print(recipe[0])

#Ask for 1st recipe
desiredFood = input("\nEnter your desired meal: ")
print_recipe(desiredFood)

#Ask for 2nd recipe
secondFood = input("\nEnter your second recipe: ")
print_recipe(secondFood)

#Ask for additional grocery items
while True:
  x = input("\nWould you like to add more to your grocery list? (enter 'Done' when finished)")
  if x == "Done":
    break
  else:
    groceryList.append(x)
    pass

#Display grocery list
print('\nGrocery List: ')
print(*groceryList, sep=", ")