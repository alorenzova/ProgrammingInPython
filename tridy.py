# Funkce pro práci s objekty
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
if isinstance(marian, Manager):
    print("Objekt pochází ze třídy Manager")
else:
    print("Objekt nepochází ze třídy Manager")

frantisek = Employee("František Novák", "konstruktér", 25)
if isinstance(frantisek, Manager):
    print("Objekt pochází ze třídy Manager")
else:
    print("Objekt nepochází ze třídy Manager")

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
frantisek = Employee("František Novák", "konstruktér", 25)
objekty = [marian, frantisek]
for polozka in objekty:
    if isinstance(polozka, Manager):
        print(f"{polozka} pochází ze třídy Manager")
    else:
        print(f"{polozka} nepochází ze třídy Manager")

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
frantisek = Employee("František Novák", "konstruktér", 25)
objekty = [marian, frantisek]
for polozka in objekty:
    if isinstance(polozka, Employee):
        print(f"{polozka.name} pochází ze třídy Employee nebo jejích potomků")
    else:
        print(f"{polozka.name} nepochází ze třídy Employee nebo jejích potomků")

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
objekty = [marian, marketa, frantisek]
expected_people = 0
for polozka in objekty:
    if isinstance(polozka, Manager):
        print(f"Pozvánka pro: {polozka.name}")
        expected_people += 1
print(f"Čekáme {expected_people} osob.")

jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")
objekty = [marian, marketa, frantisek, jakub]
for polozka in objekty:
    if hasattr(polozka, "car"):
        print(polozka.car)

for polozka in objekty:
    if isinstance(polozka, Salesman) or isinstance(polozka, Manager):
        print(polozka.car)

atribut = input("Zadej atribut: ")
print(getattr(marketa, atribut, f"neznámý atribut: {atribut}"))

class Employee:
    def __init__(self, name, position, holiday_entitlement, manager=None):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.manager = manager
    def get_manager_name(self):
        if self.manager:
            return self.manager.name
        else:
            return "Zatím nenastoupil"

class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, manager, subordinates, car):
        super().__init__(name, position, holiday_entitlement, manager)
        self.subordinates = subordinates
        self.car = car

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, None, 5, "Škoda Octavia 1.5 TSI")
frantisek = Employee("František Novák", "konstruktér", 25)
print(frantisek.get_manager_name())
marketa = Manager("Markéta Polková", "teamleader", 25, marian, 12, "Škoda Octavia RS")
frantisek.manager = marketa
print(frantisek.get_manager_name())





## Cvičení
### Celková hodnota balíků
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."
    
### Celková hodnota balíků podruhé (bonus) --> zmenit podminku v cyklu

