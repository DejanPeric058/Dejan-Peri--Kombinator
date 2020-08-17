% rebase('base.tpl')
% from slovar import slovar_funkcij

   <h1 align='center'>{{razdelek}}</h2>

   <h2>{{razlikovanje}}</h2>

   <h2>{{vrsta}}</h2>

   <form action="/{{razdelek}}/{{razlikovanje}}/{{vrsta}}/rezultat/" method="get">

   <p>
      Vpiši število kroglic:
   </p>

   <input type="text" name="vrednost1">

   <p>
      Vpiši število škatel:
   </p>

   <input type="text" name="vrednost2">
   <input type="submit" value="Rezultat">