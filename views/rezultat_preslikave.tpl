% rebase('base.tpl')
% from slovar import slovar_funkcij
% from model import *

   <h2>
    {{razdelek}}
   </h2>

   <h2>
    {{razlikovanje}}
   </h2>

   <h2>
    {{vrsta}}
   </h2>

% preslikava = ustvari_preslikavo()
% preslikava.doloci_vrsto(slovar_funkcij[razdelek]['vrsta'][vrsta])
% preslikava.doloci_razlikovanje(slovar_funkcij[razdelek]['razlikovanje'][razlikovanje])
% rezultat = preslikava.stevilo_preslikav(vrednost1, vrednost2)

Rezultat: {{rezultat}}

% end



   <form action="/{{razdelek}}/shrani_rezultat/" method="POST">
     <input  type="submit" value='Nazaj na naslovno stran' name='Nazaj na naslovno stran'>
     </form>