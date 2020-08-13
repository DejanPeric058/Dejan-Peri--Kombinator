
% rebase('base.tpl')
% from slovar import slovar_funkcij

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


