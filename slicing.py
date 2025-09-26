# seznamy
venecky = [5, 3, 2, 1, 2, 1, 9]

print(venecky[0])

venecky_vsedni_dny = venecky[0:5]
print(venecky_vsedni_dny)
venecky_vsedni_dny_2 = venecky[:5]
print(venecky_vsedni_dny_2)
venecky_vikend = venecky[-2:]
print(venecky_vikend)
print(sorted(venecky_vsedni_dny, reverse=True))

# řetězce
jmeno = 'martin' + ' ' + 'podloucký'
print(jmeno[:6])
print(len(jmeno))

inzerat = "Na této pracovní pozici budete využívat Python a SQL"
if "JavaScript" in inzerat:
    print("OK!")
else:
    print("Run!")

email = "spatny-mail.cz"
if "@" not in email:
    print("V e-mailu chybí zavináč!")

"""
Notes
- mezera na začátku může vyhodit chybu - py řeší odsazení, jinak se mezery moc neřeší
- hlídat malá a velká písmena
- v tomto případě venecky = seznam, Venecky = třída (dodržovat pravidla pro názvy proměnných)
- apostrofy i uvozovky ok
- podmínka = rozhodnutí

Slicing
- index - pozice --> print(venecky[0])
- komentář na jeden řádek --> #
- kde_koncim = pozice, před kterou výběr končí --> venecky[0:5] --> prvních 5 hodnot (může být i [:5])
- posledni 2 hodnoty --> [-2:]
- print(len()) --> nejdřív se zpracuje len, pak print
- len - jako znak se počítá i mezera

Několik funkcí pro práci se seznamy:
- len() : Vrátí délku seznamu
- sum() : Vrátí součet všech prvků v seznamu
- min() : Vrátí nejmenší prvek seznamu
- max() : Vrátí největší prvek seznamu
- sorted() : Vrátí setříděný seznam --> přidat reverse=True - pokud chci seřadit desc --> print(sorted(venecky_vsedni_dny, reverse=True))
"""

# cvičení
## pohyby na účtu
pohyby = [1200, -250, -800, 540, 721, -613, -222]
# Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2:])
# Vypište všechny pohyby kromě prvních dvou.
print(len(pohyby))
# Vypište kolik je všech pohybů dohromady.
print(max(pohyby))
# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(min(pohyby))
# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))

## průměr
"""
Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
"""
s = [5, 3, 2, 1, 2, 1, 9]

"""
Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. 
Otestujte jej na seznamech různých délek.
"""
vzorecek = sum(s)/len(s)
print(vzorecek)

## rozpětí
"""
Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí,
tedy rozdílu mezi minimální a maximální hodnotou.
"""
rozpeti = max(s)-min(s)
print(rozpeti)
print(max(s)-min(s))