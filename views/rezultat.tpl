% rebase('base.tpl')
% from model import *
% from slovar import slovar_funkcij

    <h1 align='center'>{{razdelek}}</h1>

    <h2>{{stevilo}}</h2>

    % funkcija = slovar_funkcij[razdelek][stevilo]['funkcija']

    <p>
        Rezultat: {{funkcija(sez)}}
    </p>

    % end

    <form action="/{{stevilo}}/shrani_rezultat/" method="POST">
        <input type="submit" value='Nazaj na naslovno stran' name='Nazaj na naslovno stran'>
        </form>