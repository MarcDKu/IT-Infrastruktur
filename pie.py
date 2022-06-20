from __future__ import print_function, unicode_literals
import os
from prettytable import PrettyTable
from InquirerPy import prompt, inquirer
from pprint import pprint

#Konsole aufräumen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def starting_window():
    cls()

    terminal_size = os.get_terminal_size()

    #Begrüßung
    print('Willkommen zum Kuchenbacken'.center(terminal_size.columns))
    print('Heute backen wir einen Frankfurter Kranz!'.center(terminal_size.columns))
    print('\n\n\n')

starting_window()


#ingredients = {'Puddingpulver "Vanillegeschmack"' : '1 Päckchen', 'Zucker' : '275g', 'Milch' : '500 ml + 5 EL', 'Butter':'400g', 'Salz':'1 Prise', 'Vanillin Zucker':'1 Päckchen', 'Eier':4, 'Mehl':'500g', 'Speißestärke':'50g', 'Backulver':'1/2 Päckchen', 'Johannisbeergelee': '150g', 'Haselnuss-Krokant':'50g', 'Belegkirschen zum Verzieren': 'nach belieben', 'Fett und Mehl für die Form':' ', 'Frischhaltefolie':' '}
ingredients = ['1 Päckchen Puddingpulver "Vanillegeschmack"', '275g Zucker',  '500 ml + 5 EL Milch', '400g Butter', '1 Prise Salz', '1 Päckchen Vanillin Zucker', '4 Eier', '500g Mehl', '50g Speißestärke', '1/2 Päckchen Backulver', '150g Johannisbeergelee', '50g Haselnuss-Krokant', 'Belegkirschen zum Verzieren', 'Fett und Mehl für die Form', 'Frischhaltefolie']

#Einkaufen
def shopping(ingredients):
    print('Um diesen Kuchen backen zu können, benötigen wir Zutaten folgende Zutaten:\n')


    # table = PrettyTable(['Index', 'Menge', 'Zutat'])
    # table.align
    # counter = 1
    # for key in ingredients.keys():
    #     table.add_row([counter, ingredients[key], key])
    #     counter+=1

    # counter-=1

    # print(table)
    # print('Geben Sie den Index einer Zutat ein, die sie bereits besitzen:')
    # input = int(input()


    question1_choice = ingredients

    all_ingredients_gathered = False
    selected_ingredients=[]
    while all_ingredients_gathered == False:
        selected_ingredients = inquirer.checkbox(
            message="Zutaten bitte abhaken:",
            choices=question1_choice,
            cycle=False,
        ).execute()

        if len(selected_ingredients) < len(ingredients):
            leftover_ingredients = [x for x in ingredients if x not in selected_ingredients]
            ingredients = leftover_ingredients
            shopping(ingredients)
shopping(ingredients)