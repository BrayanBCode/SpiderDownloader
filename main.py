from flask import Flask, request, render_template
from logic.OpenBrowser import abrir_navegador_con_ip_y_puerto


app = Flask(__name__)

headings = ("index", "titulo", "Artista", "Duracion", "URL")
data = (
        ("1", "La morochaaaaaaaaaaaaaaaaaaaaaaa", "Emanero", "200" , "https://www.youtube.com/watch?v=OMkqDu4ElCA"),
        ("2", "La morocha", "Emanero", "200" , "https://www.youtube.com/watch?v=OMkqDu4ElCA"),
        ("3", "La morocha", "Emanero", "200" , "https://www.youtube.com/watch?v=OMkqDu4ElCA")
    )
        

@app.route('/search', methods=['POST'])
def procesar_formulario():
    if request.method == 'POST':
        name = request.form.get('search-bar')
        print(name)
        # Haz lo que necesites con el valor (por ejemplo, guárdalo en una base de datos)
        return render_template('index.html', headings=headings, data=data)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    abrir_navegador_con_ip_y_puerto()
    app.run(debug=True)
