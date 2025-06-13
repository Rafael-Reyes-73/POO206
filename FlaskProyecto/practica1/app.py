from flask import Flask
app = Flask(__name__)

#ruta simple
@app.route('/')
def home():
    return '¡Hola, Flask!'

#ruta con un parámetro
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'

#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Página no encontradota', 404

#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#ruta POST
@app.route('/formulario', methods=['GET'])
def formulario():
    return 'Soy un formulario'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    