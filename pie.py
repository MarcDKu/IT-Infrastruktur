from __future__ import print_function, unicode_literals
from asyncio.windows_events import NULL
from multiprocessing.connection import wait
import os
import re
import time
from prettytable import PrettyTable
from InquirerPy import prompt, inquirer
from progress.bar import PixelBar


# Konsole aufräumen


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Einführung
def starting_window():
    cls()

    terminal_size = os.get_terminal_size()

    # Begrüßung
    print('Willkommen zum Kuchenbacken'.center(terminal_size.columns))
    print('Heute backen wir einen Frankfurter Kranz!'.center(terminal_size.columns))
    print('\n\n\n')

# Einkaufen


def shopping(ingredients):
    print('Navigation im Folgenden über die Pfeiltasten. Auswahl mir Leertaste und Bestätigen mit Enter')
    print('Um diesen Kuchen backen zu können, benötigen wir noch Zutaten folgende Zutaten:\n')

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
    selected_ingredients = []
    while all_ingredients_gathered == False:
        selected_ingredients = inquirer.checkbox(
            message="Zutaten bitte abhaken:",
            choices=question1_choice,
            cycle=False,
        ).execute()
        if len(selected_ingredients) < len(ingredients):
            leftover_ingredients = [
                x for x in ingredients if x not in selected_ingredients]
            ingredients = leftover_ingredients
            cls()
            print('Schöner Versuch, aber da fehlen noch %i Artikel' %
                  len(ingredients))
            shopping(ingredients)
        else:
            all_ingredients_gathered = True


