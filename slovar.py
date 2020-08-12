from model import *

slovar_funkcij = {'Fakulteta':

{'funkcija': fakulteta,'stevilo_argumentov': 1, 'besedilo1': 'Vpiši število:', 'besedilo2': ''},
'Binomski koeficient': 

{'funkcija': binomski,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši zgornje število:', 'besedilo2': 'Vpiši spodnje število:'},
'Potenca':

{'funkcija': potenca,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši osnovo:', 'besedilo2': 'Vpiši eksponent:'},
'Padajoča potenca': 

{'funkcija': padajoča_potenca,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši osnovo:', 'besedilo2': 'Vpiši eksponent:'},
'Rastoča potenca': 

{'funkcija': rastoča_potenca,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši osnovo:', 'besedilo2': 'Vpiši eksponent:'},
'Multinomski koeficient': 

{'funkcija': multinomski,'stevilo_argumentov': 'poljubno', 'besedilo1': 'Koliko členov ima multinomski koeficient?:', 'besedilo2': '', 'argumenti_nastavljeni': False},
'Stirlingova števila 1. vrste': 

{'funkcija': stirling1,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši število elementov:', 'besedilo2': 'Vpiši število blokov:'},
'Stirlingova števila 2. vrste': 

{'funkcija': stirling2,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši število elementov:', 'besedilo2': 'Vpiši število blokov:'},
'Lahova števila': 

{'funkcija': lahova,'stevilo_argumentov': 2, 'besedilo1': 'Vpiši število elementov:', 'besedilo2': 'Vpiši število blokov:'},
#'Celoštevilske particije': 

#{'funkcija': ,'stevilo_argumentov': ,'besedilo1': , 'besedilo2': },
'Bellova števila': 

{'funkcija': bellova,'stevilo_argumentov': 1, 'besedilo1': 'Kateri člen zaporedja Bellovih števil iščeš?:', 'besedilo2': ''},
'Catalanova števila': 

{'funkcija': catalanova,'stevilo_argumentov': 1, 'besedilo1': 'Kateri člen zaporedja Catalanovih števil iščeš?:', 'besedilo2': ''},
}