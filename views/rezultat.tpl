% rebase('base.tpl')
% from model import *
% from slovar import slovar_funkcij

   <h2>
    {{stevilo}}
   </h2>

% funkcija = slovar_funkcij[stevilo]['funkcija']
% if slovar_funkcij[stevilo]['stevilo_argumentov'] == 2:
Rezultat: {{funkcija(vrednost1, vrednost2)}}
% else:
Rezultat: {{funkcija(vrednost1)}}
% end

<form action="/" method="GET">
     <input  type="submit" value='Nazaj na naslovno stran' name='Nazaj na naslovno stran'>
     </form>