import bottle
from model import *
from slovar import slovar_funkcij

import os

bottle.TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

@bottle.get('/')
def osnovna_stran():
  return bottle.template('index')

@bottle.get('/Osnovne_kombinatoricne_funkcije/')
def Osnovne_kombinatorične_funkcije():
    return bottle.template('Osnovne_kombinatorične_funkcije2')


@bottle.get('/izracun/<stevilo>/')
def izracun(stevilo):
    if stevilo == 'Multinomski koeficient' and slovar_funkcij[stevilo]['argumenti_nastavljeni']:
        stevilo_argumentov = int(bottle.request.query.getunicode('stevilo_argumentov'))
        return bottle.template('izracun', stevilo=stevilo, stevilo_argumentov = stevilo_argumentov)
    else:
        return bottle.template('izracun', stevilo=stevilo)

@bottle.get('/rezultat/<stevilo>/')
def rezultat(stevilo):
    vrednost1 = int(bottle.request.query.getunicode('vrednost1'))
    if slovar_funkcij[stevilo]['stevilo_argumentov'] == 2:
        vrednost2 = int(bottle.request.query.getunicode('vrednost2'))
        return bottle.template('rezultat', stevilo=stevilo, vrednost1=vrednost1, vrednost2=vrednost2)
    elif slovar_funkcij[stevilo]['stevilo_argumentov'] == 1:
        return bottle.template('rezultat', stevilo=stevilo, vrednost1=vrednost1)
    else:
        pass

bottle.run(debug = True, reloader = True)