% rebase('base.tpl')
% from slovar import slovar_funkcij

   <h1 align='center'>{{razdelek}}</h2>

   % if razdelek == 'Dvanajstera pot':
   
   <p>
      Ali kroglice in škatle razlikujemo med seboj ali ne?
   </p>

   % for x in slovar_funkcij[razdelek]['razlikovanje']:

      <form action="/{{razdelek}}/{{x}}/" method="GET">
      <input  type="submit" value='{{x}}' name={{x}}>
      </form>

   % end

   % else:

   <p>
      Kaj bi rad izračunal?
   </p>

   <p>
      % for x in slovar_funkcij[razdelek]:

      <form action="/{{razdelek}}/{{x}}/" method="GET">
      <input  type="submit" value='{{x}}' name={{x}}>
      </form>
        
   </p>

   % end


