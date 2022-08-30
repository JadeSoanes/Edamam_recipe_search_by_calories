import requests
import json

# function connecting to api

def recipe_search(ingredient):
    app_id = '2ce04194'
    app_key = '884c0755cdc7675a9bc6a788c0f4dcd1'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

# function asking user to input an ingredient and the maximum number of calories they want

def run():
    ingredient = input('Enter an ingredient: ')
    max_calories = float(input('Enter the maximum number of calories desired: '))
    results = recipe_search(ingredient)
# function to print the recipe name, link and calories each time
    def output():
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['calories'])
        print()
# for loop to categorise recipe into suitable, potentially suitable (within 100 cals) and unsuitable recipes
    for result in results:
        recipe = result['recipe']
        if recipe['calories'] < max_calories:
            print('Suitable recipe!')
            output()
        elif recipe['calories'] <= max_calories + 100:
            print('Recipe potentially suitable')
            output()
        else:
            print('Unsuitable recipe :(')
            output()


run()



