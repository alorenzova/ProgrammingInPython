# Třídy a objekty
#* místo pass se dají použít ...

class Employee:
    def __init__(self, name, position, holiday_entitlement):
        # self.name je atribut třídy Employee
        # name je jen parametr metody __init__
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    # def get_info(self):
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            # self.holiday_entitlement = self.holiday_entitlement - days
            self.holiday_entitlement -= days # -= snížení
            return "Schváleno"
        else:
            return "Neschváleno, nahlášené dny jsou nad limit zbývajícíh dnů k čerpání dovolené"

frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nová", "konstruktérka", 25)
print(frantisek.holiday_entitlement)
frantisek.take_holiday(5)
print(frantisek.holiday_entitlement)
print(frantisek.take_holiday(20))
print(frantisek.take_holiday(10))
print(klara.take_holiday(15))

print(frantisek.name) # Čtu atribut name objektu frantisek
# print(frantisek.get_info())
# print(klara.get_info())


## Cvičení
### Balík
"""
Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, 
která uloží hodnoty parametrů metody do atributů.
"""

"""
class Package:
    def __init__(self, address: str, weight: float, state: str):
        self.address = address
        self.weight = weight
        self.state = state  

    def get_info(self) -> str: # -> str --> očekávám jako výsledek řetězec
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self) -> int:
        if self.weight < 10:
            return 129
        elif 10 <= self.weight <= 20: # podmínka na interval od 10 do 20
            return 159
        else:
            return 359

# typizace: upřesnění datových typů --> best practice
"""

"""
⬆️
Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. 
Uvažuj například větu "Balík na adresu Krakovská 583/9, Praha má hmotnost 0.25 kg je ve stavu nedoručen".

Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. 
Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších 
než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.
"""

"""
Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. 
U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
⬇️
"""

"""
balik1 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
balik2 = Package("Masarykova 21, Brno", 15.8, "doručen")
"""

"""
Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.
"""

"""
print(balik1.get_info())
print("Cena přepravy:", balik1.delivery_price(), "Kč")
print(balik2.get_info())
print("Cena přepravy:", balik2.delivery_price(), "Kč")
"""

### Balík podruhé
"""
U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print(). --> ne, chybí self

Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. 
Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". 
Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. 
Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".

Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?
"""

class Package:
    def __init__(self, address: str, weight: float, state: str):
        self.address = address
        self.weight = weight
        self.state = state  

    def __str__(self) -> str: # -> str --> očekávám jako výsledek řetězec
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self) -> int:
        if self.weight < 10:
            return 129
        elif 10 <= self.weight <= 20: # podmínka na interval od 10 do 20
            return 159
        else:
            return 359

    def deliver(self) -> str:
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen" # bez toho nefunguje --> dvakrát deliver() --> dvakrát "Balík již byl doručen"
            return "Doručení uloženo"


balik1 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
balik2 = Package("Masarykova 21, Brno", 15.8, "doručen")

#print(balik1.get_info())
print("Cena přepravy:", balik1.delivery_price(), "Kč")
#print(balik2.get_info())
print("Cena přepravy:", balik2.delivery_price(), "Kč")

print("První pokus o doručení:", balik1.deliver())
print("Druhý pokus o doručení:", balik1.deliver())

# balíček mypy --> nástroj pro statickou kontrolu typů v Pythonu

### Kniha (bonus)
"""
Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. 
Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

> Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.

> Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. S využitím atributu pages vypočítej čas na přečtení knihy. 
Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy. Dobu potřebnou na přečtení knihy získáš jako 
násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. Výchozí hodnota nepovinného parametru je 4.
"""

"""
class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
        
    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, page_minutes=4):
        return self.pages * page_minutes

book_1 = Book("Day of the Wipers", 528, 646)
print(book_1.get_info())
print(f"Knihu je možné přečíst za {book_1.get_time_to_read()} minut.")
print(f"Při pomalejším čtení za {book_1.get_time_to_read(5)} minut.")
"""

### Kniha podruhé (bonus)
"""
> U knihy budeme chtít evidovat, kolik kusů bylo prodáno. Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__(). 
Dále přidej atribut costs, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).

> Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).

> Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". 
Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".
"""

class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs
        
    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, page_minutes=4):
        return self.pages * page_minutes
    
    def profit(self):
        return (self.price - self.costs) * self.sold
    
    def rating(self):
        if self.profit() < 50000:
            return "propadák"
        elif self.profit() < 500000:
            return "průměr"
        else:
            return "bestseller"

book_1 = Book("Day of the Wipers", 528, 646, 340000, 260)
print(f"Zisk z prodeje knihy je {book_1.profit()} Kč.")
print(f"Kniha je {book_1.rating()}.")