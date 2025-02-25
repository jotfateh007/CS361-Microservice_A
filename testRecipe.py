import time
def writeInitial(recipeParameters):
    with open("recipe.txt", 'w+') as recipe:
        recipe.write(", ".join(recipeParameters))


def getRecipe():
    with open("recipe.txt", 'r') as file:
        recipe = file.read().strip()
    return recipe

def main():
    recipeParameters = ['run', 'Polish', 'Main Course', 'Savory']
    writeInitial(recipeParameters)
    time.sleep(8)
    recipe = getRecipe()
    print(recipe)


if __name__ == "__main__":
    main()
