# Obsluha vyjimek
## Krokovani
### Click to add a breakpoint - najet na cislo radku a kliknout na cervenou tecku (prvni prikaz , ktery neudela)
### Run - start debugging (F5) - select debugger (PYthon) - python file
#### Kontrola? --> variables - local - lines - neni tam avg_sales
### Tlacitko Step Over (F10) - pokracovat na dalsi radek

"""
lines = [
    "2904,4",
    "7390,7",
    "6950,8",
    "3300,4",
    "10570,8",
    "1310,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    line = line.split(",")
    avg = int(line[0]) / int(line[1])
    avg_sales.append(avg)

print(avg_sales)
"""
"""
lines = [
    "6950,0",
    "73907",
    2904,
    "3300;4",
    "10570,4,4",
    "a,2",
    "9806,8"]

avg_sales = []
for line in lines:
    line = line.split(",")
    try:
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except ZeroDivisionError:
        print("Délka směny nesmí být 0.")

print(avg_sales)
"""
"""
lines = [
    "6950,0",
    "73907",
    2904,
    "3300;4",
    "10570,4,4",
    "a,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    try:
        line = line.split(",")
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except Exception as e:
        print(f"Zpracování se nepodařilo kvůli chybě: {e}")

print(avg_sales)
"""

"""
lines = [
    "6950,0",
    "73907",
    2904,
    "3300;4",
    "10570,4,4",
    "a,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    try:
        line = line.split(",")
        if len(line) > 2:
            print("Na řádku mají být dvě hodnoty")
            avg_sales.append("chyba")
        else:
            avg = int(line[0]) / int(line[1])
            avg_sales.append(avg)
    except Exception as e:
        print(f"Zpracování se nepodařilo kvůli chybě: {e}")
        avg_sales.append("chyba")

print(avg_sales)
"""

"""
if len(line) > 2:
            print("Na řádku mají být dvě hodnoty")
            avg_sales.append("chyba")
            # raise Exception("Na řádku mají být dvě hodnoty")
        else:
            avg = int(line[0]) / int(line[1])
            avg_sales.append(avg)
"""

## Cviceni
### Knihy
knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
index = input("Zadej index knihy: ")
index = int(index)
print(knihy[index])

"""
value error a index error
"""


knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

try:
    index = input("Zadej index knihy: ")
    index = int(index)
    print(knihy[index])
except Exception:
    print("Nastala chyba")

### Knizni serie (bonus)