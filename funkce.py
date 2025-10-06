# Vlastní funkce
"""
Funkce nám umožňují program strukturovat do bloků a využívat stejný kód na více místech, 
aniž bychom ho museli kopírovat, např. round, int, len, print, input.
"""

result = round(12.5555)
print(result)

# def - definice funkce
# def + název fce a (parametr)
# přidat print()
# po fci dvojtečka
# python čte program postupně

def greet_user():
    print("Ahoj!")
greet_user()

def greet_user(name):
    print(f"Ahoj {name}!")
greet_user("Honzo")
greet_user("Zuzko")

def greet_user(language_code):
    if language_code == "cs":
        print("Ahoj!")
    elif language_code == "de":
        print("Hallo!")
    else:
        print("Hello!")
greet_user("cs")
greet_user("fr")

def divide_two_numbers(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        return "Nulou nelze dělit"
    
# Větev if
division_result = divide_two_numbers(120, 4)
print(division_result)
# Větev else
division_result_2 = divide_two_numbers(120, 0)
print(division_result_2)


def kilometry_na_mile(kilometry):
    return kilometry * 0.621371
def mile_na_kilometry(mile):
    return mile / 0.621371


def mile_na_kilometry(mile, namorni=False):
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852
london_oxford_km = mile_na_kilometry(59.7)
print(london_oxford_km)
belfast_new_york = mile_na_kilometry(2758.13, True)
print(belfast_new_york)

"""
File -> Preferences -> Settings
"python.analysis.typeCheckingMode"
"""

def mile_na_kilometry(mile, namorni: bool=False):
    # 0, "", [] se berou jako False
    # neprázdný řetězec, neprázdný seznam, nenulové číslo se berou jako True
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852

## Cvičení
### Násobení
"""
Napiš funkci mult, která bude mít dva číselné parametry. 
Funkce oba parametry vynásobí a vrátí výsledek.
"""
def mult(a, b):
    return a * b

vysledek = mult(4, 5)
print(vysledek)

### Funkce pro převody jednotek
"""
Začni vytvořením funkce kilometry_na_mile(kilometry) a mily_na_kilometry(mile),
které provedou převod mezi kilometry a mílemi.
"""
def celsia_na_fahrenheit(teplota):
    if teplota!=0:
        result=(teplota* 9/5) + 32
        return result
    elif teplota==0:
        return 30
    
print(celsia_na_fahrenheit(5))

### Měsíc narození (bonus)
"""
Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. 
Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
"""
def month_of_birth(birth_number: str) -> int:
    month = int(birth_number[2:4])
    if month > 12:
        month -= 50
    return month

print(month_of_birth("9207054439"))  # 7
print(month_of_birth("9555125899"))  # 5


### Rámeček (bonus)
"""
Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

Zadej slovo: ahoj
********
* ahoj *
********
"""


##