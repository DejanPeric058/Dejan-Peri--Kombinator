% rebase('base.tpl')
% from slovar import slovar_funkcij

   <h2>
    {{razdelek}}
   </h2>

    <p>
       Kaj bi rad izračunal?
    </p>
    <p>
    % for x in slovar_funkcij[razdelek]:
        <form action="/{{razdelek}}/{{x}}/" method="GET">
        <input  type="submit" value='{{x}}' name={{x}}>
        </form>
   % end
        
    </p>


