# metody
jmeno = " MArtin    Ekekekek"
print(jmeno)
# použití metody --> proti fci --> s čím pracujeme, pak ., pak název metody
# - metody = věci, které jsou zaměřené na jeden typ hodnoty
# - lower --> metoda (pracuje jen s řetěžcem), len --> funkce
print(jmeno.lower())
print('martin'.upper())
print('  martin   '.strip()) #whitescpaces
print(jmeno.lower().strip())
print(jmeno.replace("A", "b")) #nahradit znak(y)


dny = "po    ut      st čt pá" #print('po ut st čt pá'.split(' '))
print(dny.split()) 
#když prázdné závorky, tak mezera znamená konec řetězce a začátek druhého
#víc mezer, jeden oddělovač
# pokud oddělěno čárkami, tak to chápe jako řetězec (neoodělené dny) -->(",")
days = "po,ut,st,čt,pá"
print(days.split(","))

temata = ['metody', 'czechitas', 'python', 'priklady']
print(", ".join(temata))

# počty mezer jsou různé
retezec = "python    java  C        pascal"
# použiju split s prázdnými závorkami, ten se zbaví mezer mezi slovy bez ohledu na jejich počet
# vznikne seznam řetězců (bez mezer)
seznam = retezec.split()
# seznam řetězců převedu na řetězec a jako znak mezi nimi využiju mezeru
# všude bude shodně jedna mezera
retezec_jedna_mezera = " ".join(seznam)
print(retezec_jedna_mezera)


# cvičení 
## převod písmen
name = "Aneta"
print(name.lower())
print(name.upper())

## čísla jako text
hodnoty = ['12', '1', '7', '-11']

"""
Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:

hodnoty = ['12', '1', '11', '-11']
"""

#print(hodnoty[2].plus[4])

num3 = hodnoty[2]
num3 = int(num3)
num3 += 4
#print(num3)
num3 = str(num3)
hodnoty[2] = num3
print(hodnoty)

## 3
values_list = hodnoty.split()
print(values_list)
last_value = hodnoty[-1]
print(last_value)
