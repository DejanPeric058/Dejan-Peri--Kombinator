import bottle, model

import os

bottle.TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

@bottle.get('/')
def osnovna_stran():
  return bottle.template('index')

  


bottle.run(debug=True, reloader=True)