% rebase('base.tpl')
% from model import *
% from slovar import slovar_funkcij

<h2>
    {{razdelek}}
   </h2>

   <h2>
    {{stevilo}}
   </h2>

% podslovar = slovar_funkcij[razdelek][stevilo]



% if podslovar['stevilo_argumentov'] == 2 and stevilo != 'Multinomski koeficient':
<form action="/{{razdelek}}/{{stevilo}}/rezultat/" method="get">
{{podslovar['besedilo1']}}
            <input type="text" name="vrednost1">
{{podslovar['besedilo2']}}
            <input type="text" name="vrednost2">
            <input type="submit" value="Rezultat">

% elif podslovar['stevilo_argumentov'] == 1 and stevilo != 'Multinomski koeficient':
<form action="/{{razdelek}}/{{stevilo}}/rezultat/" method="get">
{{podslovar['besedilo1']}}
            <input type="text" name="vrednost1">
            <input type="submit" value="Rezultat">

% else:
%     if not slovar_funkcij[razdelek][stevilo]['argumenti_nastavljeni']:
%        slovar_funkcij[razdelek][stevilo]['argumenti_nastavljeni'] = True
<form action="/{{razdelek}}/{{stevilo}}/" method="get">
{{podslovar['besedilo1']}}
            <input type="text" name="stevilo_argumentov">
            <input type="submit" value="Naprej">
%     else:
         <form action="/{{razdelek}}/{{stevilo}}/rezultat/" method="GET">
%        for x in range(stevilo_argumentov):
   Vpiši {{x + 1}}. člen:
         <input  type="text" name='vrednost{{x + 1}}'>
% end
<input type="submit" value="Rezultat">
%

% end
