from model2 import *

def pozdrav():
    return input("Dobrodošli v Kombinator! Izberite, katero kombinatorično število bi radi izračunali:")

def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('> ')
    return int(izbira) - 1

def osnovni_meni():
    print('Kaj bi rad izračunal?')
    izbira = izberi(['Osnovne kombinatorične funkcije', 
        'Kombinatorična številska zaporedja',
        'Dvanajstera pot',
    ])
    if izbira == 0:
        Osnovne_kombinatoricne_funkcije()
    elif izbira == 1:
        Kombinatoricna_stevilska_zaporedja()
    elif izbira == 2:
        Dvanajstera_pot()
    else:
        assert False

def Osnovne_kombinatoricne_funkcije():
    print('Kaj bi rad izračunal?')
    izbira = izberi(['Fakulteta', 
        'Binomski koeficient',
        'Potenca',
        'Padajoča potenca',
        'Rastoča potenca',
        'Multinomski koeficient',
    ])
    if izbira == 5:
        vnesi_multinomski()
    else:
        if izbira == 0:
            stevilo = ustvari_stevilo(fakulteta, 1, 'Vpiši število:', '')
        elif izbira == 1:
            stevilo = ustvari_stevilo(binomski, 2, 'Vpiši zgornje število:', 'Vpiši spodnje število:')
        elif izbira == 2:
            stevilo = ustvari_stevilo(potenca, 2, 'Vpiši osnovo:', 'Vpiši eksponent:')  
        elif izbira == 3:
            stevilo = ustvari_stevilo(padajoča_potenca, 2, 'Vpiši osnovo:', 'Vpiši eksponent:')
        elif izbira == 4:
            stevilo = ustvari_stevilo(rastoča_potenca, 2, 'Vpiši osnovo:', 'Vpiši eksponent:')
        else:
            assert False
        vnesi_cifre(stevilo)

def Kombinatoricna_stevilska_zaporedja():
    print('Kaj bi rad izračunal?')
    izbira = izberi(['Stirlingova števila 1. vrste', 
        'Stirlingova števila 2. vrste',
        'Lahova števila',
        'Celoštevilske particije',
        'Bellova števila',
        'Catalanova števila',
    ])
    if izbira == 3:
        Celoštevilske_particije()
    else:    
        if izbira == 0:
            stevilo = ustvari_stevilo(stirling1, 2, 'Vpiši število elementov:', 'Vpiši število blokov:')
        elif izbira == 1:
            stevilo = ustvari_stevilo(stirling2, 2, 'Vpiši število elementov:', 'Vpiši število blokov:')
        elif izbira == 2:
            stevilo = ustvari_stevilo(lahova, 2, 'Vpiši število elementov:', 'Vpiši število blokov:')
        elif izbira == 4:
            stevilo = ustvari_stevilo(bellova, 1, 'Kateri člen zaporedja Bellovih števil iščeš?:', '')
        elif izbira == 5:
            stevilo = ustvari_stevilo(catalanova, 1, 'Kateri člen zaporedja Catalanovih števil iščeš?:', '')
        else:
            assert False
        vnesi_cifre(stevilo)

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
    print (stevilo.besedilo1)
    vrednost1 = int(preberi())
    if stevilo.stevilo_argumentov == 1:
        return print('Rezultat: {}'.format(stevilo.funkcija(vrednost1)))
    else:
        print (stevilo.besedilo2)
        vrednost2 = int(preberi())
        return print('Rezultat: {}'.format(stevilo.funkcija(vrednost1, vrednost2)))

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