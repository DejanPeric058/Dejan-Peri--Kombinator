from model import *

slovar_funkcij = {'Osnovne kombinatorične funkcije':{'Fakulteta':

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

                                                    {'funkcija': multinomski,'stevilo_argumentov': 'poljubno', 'besedilo1': 'Koliko členov ima multinomski koeficient?:', 'besedilo2': ''}
                                                    },           
             'Kombinatorična številska zaporedja':{'Stirlingova števila 1. vrste': 

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
                                                    },
                                'Dvanajstera pot':  {'vrsta':       {'Vse preslikave': 1, 
                                                                    'Injekcijo': 2,
                                                                    'Surjekcijo': 3,
                                                                    'Bijekcijo': 4
                                                                    }, 

                                                    'razlikovanje': {'Kroglice in škatle razlikujemo med seboj': 1, 
                                                                    'Kroglice razlikujemo, škatel ne': 2,
                                                                    'Škatle razlikujemo, kroglic ne': 3,
                                                                    'Kroglic in škatel ne razlikujemo med seboj': 4
                                                                    }
                                                    }
                                                    }