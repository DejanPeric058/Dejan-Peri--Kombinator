% rebase('base.tpl')
% from slovar import slovar_funkcij

   <h1 align='center'>{{razdelek}}</h2>

   <h2>{{razlikovanje}}</h2>

   <p>
   Kakšno vrsto preslikave imaš?
   </p>

   % for x in slovar_funkcij[razdelek]['vrsta']:

   <form action="/{{razdelek}}/{{razlikovanje}}/{{x}}/" method="GET">
      <input  type="submit" value='{{x}}' name={{x}}>
      </form>
   % end