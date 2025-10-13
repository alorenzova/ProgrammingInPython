# Máme následující slovník:
#item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
# Která z podmínek je vyhodnocená jako pravda?
#* if "title" in item:

# Co platí o slovníku?
#obedy = {"Jirka": "salat", "Kuba": "nudle", "Míša": "nudle"}
#* Jeho délka je 3

# Jak zjistíme, co měl k obědu Jirka?
#* print(obedy["Jirka"])

# Jaký bude výsledek programu níže?
"""
pozice = {"Lenka": "testerka", "Lucka": "analytička"}
print(pozice["Petra"])
"""
#* Skončí chybou KeyError

# Co je potřeba doplnit do programu
"""
pozice = {"Lenka": "testerka", "Lucka": "analytička"}
if ____:
    print(pozice["Petra"])
else:
    print("Petru v seznamu nemáme")
"""
#* "Petra" in pozice

# Jak bude vypadat slovník pozice?
pozice = {"Lenka": "testerka", "Lucka": "analytička"}
nova_kolegyne = "Petra"
pozice[nova_kolegyne] = "vývojářka"
print(pozice)
#* Ke klíči "Petra" se uloží hodnota "vývojářka". Lenka a Lucka zůstanou

# Jaké dvě chyby obsahuje program?
"""
obedy = {"Jirka": "salat", "Kuba": "nudle", "Míša": "nudle"}
for jmeno, jidlo in obedy:
    print("{jmeno} měl(a) k obědu {jidlo}.")
"""
#* Před řetězcem ve funkci print chybí "f"
#* Ve druhém řádku by mělo být obedy.items()

# Co vypíše následující program
random_dict = {
    "jablko": "červené",
    "pes": "štěká",
    "dům": "velký",
    "auto": "rychlé"
}

random_dict.pop("pes")
print(len(random_dict))

# Následující program obsahuje seznam cvičení, která čekají na konkrétního studenta nebo studentku v rámci kurzu programování. 
# Jaký řádek v programu chybí, aby byl v proměnné remaining_exercises počet cvičení, která je třeba ještě dokončit?
excercises = [
    {
        "topic": "Variables & Types",
        "difficulty": "Easy",
        "completed": True
    },
    {
        "topic": "Methods",
        "difficulty": "Medium",
        "completed": False
    },
    {
        "topic": "Functions",
        "difficulty": "Medium",
        "completed": False
    },
]
remaining_excercises = 0
for item in excercises:
    # sem doplň řádek --> if item["completed"] == False:
        remaining_excercises = remaining_excercises + 1
print(remaining_excercises)
#* if item["completed"] == False:

# Nyní vytváříme program, který spočítá celkový čas potřebný na vyřešení všech cvičení. Odhadujeme, 
# že cvičení s jednoduchou obtížností zabere 2 hodiny a cvičení se střední obtížností 5 hodin. 
# Jaký řádek je potřeba doplnit do programu, abychom v proměnné total_hours měli odhadovanou časovou náročnost všech cvičení?
excercises = [
    {
        "topic": "Variables & Types",
        "difficulty": "Easy",
        "completed": True
    },
    {
        "topic": "Methods",
        "difficulty": "Medium",
        "completed": False
    },
    {
        "topic": "Functions",
        "difficulty": "Medium",
        "completed": False
    },
]
hours_per_excercise = {
        "Easy": 2,
        "Medium": 5
}
total_hours = 0
for item in excercises:
    difficulty = item["difficulty"]
    # sem doplň řádek --> total_hours = total_hours + hours_per_excercise[difficulty]
print(total_hours)
#* total_hours = total_hours + hours_per_exercise[difficulty]

# Jaký řádek je potřeba do programu doplnit, aby vypsal názvy filmů, které hrají v alespoň jednom kině?
filmy = [
      {"nazev": "Catch Me If You Can", "zeme": "USA", "rok_vyroby": 2002, "kina": 127},
      {"nazev": "Inception", "zeme": "USA", "rok_vyroby": 2010, "kina": 0},
      {"nazev": "Amelie", "zeme": "Francie", "rok_vyroby": 2001, "kina": 45},
      {"nazev": "The King's Speech", "zeme": "Velka Britanie", "rok_vyroby": 2010, "kina": 0},
      {"nazev": "Pan's Labyrinth", "zeme": "Spanelsko", "rok_vyroby": 2006, "kina": 89},
      {"nazev": "Das Boot", "zeme": "Nemecko", "rok_vyroby": 1981, "kina": 156},
]
for film in filmy:
#      __________
        print(film["nazev"])
#* if film["kina"] > 0: