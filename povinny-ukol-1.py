# Domácí úkoly - Úkol 1 (povinný)
## Zadání povinné části úkolu
"""
Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. 
Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, 
bytové a komerční prostory. Výše daně se odvíjí od několika faktorů, např. typu 
nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd.
"""

### 1) Třída Locality s atributy name a locality_coefficient
"""
V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, 
kde se nemovitost nachází. Třída bude mít atributy name (název katastru/obce) 
a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).
"""

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient = locality_coefficient

    def __str__(self) -> str:
        return f"Lokalita: {self.name}, místní koeficient: {self.locality_coefficient}"
 
    #def get_locality_info_(self) -> str:
        #return f"Lokalita: {self.name}, místní koeficient: {self.locality_coefficient}"
        # !!! tato cast nefunguje, smazat

#### Praha, Brno
"""
praha = Locality("Praha", 6.4)
brno = Locality("Brno", 2.3)
"""
"""
praha = Locality(name="Praha", locality_coefficient=6.4)
brno = Locality(name="Brno", locality_coefficient=2.3)
"""
"""
print(praha)
print(brno)

print("Koeficient pro Brno: ", brno.locality_coefficient)
"""

### 2) třída Property s atributem locality
"""
Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. 
Třída bude mít atribut locality (lokalita, kde se pozemek nachází, 
bude to objekt třídy Locality).
"""

class Property:
    def __init__(self, locality: Locality):
    #def __init__(self, locality: Locality, size: float):
        self.locality = locality
        # self.size = size --> uvest navic i m², aby to davalo vetsi smysl? --> bude nize
    def __str__(self) -> str:
        return f"Nemovitost se nachází v lokalitě s názvem {self.locality.name}." 

    #def __str__(self) -> str:
        #return f"Nemovitost o velikosti {self.size} m² se nachází v lokalitě {self.locality.name}"

#### Dům, byt
"""
dum_v_praze = Property(locality=praha)
byt_v_brne = Property(locality=brno)

print(dum_v_praze)
print(byt_v_brne)

print(f"Místní koeficient pro dům v Praze je: {dum_v_praze.locality.locality_coefficient}")
"""

### 3) třída Estate (potomek Property) s atributy locality, estate_type, area
"""
Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. 
Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku 
v metrech čtverečních). 
"""

class Estate(Property):
    def __init__(self, locality: Locality, estate_type: str, area: float):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def __str__(self) -> str:
        return (f"Pozemek typu {self.estate_type} o rozloze {self.area} m² "
                f"v lokalitě s názvem {self.locality.name}.")
    
#### Zahrádka u Brna
brno = Locality(name="Brno", locality_coefficient=6.66)

zahradka_brno = Estate(
    locality=brno,
    estate_type="zahradka",
    area=123.21
)

print(zahradka_brno)

### 4) Metoda calculate_tax()

"""
Dále přidej metodu calculate_tax(), která spočítá výši daně 
pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() 
z modulu math). Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu 
pozemku (atribut estate_type) * místní koeficient. U atributu estate_type 
následující hodnoty a koeficienty:

- land (zemědělský pozemek) má koeficient 0.85.
- building site (stavební pozemek) má koeficient 9.
- forrest (les) má koeficient 0.35,
- garden (zahrada) má koeficient 2. 

Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě 
s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.
"""



"""
Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem 
třídy Property. Třída bude mít atributy locality, area (podlahová plocha bytu nebo 
domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost 
používanou k podnikání). Dále přidej metodu calculate_tax(), která spočítá výši daně 
pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: 
podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru 
commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů 
čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700. 
Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.
"""



"""
Vyzkoušej svůj program pomocí následujících nemovitostí:

- Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín 
s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
- Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín 
s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
- Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů 
čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti 
je 90 * 3 * 15 * 2 = 8100.
"""

## Bonusy
"""
Tyto bonusy jsou nepovinné a záleží čistě na tobě, zda se do nich pustíš. 
Jednotlivé části jsou nezávislé, můžeš si tedy vybrat libovolné odrážky a ty vyřešit.

- Ke třídě Estate a Residence přidej výpisy informací do metody __str__(). 
Např.: Zemědělský pozemek, lokalita Manětín (koeficient 1), 900 metrů čtverečních, 
daň 765 Kč.
- Uprav třídu Property na abstraktní třídu. Tato třída totiž nereprezentuje žádnou 
konkrétní nemovitost, nemovitost totiž musí být pozemek nebo stavba.
- Přidej třídu TaxReport, která bude reprezentovat daňové přiznání. Třída bude mít 
atributy name (jméno osoby, která přiznání podává) a property_list, což je seznam 
nemovitostí, které jsou v přiznání uvedeny. Dále přidej metodu add_property(), 
která bude mít jako parametr objekt (nemovitost, která je součástí přiznání) 
a vloží ji do seznamu property_list. Dále přidej metodu calculate_tax(), 
která vypočte daň ze všech nemovitostí v seznamu property_list.
- Podívej se na to, jak fungují tzv. enum třídy. Můžeš si přečíst například tento 
text (link: https://www.geeksforgeeks.org/enum-in-python/). Zkus vytvořit třídu pro typy pozemků (zemědělský pozemek, stavební pozemek, 
les, zahrada) a použít ji ve třídě Estate. Použití této třídy zabrání, aby byl 
vytvořen pozemek s neexistujícím typem.
"""

### Řešení bonusu