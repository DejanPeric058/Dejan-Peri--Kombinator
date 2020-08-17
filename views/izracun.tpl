% rebase('base.tpl')
% from slovar import slovar_funkcij
% import bottle

   <h1 align='center'>{{razdelek}}</h1>

   <h2>{{stevilo}}</h2>

   % podslovar = slovar_funkcij[razdelek][stevilo]
   % if podslovar['stevilo_argumentov'] == 2 and stevilo != 'Multinomski koeficient':

   <form action="/{{razdelek}}/{{stevilo}}/rezultat/" method="get">

   <p>
      {{podslovar['besedilo1']}}
   </p>

      <input type="text" name="vrednost1">

   <p>
      {{podslovar['besedilo2']}}
   </p>

      <input type="text" name="vrednost2">
      <input type="submit" value="Rezultat">

   % elif podslovar['stevilo_argumentov'] == 1 and stevilo != 'Multinomski koeficient':

   <form action="/{{razdelek}}/{{stevilo}}/rezultat/" method="get">

   <p>
      {{podslovar['besedilo1']}}
   </p>

      <input type="text" name="vrednost1">
      <input type="submit" value="Rezultat">

   % else:
   % if bottle.request.query.getunicode('stevilo argumentov') == None:

   <form action="/{{razdelek}}/{{stevilo}}/" method="get">

   <p>
      {{podslovar['besedilo1']}}
   </p>

      <input type="text" name="stevilo argumentov">
      <input type="submit" value="Naprej">

   % else:

      <form action="/{{razdelek}}/{{stevilo}}/rezultat/" method="GET">

   % for x in range(stevilo_argumentov):

   <p>
      Vpiši {{x + 1}}. člen:
   </p>

      <input  type="text" name='vrednost{{x + 1}}'>

   % end

   <input type="submit" value="Rezultat">

   % end
