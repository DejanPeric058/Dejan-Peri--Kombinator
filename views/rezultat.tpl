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
Rezultat: {{funkcija(sez)}}
% end

<form action="/<razdelek>/<stevilo>/shrani_rezultat/" method="POST">
     <input  type="submit" value='Nazaj na naslovno stran' name='Nazaj na naslovno stran'>
     </form>