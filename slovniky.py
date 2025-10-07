# Další datové struktury
## Slovníky
item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}

# klíč (key): hodnota (value)
print(item["title"])

item_price = item["price"]
print(f"Vybraný produkt je {item['title']}")

item["weight"] = 0.9
print(item["weight"])

item["price"] = 599
print(item["price"])

item["weight"] = 0.9
if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není uvedená")

sklad = {"A1": "Čajová konvička s hrnky", "A2": "Zubní kartáček"}
if "Zubní kartáček" in sklad.values():
    print("Zubní kartáčky máme")
else:
    print("Zubní kartáčky nemáme")

my_key = "title"
print(item[my_key])

## Slovníky a cykly
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
for key in sales:
    # V proměnné je key je řetězec "Zločinný steh"
    print(key)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# Názvy proměnných si určujeme samy
# Do první proměnné uloží klíč, do druhé proměnné hodnotu
for key, value in sales.items():
    # V proměnné je key je řetězec "Zločinný steh"
    # V proměnné je value je číslo 2565
    print(f"Knihy {key} bylo prodáno {value} kusů.")

total = 0
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} kusů.")
    # total = value
    total = total + value
print(f"Celkem bylo prodáno {total} knih.")

total = 0
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} kusů.")
    # total = value
    total = total + value
print(f"Celkem bylo prodáno {total} knih.")

total = sum(sales.values())

## Dvourozměrné tabulky v Pythonu
#* více slovníků
#* uloženo v seznamu []

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

total = 0
for item in books:
    # 1. běh: item = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
    # 2. běh: item = {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019}
    # 3. běh: item = {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019}
    total = total + item["sold"] * item["price"]
print(total)

total = 0
for item in books:
    # 1. běh: item = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
    # 2. běh: item = {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019}
    # 3. běh: item = {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019}
    total = total + item["sold"] * item["price"]
print(total)

total = 0
for item in books:
    # 1. běh: item = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
    # 2. běh: item = {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019}
    # 3. běh: item = {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019}
    if item["year"] == 2019:
        total = total + item["sold"] * item["price"]
print(total)


## Cvičení
### Vysvědčení
vysvedceni = {"Český jazyk": 1, "Matematika": 2, "Dějepis": 3}
print(vysvedceni)

### Detektivky
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

#### Přidej do slovníku nově vydanou detektivku 
#### "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů
sales["Noc, která mě zabila"] = 0

#### U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.
sales["Vrah zavolá v deset"] += 100

print(sales)


### Tombola
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

#### Napiš program, který se nejprve zeptá uživatele na číslo
#### jeho lístku. Vstup uživatele si převeď na int!
cislo = int(input("Zadej číslo svého lístku: "))

#### Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text 
#### "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.
if cislo in tombola:
    print(f"Gratuluji, vyhráváš! 🎉: {tombola[cislo]}")
else:
    print("Bohužel nevyhráváš nic.")

print(cislo(7))

### Paranoidní večírek (bonus)
#### Seznam hostů a jejich hesel
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

#### Napiš program, který nejprve zkontroluje, zda je host na seznamu, 
#### a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. 
#### Hostu na seznamu, který zadá správné heslo, vypíše program text "Smíš vstoupit."
name = input("Zadej své jméno: ")
if name in passwords:
    password = input("Zadej své heslo: ")
    if password == passwords[name]:
        print("Smíš vstoupit.")
    else:
        print("Špatné heslo! Vstup zamítnut.")
else:
    print("Nejsi na seznamu hostů.")

### Vysvědčení 2
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

znamky = list(school_report.values())
prumer = sum(znamky) / len(znamky)
print(f"Průměrná známka je: {prumer:.2f}")

print("Předměty se známkou 1:")
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(f"- {predmet}")

#* další možná řešení
average_grade = sum(school_report.values()) / len(school_report)
print(f"Průměrná známka je {average_grade:.2f}")

import statistics

avg = statistics.mean(school_report.values())
print(f"Průměrná známka je {avg:.2f}")

print("Předměty, ze kterých student získla známku výborně: ")
for key, value in school_report.items():
    if value == 1:
        print(key)

### Čtenářský deník
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

celkem_stran = 0
for kniha in books:
    celkem_stran += kniha["pages"]

print(f"Celkový počet přečtených stran: {celkem_stran}")

knihy_s_vysokym_hodnocenim = 0
for kniha in books:
    if kniha["rating"] >= 8:
        knihy_s_vysokym_hodnocenim += 1

print(f"Počet knih s hodnocením alespoň 8: {knihy_s_vysokym_hodnocenim}")


#* další možná řešení
total_pages = sum(book["pages"] for book in books)
print(f"Celkový počet přečtených stran: {total_pages}")

favourite_books = [book for book in books if book["rating"] >= 8]
print(f"Počet knih s hodnocením alespoň 8: {len(favourite_books)}")

page_count = 0
favourite_books = 0
for item in books:
    page_count = page_count + item["pages"]
    if item["rating"] >= 8:
        favourite_books = favourite_books + 1

print(f"Gustav celkem přečetl {page_count} stran.")
print(f"Počet knih s hodnocením alespoň 8: {favourite_books}.")
