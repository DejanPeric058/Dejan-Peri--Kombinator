from datetime import datetime
import json


class Model:
    def __init__(self):
        return print('MODEL ŠE NI REDI')

class Stevilo:
    def __init__(self, funkcija, stevilo_argumentov=2, besedilo1='Vnesi število:', besedilo2='Vnesi število blokov'):
        self.funkcija = funkcija
        self.stevilo_argumentov = stevilo_argumentov
        self.besedilo1 = besedilo1
        self.besedilo2 = besedilo2

    def spremeni_besedilo2(self, besedilo2):
        self.besedilo2 = besedilo2
        return

class Preslikava:
    def __init__(self, vrsta=1, razlikovanje=1):
        self.vrsta = vrsta
        self.razlikovanje = razlikovanje

    def stevilo_preslikav(self, stevilo_kroglic, stevilo_skatel):
        n = stevilo_kroglic
        k = stevilo_skatel
        if self.vrsta == 4:
            if self.razlikovanje == 1:
                return bijekcija1(n, k)
            elif self.razlikovanje in [2, 3, 4]:
                return bijekcija234(n, k)
        elif self.razlikovanje == 1:
            if self.vrsta == 1:
                return preslikave1(n, k)
            elif self.vrsta == 2:
                return injekcije1(n, k)
            elif self.vrsta == 3:
                return surjekcije1(n, k)
        elif self.razlikovanje == 2:
            if self.vrsta == 1:
                return preslikave2(n, k)
            elif self.vrsta == 2:
                return injekcije2(n, k)
            elif self.vrsta == 3:
                return surjekcije2(n, k)
        elif self.razlikovanje == 3:
            if self.vrsta == 1:
                return preslikave3(n, k)
            elif self.vrsta == 2:
                return injekcije34(n, k)
            elif self.vrsta == 3:
                return surjekcije3(n, k)
        elif self.razlikovanje == 4:
            if self.vrsta == 1:
                return preslikave4(n, k)
            elif self.vrsta == 2:
                return injekcije34(n, k)
            elif self.vrsta == 3:
                return surjekcije4(n, k)
        
    def doloci_vrsto(self, vrsta):
        self.vrsta = vrsta
        return

    def doloci_razlikovanje(self, razlikovanje):
        self.razlikovanje = razlikovanje
        return

def ustvari_stevilo(funkcija, n, besedilo1, besedilo2):
    return Stevilo(funkcija, n, besedilo1, besedilo2)

def ustvari_preslikavo():
    return Preslikava()

def fakulteta(n):
    produkt = 1
    for x in range(1, n + 1):
        produkt = x * produkt
    return produkt

def binomski(n, k):
    if k == 0:
        return 1
    else:
        return (n - k + 1) * binomski(n, k - 1) // k

def potenca(n, k):
    return n ** k

def padajoča_potenca(x, n):
    produkt = x
    for i in range(1, n):
        produkt = produkt * (x - i)
    return produkt

def rastoča_potenca(x, n):
    produkt = x
    for i in range(1, n):
        produkt = produkt * (x + i)
    return produkt

def multinomski(sez):
    if len(sez) == 1:
        return 1
    return binomski(sum(sez), sez[-1]) * multinomski(sez[:-1])

def stirling2_vsota(n, k, j):
    if j < 0:
        return 0
    else:
        return stirling2_vsota(n, k, j - 1) + (((- 1) ** j) * binomski(k, j) * (k - j) ** n)

def stirling2(n, k):
    return stirling2_vsota(n, k, k) // fakulteta(k)

def stirling1(n, k):
    if n == k:
        return 1
    elif n == 0 or k > n:
        return 0
    elif k == 1:
        return fakulteta(n - 1)
    elif k == n - 2:
        return (3 * n - 1) * binomski(n, 3) // 4
    elif k == n - 3:
        return binomski(n, 2) * binomski(n, 4)
    else:
        return (n - 1) * stirling1(n - 1, k) + stirling1(n - 1, k - 1)

def lahova(n, k):
    return binomski(n - 1, k - 1) * fakulteta(n) // fakulteta(k)

def particijek(n, k):
    if n == k == 0 :
        return 1
    elif n == 0 or k == 0 or n < k:
        return 0
    else:
        return particijek(n - k, k) + particijek(n - 1, k - 1)

def particije(n):
    particija = 0
    for i in range(1, n + 1):
        particija += particijek(n, i)
    return particija

def bellova(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
 
        bell[i][0] = bell[i-1][i-1] 
   
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 
  
    return bell[n][0] 

def catalanova(n):
    return binomski(2 * n, n) // (n + 1)

def preslikave1(n, k):
    return k ** n

def injekcije1(n, k):
    return padajoča_potenca(k, n)

def surjekcije1(n, k):
    return fakulteta(k) * stirling2(n, k)

def preslikave2(n, k):
    return binomski(n + k - 1, n)

def injekcije2(n, k):
    return binomski(k, n)

def surjekcije2(n, k):
    return binomski(n - 1, n - k)

def preslikave3(n, k):
    preslikave = 0
    for i in range(1, k + 1):
        preslikave += stirling2(n, i)
    return preslikave

def injekcije34(n, k):
    if k >= n:
        return 1
    else:
        return 0
def surjekcije3(n, k):
    return stirling2(n, k)

def preslikave4(n, k):
    preslikave = 0
    for i in range(1, k + 1):
        preslikave += particijek(n, i)
    return preslikave

def surjekcije4(n, k):
    return particijek(n, k)

def bijekcija1(n, k):
    if n == k:
        return fakulteta(n)
    else:
        return 0

def bijekcija234(n, k):
    if n == k:
        return 1
    else:
        return 0
