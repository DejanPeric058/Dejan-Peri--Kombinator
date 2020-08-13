import bottle
from model import *
from slovar import slovar_funkcij

import os

bottle.TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

@bottle.get('/')
def osnovna_stran():
  return bottle.template('index')

@bottle.get('/<razdelek>/')
def Osnovne_kombinatorične_funkcije(razdelek):
    return bottle.template('Osnovne_kombinatorične_funkcije2', razdelek = razdelek)


@bottle.get('/<razdelek>/<stevilo>/')
def izracun(razdelek, stevilo):
    if stevilo == 'Multinomski koeficient' and slovar_funkcij[razdelek][stevilo]['argumenti_nastavljeni']:
        stevilo_argumentov = int(bottle.request.query.getunicode('stevilo_argumentov'))
        slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] = stevilo_argumentov
        return bottle.template('izracun', stevilo=stevilo, stevilo_argumentov = stevilo_argumentov, razdelek=razdelek)
    else:
        return bottle.template('izracun', stevilo=stevilo, razdelek=razdelek)

@bottle.get('/<razdelek>/<stevilo>/rezultat/')
def rezultat(razdelek, stevilo):
    vrednost1 = int(bottle.request.query.getunicode('vrednost1'))
    if slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] == 2 and stevilo != 'Multinomski koeficient':
        vrednost2 = int(bottle.request.query.getunicode('vrednost2'))
        return bottle.template('rezultat', stevilo=stevilo, razdelek=razdelek, vrednost1=vrednost1, vrednost2=vrednost2)
    elif slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] == 1 and stevilo != 'Multinomski koeficient':
        return bottle.template('rezultat', stevilo=stevilo, vrednost1=vrednost1)
    else:
        sez = []
        for x in range(1, slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] + 1):
            sez.append(int(bottle.request.query.getunicode('vrednost{}'.format(x))))
        return bottle.template('rezultat', stevilo=stevilo, razdelek=razdelek, sez=sez)

bottle.run(debug = True, reloader = True)