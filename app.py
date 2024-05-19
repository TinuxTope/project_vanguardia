from flask import Flask, request, render_template, redirect, url_for, flash
from flask import request
import feedparser, os

app = Flask(__name__)
app.secret_key = '¡3248 97320983 bkjxdlrkfj k2 r9p874989387 98p78oiyylkhçç'


# Configuració per alternar a mode local o remot
MODE = 'remote'  # Cambia a 'local' per utilitzar els archius de mode locales
#MODE = 'local'

def get_rss(seccion, diario):
    try:
        if MODE == 'local':
            xml = os.path.join('rss', diario, f'{seccion}.xml')
        else:
            if diario == 'lavanguardia':
                xml = f"https://www.lavanguardia.com/rss/{seccion}.xml"
            elif diario == 'elpuntavui':
                if seccion == 'comunicacio':
                    xml = "http://www.elpuntavui.cat/comunicacio.feed?type=rss"
                elif seccion == 'societat':
                    xml = "http://www.elpuntavui.cat/societat.feed?type=rss"
                elif seccion == 'deportes':
                    xml = "http://www.elpuntavui.cat/territori.feed?type=rss"
                elif seccion == 'territori':
                    xml = "http://www.elpuntavui.cat/territori.feed?type=rss"
                elif seccion == 'politica':
                    xml = "http://www.elpuntavui.cat/territori.feed?type=rss"
        
        rss = feedparser.parse(xml)
        return rss
    except Exception as e:
        print(f"Error al obtener el feed RSS de {diario}: {e}")
        return None

def get_news_for_index():
    sections_lavanguardia = ['cultura', 'deportes', 'economia', 'politica', 'vida']
    sections_elpuntavui = ['comunicacio', 'societat', 'territori', 'politica','deportes']
    noticias = {'lavanguardia': {}, 'elpuntavui': {}}

    for section in sections_lavanguardia:
        rss = get_rss(section, 'lavanguardia')
        if rss and rss.entries:
            primera_noticia = rss.entries[0]
            if 'media_content' in primera_noticia and primera_noticia.media_content:
                primera_noticia.image = primera_noticia.media_content[0]['url']
            elif 'media_thumbnail' in primera_noticia and primera_noticia.media_thumbnail:
                primera_noticia.image = primera_noticia.media_thumbnail[0]['url']
            else:
                primera_noticia.image = None
            noticias['lavanguardia'][section] = primera_noticia
    
    for section in sections_elpuntavui:
        rss = get_rss(section, 'elpuntavui')
        if rss and rss.entries:
            primera_noticia = rss.entries[0]
            # Asignar imágenes predefinidas según la sección
            primera_noticia.image = f"/static/img/{section}.jpg"
            noticias['elpuntavui'][section] = primera_noticia

    return noticias

@app.route('/')
def index():
    noticias = get_news_for_index()
    return render_template('index.html', noticias=noticias)

@app.route('/lavanguardia')
def lavanguardia():
    noticias = get_news_for_index()['lavanguardia']
    return render_template('indexVanguardia.html', noticias=noticias)

@app.route('/lavanguardia/<seccio>')
def lavanguardia_section(seccio):
    rss = get_rss(seccio, 'lavanguardia')
    return render_template("lavanguardia.html", rss=rss)

@app.route('/elpuntavui')
def elpuntavui():
    noticias = get_news_for_index()['elpuntavui']
    return render_template('indexpuntdavui.html', noticias=noticias)

@app.route('/elpuntavui/<seccio>')
def elpuntavui_section(seccio):
    rss = get_rss(seccio, 'elpuntavui')
    return render_template("elpuntavui.html", rss=rss)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)