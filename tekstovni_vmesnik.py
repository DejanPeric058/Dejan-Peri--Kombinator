from model import *
from slovar import slovar_funkcij

def pozdrav():
    return input("Dobrodošli v Kombinator! Izberite, katero kombinatorično število bi radi izračunali:")

def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('> ')
    return int(izbira) - 1

def osnovni_meni():
    print('Kaj bi rad izračunal?')
    sez = slovar_v_seznam(slovar_funkcij)
    izbira = izberi(sez)
    stevilo = sez[izbira]
    Razdelek(razdelek)

def Razdelek(razdelek):
    print('Kaj bi rad izračunal?')
    sez = slovar_v_seznam(slovar_funkcij[razdelek])
    izbira = izberi(sez)
    stevilo = sez[izbira]
    vnesi_cifre(razdelek, stevilo)

def Celoštevilske_particije():
    print('Katera vrsta celoštevilskih particij te zanima?')
    izbira = izberi(['Particije celega števila na določeno število sumandov', 
        'Vse particije celega števila',
    ])
    if izbira == 0:
        stevilo = ustvari_stevilo(particijek, 2, 'Vpiši naravno število:', 'Vpiši število členov razčlenitve:')
    elif izbira == 1:
        stevilo = ustvari_stevilo(particije, 1, 'Vpiši naravno število:', '')
    else:
        assert False
    vnesi_cifre(stevilo)

def Dvanajstera_pot():
    preslikava = ustvari_preslikavo()
    print('Kakšno vrsto preslikave imaš?')
    izbira = izberi(['Vse preslikave', 
        'Injekcijo',
        'Surjekcijo',
        'Bijekcijo',
    ])
    if izbira == 0:
        preslikava.doloci_vrsto(1)
    elif izbira == 1:
        preslikava.doloci_vrsto(2)
    elif izbira == 2:
        preslikava.doloci_vrsto(3)
    elif izbira == 3:
        preslikava.doloci_vrsto(4)
    else:
        assert False
    Razlikujemo(preslikava)

def Razlikujemo(preslikava):
    print('Ali kroglice in škatle razlikujemo med seboj ali ne?')
    izbira = izberi(['Kroglice in škatle razlikujemo med seboj', 
        'Kroglice razlikujemo, škatel ne',
        'Škatle razlikujemo, kroglic ne',
        'Kroglic in škatel ne razlikujemo med seboj'
    ])
    if izbira == 0:
        preslikava.doloci_razlikovanje(1)
    elif izbira == 1:
        preslikava.doloci_razlikovanje(2)
    elif izbira == 2:
        preslikava.doloci_razlikovanje(3)
    elif izbira == 3:
        preslikava.doloci_razlikovanje(4)
    else:
        assert False
    Vnesi_število(preslikava)

def preberi():
    return input('> ')

def vnesi_cifre(stevilo):
    sez = []
    print (stevilo.besedilo1)
    sez.append(int(preberi()))
    if stevilo.stevilo_argumentov == 1:
        return print('Rezultat: {}'.format(stevilo.funkcija(sez)))
    else:
        print (stevilo.besedilo2)
        sez.append(int(preberi()))
        return print('Rezultat: {}'.format(stevilo.funkcija(sez)))

def vnesi_multinomski():
    print ('Koliko členov ima multinomski koeficient?:')
    stevilo = int(preberi())
    sez = []
    for x in range(stevilo):
        print ('Vpiši {}. člen'.format(x + 1))
        sez.append(int(preberi()))
    return print('Rezultat: {}'.format(multinomski(sez)))

def Vnesi_število(preslikava):
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