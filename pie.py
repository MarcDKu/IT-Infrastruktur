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

#Einkaufen
def shopping():
    print('Um diesen Kuchen backen zu können, benötigen wir Zutaten folgende Zutaten:\n')

    ingredients = {'Puddingpulver "Vanillegeschmack"' : '1 Päckchen', 'Zucker' : '275g', 'Milch' : '500 ml + 5 EL', 'Butter':'400g', 'Salz':'1 Prise', 'Vanillin Zucker':'1 Päckchen', 'Eier':4, 'Mehl':'500g', 'Speißestärke':'50g', 'Backulver':'1/2 Päckchen', 'Johannisbeergelee': '150g', 'Haselnuss-Krokant':'50g', 'Belegkirschen zum Verzieren': 'nach belieben', 'Fett und Mehl für die Form':' ', 'Frischhaltefolie':' '}

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

    slested_ingredients = inquirer.checkbox(
        message="Zutaten bitte abhaken:",
        choices=question1_choice,
        cycle=False,
    ).execute()

shopping()