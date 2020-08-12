% rebase('base.tpl')
% from model import *
% from slovar import slovar_funkcij

   <h2>
    {{stevilo}}
   </h2>

% podslovar = slovar_funkcij[stevilo]



% if podslovar['stevilo_argumentov'] == 2:
<form action="/rezultat/{{stevilo}}/" method="get">
{{podslovar['besedilo1']}}
            <input type="text" name="vrednost1">
{{podslovar['besedilo2']}}
            <input type="text" name="vrednost2">
            <input type="submit" value="Rezultat">

% elif podslovar['stevilo_argumentov'] == 1:
<form action="/rezultat/{{stevilo}}/" method="get">
{{podslovar['besedilo1']}}
            <input type="text" name="vrednost1">
            <input type="submit" value="Rezultat">

% else:
%     if not slovar_funkcij[stevilo]['argumenti_nastavljeni']:
%        slovar_funkcij[stevilo]['argumenti_nastavljeni'] = True
<form action="/izracun/{{stevilo}}/" method="get">
{{podslovar['besedilo1']}}
            <input type="text" name="stevilo_argumentov">
            <input type="submit" value="Naprej">
%     else:
         <form action="/rezultat/{{stevilo}}/" method="GET">
%        for x in range(stevilo_argumentov):
   Vpiši {{x + 1}}. člen:
         <input  type="text" name='vrednost{{x}}'>
% end
<input type="submit" value="Rezultat">
%

% end
