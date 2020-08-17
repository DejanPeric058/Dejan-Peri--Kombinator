from model import *

slovar_funkcij = {'Osnovne kombinatorične funkcije':{'Fakulteta':

                                                    {'funkcija': fakulteta, 'stevilo_argumentov': 1, 'besedilo1': 'Vpiši število:', 'besedilo2': '', 'informacije': 'To je fakulteta'},
                                                    'Binomski koeficient': 

                                                    {'funkcija': binomski, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši zgornje število:', 'besedilo2': 'Vpiši spodnje število:', 'informacije': ''},
                                                    'Potenca':

                                                    {'funkcija': potenca, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši osnovo:', 'besedilo2': 'Vpiši eksponent:', 'informacije': ''},
                                                    'Padajoča potenca': 

                                                    {'funkcija': padajoča_potenca, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši osnovo:', 'besedilo2': 'Vpiši eksponent:', 'informacije': ''},
                                                    'Rastoča potenca': 

                                                    {'funkcija': rastoča_potenca, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši osnovo:', 'besedilo2': 'Vpiši eksponent:', 'informacije': ''},
                                                    'Multinomski koeficient': 

                                                    {'funkcija': multinomski, 'stevilo_argumentov': 'poljubno', 'besedilo1': 'Koliko členov ima multinomski koeficient?:', 'besedilo2': '', 'informacije': ''}
                                                    },           
             'Kombinatorična številska zaporedja':{'Stirlingova števila 1. vrste': 

                                                    {'funkcija': stirling1, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši število elementov:', 'besedilo2': 'Vpiši število blokov:', 'informacije': ''},
                                                    'Stirlingova števila 2. vrste': 

                                                    {'funkcija': stirling2, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši število elementov:', 'besedilo2': 'Vpiši število blokov:', 'informacije': ''},
                                                    'Lahova števila': 

                                                    {'funkcija': lahova, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši število elementov:', 'besedilo2': 'Vpiši število blokov:', 'informacije': ''},
                                                    'Celoštevilska particija na k členov': 

                                                    {'funkcija': particijek, 'stevilo_argumentov': 2, 'besedilo1': 'Vpiši naravno število:', 'besedilo2': 'Vpiši število členov razčlenitve:', 'informacije': ''},
                                                    'Celoštevilska particija': 

                                                    {'funkcija': particije, 'stevilo_argumentov': 1, 'besedilo1': 'Vpiši naravno število:', 'besedilo2': '', 'informacije': ''},
                                                    'Bellova števila': 

                                                    {'funkcija': bellova, 'stevilo_argumentov': 1, 'besedilo1': 'Kateri člen zaporedja Bellovih števil iščeš?:', 'besedilo2': '', 'informacije': ''},
                                                    'Catalanova števila': 

                                                    {'funkcija': catalanova,'stevilo_argumentov': 1, 'besedilo1': 'Kateri člen zaporedja Catalanovih števil iščeš?:', 'besedilo2': '', 'informacije': ''},
                                                    },
                                'Dvanajstera pot':  {'vrsta':       {'Vse preslikave': 1, 
                                                                    'Injekcija': 2,
                                                                    'Surjekcija': 3,
                                                                    'Bijekcija': 4
                                                                    }, 

                                                    'razlikovanje': {'Kroglice in škatle razlikujemo med seboj': 1, 
                                                                    'Kroglice razlikujemo, škatel ne': 2,
                                                                    'Škatle razlikujemo, kroglic ne': 3,
                                                                    'Kroglic in škatel ne razlikujemo med seboj': 4
                                                                    }
                                                    }
                                                    }