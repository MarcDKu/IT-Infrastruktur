from __future__ import print_function, unicode_literals
from operator import index
import os
from prettytable import PrettyTable
from InquirerPy import prompt, inquirer
from pprint import pprint

# Konsole aufräumen


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def starting_window():
    cls()

    terminal_size = os.get_terminal_size()

    # Begrüßung
    print('Willkommen zum Kuchenbacken'.center(terminal_size.columns))
    print('Heute backen wir einen Frankfurter Kranz!'.center(terminal_size.columns))
    print('\n\n\n')


starting_window()

# Einkaufen


def shopping():
    print('Um diesen Kuchen backen zu können, benötigen wir Zutaten folgende Zutaten:\n')

    ingredients = {'Puddingpulver "Vanillegeschmack"': '1 Päckchen', 'Zucker': '275g', 'Milch': '500 ml + 5 EL', 'Butter': '400g', 'Salz': '1 Prise', 'Vanillin Zucker': '1 Päckchen', 'Eier': 4, 'Mehl': '500g',
                   'Speißestärke': '50g', 'Backulver': '1/2 Päckchen', 'Johannisbeergelee': '150g', 'Haselnuss-Krokant': '50g', 'Belegkirschen zum Verzieren': 'nach belieben', 'Fett und Mehl für die Form': ' ', 'Frischhaltefolie': ' '}

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

# Backen


def cooking():
    print('Um den kuchen richtig zu backen, folgen sie den Anweisungen:\n')
    steps = ["Buttercreme machen", "Teig zusammenrüheren",
         "Kuchen backen", "Schichten Stapeln", "Anrichten"]
    
    instructions = ['\n  Für die Buttercreme Puddingpulver, 75 g Zucker und 100 ml Milch glatt rühren.\n  400 ml Milch aufkochen, vom Herd ziehen.\n  Angerührtes Puddingpulver einrühren, unter Rühren wieder aufkochen und ca. 1 Minute köcheln.\n  Pudding in eine Schüssel geben, direkt mit Folie abdecken und bei Zimmertemperatur auskühlen lassen.\n  Den Backofen Vorheizen (E-Herd: 175 °C/Umluft: 150 °C/Gas: Stufe 2).',
                    '\n  250 g Butter bei Zimmertemperatur lagern.\n  Für den Teig 150 g Butter, Salz, 200 g Zucker und Vanillin-Zucker mit den Schneebesen des Handrührgerätes schaumig rühren.\n  Eier nacheinander unterrühren.\n  Mehl, Stärke und Backpulver mischen, abwechselnd mit 5 EL Milch unter die Fett-Ei-Creme rühren.',
                    '\n  Eine Frankfurter-Kranz-Form bzw. Ringform (1,4 Liter Inhalt; 22 cm Ø) gut fetten und mit Mehl ausstäuben.\n  Teig einfüllen und glatt streichen.\n  Im vorgeheizten Backofen (E-Herd: 175 °C/Umluft: 150 °C/Gas: Stufe 2) 30-40 Minuten backen.\n  Auf einem Kuchengitter leicht abkühlen lassen.\n  Aus der Form stürzen und vollständig auskühlen lassen.',
                    '\n  Bei Zimmertemperatur gelagerte Butter mit den Schneebesen des Handrührgerätes cremig weiß (ca. 15 Minuten) aufschlagen.\n  Pudding esslöffelweise nach und nach unterrühren.\n  Gelee glatt rühren.\n  Ausgekühlten Kuchen zweimal waagerecht durchschneiden.\n  Johannisbeergelee auf den unteren Boden streichen.\n  1/4 der Creme auf dem Gelee verteilen und glatt streichen.\n  Den zweiten Boden darauflegen und mit einem weiteren Viertel bestreichen.\n  Dritten Boden als Deckel darauflegen.',
                    '\n  Etwas Creme in einen Spritzbeutel mit Sterntülle füllen.\n  Rundherum mit der restliche Creme einstreichen.\n  Kranz mit Krokant bestreuen.\n  Restliche Creme als Tuffs auf den Kranz spritzen.\n  Kirschen halbieren, auf die Tuffs setzen.\n  Ca. 2 Stunden kalt stellen']

    while len(steps) > 0:
        selected_instructions = inquirer.rawlist(
            message="Wählen Sie den gewünschten Schritt aus:",
            choices=steps,
            default=1,
            multiselect=False
        ).execute()
        i = 0
        while type(selected_instructions) != int:
            if selected_instructions == steps[i]:
                selected_instructions = i
            else:
                i += 1

        shown_instructions = inquirer.confirm(
            message=instructions[selected_instructions],
            confirm_letter="‎",
            reject_letter="‎",
            transformer= lambda result: "‎Im" if result else "Schritt abgeschlossen",
        ).execute()
        steps.pop(selected_instructions)
        instructions.pop(selected_instructions)



shopping()
cooking()

