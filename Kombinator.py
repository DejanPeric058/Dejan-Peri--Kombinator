import bottle
from model import *
from slovar import slovar_funkcij

zbirka_stevil = Zbirka_stevil('zbirka_stevil', 'zbirka_stevil.json')

@bottle.get('/')
def osnovna_stran():
  return bottle.template('index', zbirka_stevil=zbirka_stevil)

@bottle.get('/<razdelek>/')
def Osnovne_kombinatorične_funkcije(razdelek):
    return bottle.template('Osnovne_kombinatorične_funkcije2', razdelek = razdelek)

@bottle.get('/<razdelek>/<stevilo>/')
def izracun(razdelek, stevilo):
    if razdelek == 'Dvanajstera pot':
        return bottle.template('vrsta_preslikave', razlikovanje=stevilo, razdelek=razdelek)
    elif stevilo == 'Multinomski koeficient' and bottle.request.query.getunicode('stevilo argumentov') != None:
        stevilo_argumentov = int(bottle.request.query.getunicode('stevilo argumentov'))
        slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] = stevilo_argumentov
        return bottle.template('izracun', stevilo=stevilo, stevilo_argumentov = stevilo_argumentov, razdelek=razdelek)
    else:
        return bottle.template('izracun', stevilo=stevilo, razdelek=razdelek)

@bottle.get('/<razdelek>/<stevilo>/rezultat/')
def rezultat(razdelek, stevilo):
    sez = []
    for x in range(1, slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] + 1):
        sez.append(int(bottle.request.query.getunicode('vrednost{}'.format(x))))
    return bottle.template('rezultat', stevilo=stevilo, razdelek=razdelek, sez=sez)

@bottle.get('/<razdelek>/<razlikovanje>/<vrsta>/')
def stevilo_preslikav_izracun(razdelek, razlikovanje, vrsta):
    return bottle.template('stevilo_preslikav', razdelek=razdelek, razlikovanje=razlikovanje, vrsta=vrsta)

@bottle.get('/<razdelek>/<razlikovanje>/<vrsta>/rezultat/')
def rezultat_preslikave(razdelek, razlikovanje, vrsta):
    vrednost1 = int(bottle.request.query.getunicode('vrednost1'))
    vrednost2 = int(bottle.request.query.getunicode('vrednost2'))
    return bottle.template('rezultat_preslikave', razdelek=razdelek, razlikovanje=razlikovanje, vrsta=vrsta, vrednost1=vrednost1, vrednost2=vrednost2) 

@bottle.post('/<razdelek>/<stevilo>/shrani_rezultat/')
def shrani_rezultat(razdelek, stevilo):
    zbirka_stevil.zabelezi(stevilo)
    bottle.redirect('/')


bottle.run(debug = True, reloader = True)