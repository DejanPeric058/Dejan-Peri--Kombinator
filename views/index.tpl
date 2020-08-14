
% rebase('base.tpl')
% from slovar import slovar_funkcij
% import model

   <h2>
    Navodila
   </h2>

    <p>
       Dobrodošli v Kombinator! 
    </p>
    <p>
        Izberite, katero kombinatorično število bi radi izračunali:
        % for x in slovar_funkcij:
        <form action="/{{x}}/" method="GET">
        <input  type="submit" value='{{x}}' name={{x}}>
        </form>
   % end
    </p>

   <p>
   Tri najbolj iskana kombinatorična števila:
   </p>
   
   % for x in zbirka_stevil.prikazi_najbolj_iskane():
   <p>
   {{x}}
   </p>
   % end
 


