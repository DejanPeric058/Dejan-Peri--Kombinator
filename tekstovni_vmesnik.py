from model import *
from slovar import slovar_funkcij

zbirka_stevil = Zbirka_stevil('zbirka_stevil', 'zbirka_stevil.json')

def pozdrav():
    print('Dobrodošli v Kombinator! Tri najbolj iskana kombinatorična števila:')
    for x in zbirka_stevil.prikazi_najbolj_iskane():
        print('{}'.format(x))
    return input('Izberite, katero kombinatorično število bi radi izračunali:')

def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('> ')
    return int(izbira) - 1

def osnovni_meni():
    print('Kaj bi rad izračunal?')
    sez = slovar_v_seznam(slovar_funkcij)
    izbira = izberi(sez)
    razdelek = sez[izbira]
    if razdelek == 'Dvanajstera pot':
        Dvanajstera_pot()
    else:
        Razdelek(razdelek)

def Razdelek(razdelek):
    print('Kaj bi rad izračunal?')
    sez = slovar_v_seznam(slovar_funkcij[razdelek])
    izbira = izberi(sez)
    stevilo = sez[izbira]
    izracun(razdelek, stevilo)

def Dvanajstera_pot():
    print('Kakšno vrsto preslikave imaš?')
    preslikava = ustvari_preslikavo()
    sez = slovar_v_seznam(slovar_funkcij['Dvanajstera pot']['vrsta'])
    izbira = izberi(sez)
    vrsta = slovar_funkcij['Dvanajstera pot']['vrsta'][sez[izbira]]
    preslikava.doloci_vrsto(vrsta)
    Razlikujemo(preslikava)

def Razlikujemo(preslikava):
    print('Ali kroglice in škatle razlikujemo med seboj ali ne?')
    sez = slovar_v_seznam(slovar_funkcij['Dvanajstera pot']['razlikovanje'])
    izbira = izberi(sez)
    razlikovanje = slovar_funkcij['Dvanajstera pot']['razlikovanje'][sez[izbira]]
    preslikava.doloci_razlikovanje(razlikovanje)
    izracun_preslikave(preslikava)

def preberi():
    return input('> ')

def izracun(razdelek, stevilo):
    zbirka_stevil.zabelezi(stevilo)
    sez = []
    podslovar = slovar_funkcij[razdelek][stevilo]
    print (podslovar['besedilo1'])
    sez.append(int(preberi()))
    if podslovar['stevilo_argumentov'] == 1:
        return print('Rezultat: {}'.format(podslovar['funkcija'](sez)))
    elif podslovar['stevilo_argumentov'] == 2:
        print (podslovar['besedilo2'])
        sez.append(int(preberi()))
        return print('Rezultat: {}'.format(podslovar['funkcija'](sez)))
    else:
        return izračun_multinomski(sez)
    
def izracun_multinomski(sez):
    stevilo = sez[0]
    sez = []
    for x in range(stevilo):
        print ('Vpiši {}. člen'.format(x + 1))
        sez.append(int(preberi()))
    return print('Rezultat: {}'.format(multinomski(sez)))

def izracun_preslikave(preslikava):
    print ('Vpiši število kroglic:')
    vrednost1 = int(preberi())
    print ('Vpiši število škatel:')
    vrednost2 = int(preberi())
    return print('Rezultat: {}'.format(preslikava.stevilo_preslikav(vrednost1, vrednost2)))

def pozeni_vmesnik():
    pozdrav()
    while True:
        osnovni_meni()

pozeni_vmesnik()