# 1. Co je potřeba vložit do definice ("prvního řádku") funkce?
#* klíčové slovo def
#* název funkce
#* parametry, se kterými funkce pracuje (píšeme je do závorek)
#* dvojtečku

# 2. Co vypíše následující program?
def vynasob_cislo_deseti(cislo):
    cislo * 10
print(vynasob_cislo_deseti(5))
#* Program vypíše None (protože ve funkci chybí klíčové slovo return, funkce nevrátí nic)

# 3. Co vypíše následující program?
def spocitej_cenu(cena_za_kus, kusy, postovne):
    cena = cena_za_kus * kusy + postovne
    return cena
    print(cena)
spocitej_cenu(250, 3, 90)
#* Nevypíše nic

# 4. Proč je v proměnné cena_za_knihy hodnota None místo 840?
def spocitej_cenu(cena_za_kus, kusy, postovne):
    cena = cena_za_kus * kusy
cena_za_knihy = spocitej_cenu(250, 3, 90)
#* Ve funkci chybí klíčové slovo return

# 5. Co platí o následující funkci?
def vypocitej_slevu(kod):
    if kod == "MAM_RADA_JAVU":
        return 5
    elif kod == "MAM_RADA_PYTHON":
        return 30
    else:
        return 0
# print(vypocitej_slevu("MAM_RADA_PYTHON"))
#* Ve funkci žádná chyba není

# 6. Která volání funkce budou fungovat?
def kofein_za_den(pocet_esspreso, pocet_filtrovana=0):
    return pocet_esspreso * 75 + pocet_filtrovana * 150
#* kofein_za_den(3)
#x kofein_za_den() --> chybi pocet
#x kofein_za_den(1, 2, 3) --> tri parametry jsou moc
#* kofein_za_den(2, 1)

# 7. Uvažuj následující funkci. Která varianta typování je podle tebe nejlepší?
def kontrola_emailu(email):
    if "@" in email:
        return True
    else:
        return False
#* def kontrola_emailu(email: str) -> bool:

# 8. Jaká je chyba v definici funkce?
"""
def znamka(bonusove_body=0, body_test):
    body_celkem = body_test + bonusove_body
    if body_celkem < 60:
        return 4
    elif body_celkem < 75:
        return 3
    elif body_celkem < 90:
        return 2
    else:
        return 1
"""
#* Parametry s výchozí hodnotou musí být až za parametry bez výchozí hodnoty.

# 9. Uvažuj následující funkci a její volání. Volání je trochu jiné, než jsme si ukazovali na lekci. Jak podle tebe toto volání bude fungovat?
def spocitej_cenu(cena_za_kus, kusy, postovne):
    return cena_za_kus * kusy + postovne
print(spocitej_cenu(cena_za_kus=100, postovne=90, kusy=5))
#* Python bude respektovat, jaký název parametru dopíšu k hodnotě při volání, takže kusy budou mít hodnotu 5 a postovne 90.

# 10. Jak pomocí typování funkcí zdokumentujeme, že funkce kofein_za_den vrací jako výsledek celé číslo?
#* def kofein_za_den(pocet_espresso, pocet_filtrovana=0) -> int:
