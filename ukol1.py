"""
Kvíz z 1. lekce
V některých úkolech se vyskytuje seznam venecky, který vypadá takto:
venecky = [1, 2, 4, 1, 6, 0, 1]
"""

venecky = [1, 2, 4, 1, 6, 0, 1]

# Jaký bude výstup příkazu print(venecky[1])?
# print(venecky[1])

# Co vrátí příkaz venecky[:3]?
# print(venecky[:3])

# Jak můžeme změnit předposlední hodnotu seznamu venecky na 5?
# venecky[5] = 5
# venecky[-2] = 5
# print(venecky)

# Jaký typ chyby způsobí příkaz venecky[10]? (Zkus si tipnout podle názvů chyb nebo si zkus příkaz spustit a podívej se do terminálu.)
# print(venecky[10])
# IndexError: list index out of range

# K čemu v programu slouží moduly?
# Rozšíří možnosti našeho programu, protože nám umožní používat funkce a další nástroje, které vytvořil někdo jiný.

# Chceš pomocí svého programu vytvořit adresář (složku). Jaký modul by se na to hodil?
# To jsme si na lekci neříkali, ale můžeš si na této otázce vyzkoušet práci s umělou inteligencí, např. s ChatGPT. Poradí ti bezplatná verze.
# os

# Jak na hradíš řetězec TechStream v proměnné inzerat řetězcem NextGen Innovations?
# inzerat.replace("TechStream", "NextGen Innovations")

# U řetězců potřebujeme někdy ověřit, jestli se skládá pouze z čísel. K tomu slouží metoda isdecimal(). Jak ji správně použít?
# Můžeš si to vyzkoušet například na řetězci:
# jen_cisla = "10"
# print(jen_cisla.isdecimal())

# Které z následujících metod můžou změnit délku řetězce?
# strip()
# replace()

# Co je potřeba doplnit do podmínky, aby program fungoval?
# obr.:
"""
film = ["bla", 
        "bla2",
        "bla3",
        "bla4",
        "bla5"
        ]
cislo_filmu = int(input("zadej cislo filmu: "))
if __________:
    print(filmy[cislo_filmu])
else:
    print("tolik filmu nemame")
"""
# cislo_filmu < len(filmy)

# Máme řetězec s názvy měst:
# mesta = "Praha, Plzeň, Brno, Ostrava, Liberec"
# Který příkaz je podle tebe nejlepší na vytvoření seznamu, kde každé město bude samostatný prvek?
# mesta.split(", ")