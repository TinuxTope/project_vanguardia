# Projecte UF3 de M04

En primer lloc llegirem el projecte senser per poder desglossar cada punt i realitzar el projecte de la manera més óptima. 

Anirem al moddle i llegirem el [enunciat](https://docs.google.com/document/d/1OAJ40NJdOlQ4mXJZNoZc6ndVE9ot2GPl5HTI5l9fYQk/edit#heading=h.6sziurxns69f)

En el anunciat ens deriva en un codi de partida [codi](https://github.com/jmirinformatica/1asixdaw-m04/tree/main/python/flask-rss)

El objectiu del projecte es poder entendre i aplicar uns continguts: 

1. ### <span style="color:green">Entorns virtuals a Python (.venv).</span>

Els entorns virtuals en Python (.venv) són eines que permeten crear un espai aïllat per a cada projecte, on les seves biblioteques i dependències es poden gestionar de manera independent del sistema global. Aquesta funcionalitat és útil quan tens diversos projectes que requereixen versions diferents de les mateixes biblioteques, ja que evita conflictes entre elles.
Podem trobar [més informació](https://docs.python.org/es/3/library/venv.html) sobre creació d'entorns virtuals. 

>> Per crear un entorn virtual en Python utilitzant la eina .venv, pots seguir aquest procediment:

- Navega fins al directori del teu projecte.
```python
cd ruta/al/directoride/projecte_UF3
```
- Executa la comanda python3 -m venv nom_del_entorn per crear un nou entorn virtual. 
```python
python -m venv .venv
```
- Activa l'entorn virtual amb la comanda source.
```
\.venv\Scripts\activate (.venv)
```
- Per saber si estas dins veuras un prompt:
```
.\.venc\Scripts\activate (.venv)
```

A partir d'ara, tot el que instal·lem amb pip es guardarà dins l'entorn virtual, i les dependències del nostre projecte es mantindran separades de les altres instal·lacions de Python en el sistema.

- En aquest punt podriem instal·lar els paquets necessaris per treballar com: 
```
pip install flask
pip install feedparser
```

Això et permet tenir un control de les biblioteques que utilitza cada projecte i facilita la col·laboració amb altres desenvolupadors, ja que poden reproduir exactament l'entorn de treball utilitzant l'arxiu requirements.txt que conté totes les dependències del projecte.

per facilitar l'integració amb el VisualCode i l'entorn visual tenim [l'extenció](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager)

- Per resortir del entorn virtual es necessari executar:

```
deactivate
```

>> En el projecte ja ens han facilitat els requeriments.txt per aquest motiu no cal fer els passos inicial, sino instalamos los requerimientos 

### <span style="color:green">Flask, conceptes bàsics.</span>

Flask és un marc de treball web minimalista per a Python. És lleuger i flexible, el que el fa perfecte per a projectes petits o mitjans. En aquest context, ens centrarem en comprendre com gestionar les sol·licituds GET, que són peticions a un servidor web per obtenir informació, sense entrar en aspectes més complicats com el maneig de formularis.

Per començar amb Flask, normalment instal·les Flask a través de pip, el gestor de paquets de Python, amb la comanda:
```
pip install flask
```
Un cop instal·lat Flask, pots crear una aplicació web senzilla amb només unes quantes línies de codi Python. Aquí tens un exemple bàsic d'una aplicació web Flask que respon a peticions GET:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola, món!'

if __name__ == '__main__':
    app.run(debug=True)
```

En aquest codi, importem la classe Flask del mòdul flask, i després creem una instància de la classe Flask anomenada app. Llavors, utilitzem el decorador @app.route('/') per indicar a Flask que la funció hello() hauria de ser cridada quan es rebi una petició GET a la ruta principal del servidor (/). Finalment, si executem aquest script directament (__name__ == '__main__'), Flask posarà en marxa el servidor web, i estarem escoltant a la direcció http://127.0.0.1:5000/ (això és el que significa app.run(debug=True)).

Quan executis aquest script, si obres un navegador web i accedeixes a http://127.0.0.1:5000/, veuràs el text "Hola, món!" que retorna la funció hello(). Això és una resposta a la petició GET que el navegador envia al servidor.

Iniciar l'aplicació: Per executar la teva aplicació, obre una terminal o símbol del sistema, navega fins al directori on tens el fitxer de l'aplicació i executa el fitxer Python. Per exemple, si el teu fitxer s'anomena app.py, pots fer el següent:
```python
python app.py
```
<span style="color:purple">***python -m flask run***</span>: Aquesta comanda utilitza el mòdul flask de Python per iniciar l'aplicació. No necessites especificar el nom del fitxer de l'aplicació, ja que Flask detectarà automàticament l'aplicació en funció de determinades convencions de noms de fitxers i variables d'entorn. Això és útil quan tens una estructura de directoris estàndard per al teu projecte Flask. Aquesta comanda també habilita el mode de depuració de Flask de manera predeterminada.

<span style="color:purple">flask run --debug</span>: Aquesta comanda utilitza l'ordre flask directament i permet especificar opcions addicionals. En aquest cas, l'opció --debug habilita el mode de depuració de Flask, que mostra informació detallada sobre els errors i recarrega automàticament l'aplicació quan es fan canvis en els fitxers de codi font. Aquesta comanda també detectarà l'aplicació Flask a partir de determinades convencions de noms de fitxers i variables d'entorn.

### <span style="color:green">Jinja, el sistema de plantilles de flask</span>

Jinja és el motor de plantilles que utilitza Flask. Aquesta eina et permet generar HTML de manera dinàmica, insertant valors de variables, creant estructures condicionals (if) i bucles (for). 

Per mostrar variables a una plantilla de Jinja, primer has de passar les variables des del teu codi Python a la plantilla. Pots fer-ho mitjançant el mètode render_template() de Flask. Un cop les variables són passades, pots accedir-hi a la plantilla mitjançant les etiquetes de doble claudàtor {{ }}.

```html
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plantilla amb Jinja</title>
</head>
<body>
    <h1>Hola, {{ nom }}</h1>
</body>
</html>
```
Per utilitzar estructures condicionals (if) a Jinja, pots emprar la sintaxi similar a la de Python:

```html
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plantilla amb Jinja</title>
</head>
<body>
    {% if hora < 12 %}
        <p>Bon dia!</p>
    {% else %}
        <p>Bona tarda!</p>
    {% endif %}
</body>
</html>
```

Utilitzar bucles (for) a Jinja, pots fer-ho amb la següent sintaxi:
```html
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plantilla amb Jinja</title>
</head>
<body>
    <ul>
        {% for fruita in llista_fruites %}
            <li>{{ fruita }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```