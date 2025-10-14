# 1. Jaký je rozdíl mezi objektem a třídou?
#* Třída je šablona nebo definice, která určuje atributy a chování objektů, zatímco objekt je "postavený na základě" třídy a má nějaké konkrétní hodnoty atributů.

# 2. Jaký je rozdíl mezi objektem a atributem?
#* Objekt je instancí třídy reprezentující konkrétní entitu, zatímco atribut objektu je hodnota přiřazená k nějakému objektu.

# 3. Jaký je rozdíl mezi funkcí a metodou?
#* Funkce je samostatný blok kódu, zatímco metoda je funkce definovaná uvnitř třídy pracuje s hodnotami atributů objektu.

# 4. Které tvrzení je pravdivé?
class Task:
    def __init__(self, description, assigned_to):
        self.description = description
        self.completed = False
        self.assigned_to = assigned_to

email_task = Task("Napsat e-mail zákazníkovi, že program je hotový", "Jirka")

#* email_task je objekt (instance) třídy `Task`

# 5. Co vypíše následující program?
class Task:
    def __init__(self, description, assigned_to):
        self.description = description
        self.completed = False
        self.assigned_to = assigned_to

email_task = Task("Napsat e-mail zákazníkovi, že program je hotový", "Jirka")
print(email_task.assigned_to)

#* Program vypíše Jirka

# 6. Jak změnit úkolu email_task hodnotu atribut completed na True?
class Task:
    def __init__(self, description, assigned_to):
        self.description = description
        self.completed = False
        self.assigned_to = assigned_to

email_task = Task("Napsat e-mail zákazníkovi, že program je hotový", "Jirka")

#* email_task.completed = True

# 7. Proč tento program vypisuje Jirka a ne Kuba?
class Task:
    def __init__(self, description, assigned_to):
        self.description = description
        self.completed = False
        self.assigned_to = assigned_to

email_task = Task("Napsat e-mail zákazníkovi, že program je hotový", "Jirka")
assigned_to = "Kuba"
print(email_task.assigned_to)

#* V programu nastavujeme hodnotu proměnné assigned_to, ale nijak neměníme atribut assigned_to objektu email_task`.

# 8. Které z těchto programovacích jazyků umožňují programovat s využitím objektově orientovaného programování? (Správně jsou 3 odpovědi)
#* Java
#* C#
#* Python

# 9. Které tvrzení o rozdílu mezi Javou a Pythonem je pravdivé?
#* V Pythonu je možné psát kód i mimo třídy, v Javě musí být všechen kód uvnitř třídy.