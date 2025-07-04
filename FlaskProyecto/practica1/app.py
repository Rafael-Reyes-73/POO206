from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "ElMejorenBD"
app.config["MYSQL_DB"] = "dbflask"
app.secret_key = "mysecretkey"

mysql = MySQL(app)

@app.route("/DBCheck")
def dbCheck():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")
        return jsonify({"status": "Ok", "message": "Conectado con éxito"}), 200
    except MySQLdb.MySQLError as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

@app.route("/")
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, nombre_album FROM tb_albums")
    albums = cursor.fetchall()
    cursor.close()
    return render_template("formulario.html", albums=albums)

@app.route("/consulta")
def consulta():
    return render_template("consulta.html")

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f"¡Hola {nombre}!"

@app.errorhandler(404)
def paginaNoEncontrada(e):
    return "¡Cuidado, error de capa 8!", 404

@app.errorhandler(405)
def error505(e):
    return "¡Revisa el método de envío!", 405

@app.route("/usuario")
@app.route("/usuaria")
def dobleRoute():
    return "Soy el mismo recurso del servidor"

@app.route("/guardarAlbum", methods=["POST"])
def guardar():
    errores = {}

    titulo = request.form.get("txtTitulo", "").strip()
    artista = request.form.get("txtArtista", "").strip()
    year = request.form.get("txtYear", "").strip()

    if not titulo:
        errores["txtTitulo"] = "Nombre del álbum obligatorio"
    if not artista:
        errores["txtArtista"] = "Artista obligatorio"
    if not year:
        errores["txtYear"] = "Año de publicación obligatorio"
    elif not year.isdigit() or int(year) not in range(1800, 2101):
        errores["txtYear"] = "Ingresa un año válido"

    if not errores:
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO tb_albums (nombre_album, nombre_artista, anio_lanzamiento)
                VALUES (%s, %s, %s);
            """, (titulo, artista, year))
            mysql.connection.commit()
            flash("El álbum se guardó en la base de datos")
            return redirect(url_for("home"))
        except Exception as e:
            mysql.connection.rollback()
            flash(f"Algo falló: {e}")
            return redirect(url_for("home"))
        finally:
            cursor.close()

    return render_template("formUpdate.html", err=errores)
    

    
@app.route("/detalle/<int:id>")
def detalle(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_albums WHERE id = %s", (id,))
    album = cursor.fetchone()
    cursor.close()
    return render_template("consulta.html", album=album)






@app.route("/formUpdate/<int:id>")
def form_update(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_albums WHERE id = %s", (id,))
    album = cursor.fetchone()
    cursor.close()
    if album:
        return render_template("formUpdate.html", album=album)
    else:
        flash("Álbum no encontrado")
        return redirect(url_for("home"))



@app.route("/formElimi/<int:id>")
def form_elimi(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_albums WHERE id = %s", (id,))
    album = cursor.fetchone()
    cursor.close()
    if album:
        return render_template("formElimi.html", album=album)
    else:
        flash("Álbum no encontrado")
        return redirect(url_for("home"))


@app.route("/actualizarAlbum", methods=["POST"])
def actualizar_album():
    id_album = request.form["id"]
    titulo = request.form["titulo"]
    artista = request.form["artista"]
    anio = request.form["anio"]

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE tb_albums 
            SET nombre_album = %s, nombre_artista = %s, anio_lanzamiento = %s
            WHERE id = %s
        """, (titulo, artista, anio, id_album))
        mysql.connection.commit()
        flash("Álbum actualizado correctamente")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error al actualizar: {e}")
    finally:
        cursor.close()

    return redirect(url_for("home"))


@app.route("/eliminarAlbum", methods=["POST"])
def eliminar_album():
    
    album_id = request.form["id"] 
    
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE tb_albums
            SET state = 0 WHERE id = %s
            """, (album_id,))
        
        mysql.connection.commit()
        flash("Álbum eliminado correctamente")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error al eliminar: {e}")
    finally:
        cursor.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
