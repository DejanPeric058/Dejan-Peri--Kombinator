% rebase('base.tpl')
% from slovar import slovar_funkcij

   <h2>
    Osnovne kombinatorične funkcije
   </h2>

    <p>
       Kaj bi rad izračunal?
    </p>
    <p>
    % for x in slovar_funkcij:
        <form action="/izracun/{{x}}/" method="GET">
        <input  type="submit" value='{{x}}' name={{x}}>
        </form>
   % end
        
    </p>


