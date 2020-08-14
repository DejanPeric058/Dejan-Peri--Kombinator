% rebase('base.tpl')
% from model import *
% from slovar import slovar_funkcij

<h2>
    {{razdelek}}
   </h2>

   <h2>
    {{stevilo}}
   </h2>

% funkcija = slovar_funkcij[razdelek][stevilo]['funkcija']
% if stevilo == 'Multinomski koeficient':
Rezultat: {{funkcija(sez)}}

% elif slovar_funkcij[razdelek][stevilo]['stevilo_argumentov'] == 1:
Rezultat: {{funkcija(vrednost1)}}
%else:
Rezultat: {{funkcija(vrednost1, vrednost2)}}
% end

% end
<form action="/" method="GET">
     <input  type="submit" value='Nazaj na naslovno stran' name='Nazaj na naslovno stran'>
     </form>