% rebase('base.tpl')
% from slovar import slovar_funkcij
% import model

   <h1 align='center'>Kombinator</h1>

   <h2>
      Dobrodošli v Kombinator! 
   </h2>
   <p>
      Izberite, katero kombinatorično število bi radi izračunali:

      % for x in slovar_funkcij:
      <form action="/{{x}}/" method="GET">
      <input  type="submit" value='{{x}}' name={{x}}>
      </form>
      % end
   </p>

   <p><b>Najbolj iskana kombinatorična števila:</b></p>
   
   % for x in zbirka_stevil.prikazi_najbolj_iskane():

   <ul>
      <li> {{x}} </li>
   </ul>

   % end
 


