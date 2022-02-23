# pythoning
Just python practice stuffs

Ideas:
1. Recipe generation based on fridge inventory
   (Can include pictures and cool graphic options)
   - Ingredients
      - name: string
      - amount: number
      - units: string

   - Recipe
      - name: string
      - ingredients: Ingredient[]
      - cookware: string[]
      - prepTime: TimeSpan
      - cookTime: TimeSpan
      - instructions: string[]
   
   - Cookbook
      - title: string
      - recipes: Recipe[]
      - getAllAvailableRecipes(Pantry): Recipe[]
      - getRandomAvailableRecipe(Pantry): Recipe
      - addRecipe(Recipe): bool
      - deleteRecipe(string): bool
   
   - Pantry
      - ingredients: Ingredient[]
      - addIngredient(Ingredient): bool
      - subtractIngredient(Ingredient): bool


2. Interactive thing
   - Image manipulation and or graphics in general
   - Learn more about classes and objects
   
