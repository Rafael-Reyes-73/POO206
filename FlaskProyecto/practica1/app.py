from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ElMejorenBD'
app.config['MYSQL_DB'] = 'dbflask'
app.config['MYSQL_PORT'] = 3306 
mysql = MySQL(app)

#ruta para probar la conexión a la base de datos
@app.route('/DBCheck')
def DBCheck():
    try:
        cur = mysql.connection.cursor()
        cur.execute("Select 1")
        return jsonify({'status': 'ok','message': 'Conexion exitosa a la base de datos'}), 200
    except MySQLdb.MySQLError  as e:
        return jsonify({'status': 'error','message':str (e)}), 500
    #excepcion de contraseña incorrecta
    except MySQLdb.OperationalError as e:
        return jsonify({'status': 'error','message': 'Error de conexión a la base de datos: ' + str(e)}), 500
    #excepcion de base de datos no encontrada
    except MySQLdb.DatabaseError as e:
        return jsonify({'status': 'error','message': 'Base de datos no encontrada: ' + str(e)}), 500
    #excepcion usurio incorrecto
    except MySQLdb.ProgrammingError as e:
        return jsonify({'status': 'error','message': 'Usuario o contraseña incorrectos: ' + str(e)}), 500
    #excepcion host in9correcto
    except MySQLdb.InterfaceError as e:
        return jsonify({'status': 'error','message': 'Host incorrecto: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
    


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

@app.errorhandler(404)
def metodonoP(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST) !!!', 405

#ruta POST
@app.route('/formulario', methods=['POST'])
def formulario():
    return 'Soy un formulario'