# Backen
def cooking():
    print('Um den kuchen richtig zu backen, folgen sie den Anweisungen:\n')
    steps = ["Buttercreme machen", "Teig zusammenrüheren",
             "Kuchen backen", "Schichten Stapeln", "Anrichten"]

    instructions = ['Für die Buttercreme Puddingpulver, 75 g Zucker und 100 ml Milch glatt rühren.\n  400 ml Milch aufkochen, vom Herd ziehen.\n  Angerührtes Puddingpulver einrühren, unter Rühren wieder aufkochen und ca. ‎1 Minute köcheln.\nPudding in eine Schüssel geben, direkt mit Folie abdecken und bei Zimmertemperatur auskühlen lassen.\n  Den Backofen Vorheizen (E-Herd: 175 °C/Umluft: 150 °C/Gas: Stufe 2).',
                    '250 g Butter bei Zimmertemperatur lagern.\n  Für den Teig 150 g Butter, Salz, 200 g Zucker und Vanillin-Zucker mit den Schneebesen des Handrührgerätes schaumig rühren.\n  Eier nacheinander unterrühren.\n  Mehl, Stärke und Backpulver mischen, abwechselnd mit 5 EL Milch unter die Fett-Ei-Creme rühren.',
                    'Eine Frankfurter-Kranz-Form bzw. Ringform (1,4 Liter Inhalt; 22 cm Ø) gut fetten und mit Mehl ausstäuben.\n  Teig einfüllen und glatt streichen.\n  Im vorgeheizten Backofen (E-Herd: 175 °C/Umluft: 150 °C/Gas: Stufe 2) ‎35 Minuten backen.\nAuf einem Kuchengitter leicht abkühlen lassen.\n  Aus der Form stürzen und vollständig auskühlen lassen.',
                    'Bei Zimmertemperatur gelagerte Butter mit den Schneebesen des Handrührgerätes cremig weiß (ca. ‎15 Minuten) aufschlagen.\nPudding esslöffelweise nach und nach unterrühren.\n  Gelee glatt rühren.\n  Ausgekühlten Kuchen zweimal waagerecht durchschneiden.\n  Johannisbeergelee auf den unteren Boden streichen.\n  1/4 der Creme auf dem Gelee verteilen und glatt streichen.\n  Den zweiten Boden darauflegen und mit einem weiteren Viertel bestreichen.\n  Dritten Boden als Deckel darauflegen.',
                    'Etwas Creme in einen Spritzbeutel mit Sterntülle füllen.\n  Rundherum mit der restliche Creme einstreichen.\n  Kranz mit Krokant bestreuen.\n  Restliche Creme als Tuffs auf den Kranz spritzen.\n  Kirschen halbieren, auf die Tuffs setzen.\n  Ca. ‎120 Minuten kalt stellen. \nDer Kuchen kann jetzt serviert werden!']

    while len(steps) > 0:                                                                                               # Ausführen, solange nicht alle Schritte erledigt sind

        selected_instructions = inquirer.rawlist(                                                                       # Anzeigen der verscheidenen Schritte, welche noch erledigt werden müssen
            message="Wählen Sie den gewünschten Schritt aus:",
            choices=steps,
            default=1,
            multiselect=False
        ).execute()

        i = 0
        while type(selected_instructions) != int:                                                                       # Nach index von ausgewwähltem Wert suchen
            if selected_instructions == steps[i]:
                shownText = [instructions[i]]
                selected_instructions = i
                
            else:
                i += 1

            if instructions[i].find("Minute") != -1:                                                                   # Aufteilen des Texteiles in den Text vor der Zeiteingabe, der Zeitangabe selbst und dem Teil nach der Zeitangabe 
                shownText = [instructions[i][0:instructions[i].find("\n", instructions[i].find("Minute"))],
                            int(instructions[i][instructions[i].find("‎")+1:instructions[i].find(" Minute")]),
                            instructions[i][(instructions[i].find("\n", instructions[i].find("Minute"))+1):-1]]    
           
            if len(shownText) == 3:                                                                                    # Wenn Zeitangaben da sind, wird zuerst der Erste Text angezeigt, dannacht der Timer, und schließlich wieder Text  
                shown_instructions = inquirer.confirm(                                                                 
                    message=shownText[0],
                    confirm_letter="‎",
                    reject_letter="‎",
                    transformer=lambda result: "‎Im" if result else "Schritt abgeschlossen\n",
                ).execute()

                bar = PixelBar('  Warten sie, bis der Timer abgelaufen ist!', max=shownText[1])
                for i in range(shownText[1]):
                    time.sleep(1)
                    bar.next()
                bar.finish()

                shown_instructions = inquirer.confirm(  
                    message=shownText[2],
                    confirm_letter="‎",
                    reject_letter="‎",
                    transformer=lambda result: "‎Im" if result else "Schritt abgeschlossen\n",
                ).execute()

                shownText.clear
                cls()

            else:                                                                                                   # Ansonsten nur die Details anzeigen
                shown_instructions = inquirer.confirm( 
                    message=shownText[0],
                    confirm_letter="‎",
                    reject_letter="‎",
                    transformer=lambda result: "‎Im" if result else "Schritt abgeschlossen\n",
                ).execute()

        steps.pop(selected_instructions)  # Array kürzen
        instructions.pop(selected_instructions)
        cls()


# ------------------------------------------------------------------------------
# Logic
starting_window()
#ingredients = {'Puddingpulver "Vanillegeschmack"' : '1 Päckchen', 'Zucker' : '275g', 'Milch' : '500 ml + 5 EL', 'Butter':'400g', 'Salz':'1 Prise', 'Vanillin Zucker':'1 Päckchen', 'Eier':4, 'Mehl':'500g', 'Speißestärke':'50g', 'Backulver':'1/2 Päckchen', 'Johannisbeergelee': '150g', 'Haselnuss-Krokant':'50g', 'Belegkirschen zum Verzieren': 'nach belieben', 'Fett und Mehl für die Form':' ', 'Frischhaltefolie':' '}
ingredients = ['1 Päckchen Puddingpulver "Vanillegeschmack"', '275g Zucker',  '500 ml + 5 EL Milch', '400g Butter', '1 Prise Salz', '1 Päckchen Vanillin Zucker', '4 Eier', '500g Mehl',
               '50g Speißestärke', '1/2 Päckchen Backulver', '150g Johannisbeergelee', '50g Haselnuss-Krokant', 'Belegkirschen zum Verzieren', 'Fett und Mehl für die Form', 'Frischhaltefolie']
shopping(ingredients)
cooking()
