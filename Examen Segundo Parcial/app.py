from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ElMejorenBD'
app.config['MYSQL_DB'] = 'dbflask_peliculas'

mysql = MySQL(app)

@app.route("/")
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, titulo FROM tb_peliculas WHERE estado = 1")
    pelicula = cursor.fetchall()
    cursor.close()
    return render_template("formulario.html", pelicula=pelicula)

@app.route("/guardarPelicula", methods=["POST"])
def guardar_pelicula():
    errores = {}
    titulo = request.form.get("titulo", "").strip()
    director = request.form.get("director", "").strip()
    anio = request.form.get("anio", "").strip()
    genero = request.form.get("genero", "").strip()

    if not titulo:
        errores["titulo"] = "Título obligatorio"
    if not director:
        errores["director"] = "Director obligatorio"
    if not anio or not anio.isdigit() or not (1800 <= int(anio) <= 2100):
        errores["anio"] = "Año inválido (1800-2100)"
    if not titulo:
        errores["genero"] = "Genero obligatorio"

    if errores:
        return render_template("formulario.html", errores=errores, request=request, pelicula=[])

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tb_peliculas (titulo, director, anio_lanzamiento, genero) VALUES (%s, %s, %s, %s)", (titulo, director, anio, genero))
        mysql.connection.commit()
        flash("Pelicula guardado correctamente")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error al guardar: {e}")
    finally:
        cursor.close()

    return redirect(url_for("home"))

@app.route("/detalle/<int:id>")
def detalle(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_peliculas WHERE id = %s", (id,))
    pelicula = cursor.fetchone()
    cursor.close()
    return render_template("consulta.html", pelicula=pelicula)



@app.route("/formUpdate/<int:id>")
def form_update(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_peliculas WHERE id = %s", (id,))
    pelicula = cursor.fetchone()
    cursor.close()
    return render_template("formUpdate.html", pelicula=pelicula)

@app.route("/actualizarPelicula", methods=["POST"])
def actualizar_pelicula():
    errores = {}
    id_pelicula = request.form["id"]
    titulo = request.form.get("titulo", "").strip()
    director = request.form.get("director", "").strip()
    anio = request.form.get("anio", "").strip()
    genero = request.form.get("genero", "").strip()
    
    if not titulo:
        errores["titulo"] = "Título obligatorio"
    if not director:
        errores["director"] = "Director obligatorio"
    if not anio or not anio.isdigit() or not (1800 <= int(anio) <= 2100):
        errores["anio"] = "Año inválido (1800-2100)"
    if not titulo:
        errores["genero"] = "Genero obligatorio"

    if errores:
        return render_template("formUpdate.html", errores=errores, request=request, pelicula=[])

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tb_peliculas SET titulo = %s, director = %s, anio_lanzamiento = %s, genero = %s WHERE id = %s", (titulo, director, anio, genero, id_pelicula))
        mysql.connection.commit()
        flash("Pelicula Actualizada correctamente")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error al Actualizar: {e}")
    finally:
        cursor.close()

    return redirect(url_for("home"))


@app.route("/formElimi/<int:id>")
def form_elimi(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_peliculas WHERE id = %s", (id,))
    pelicula = cursor.fetchone()
    cursor.close()
    return render_template("formEliminar.html", pelicula=pelicula)

@app.route("/eliminarPelicula", methods=["POST"])
def eliminar_pelicula():
    id_pelicula = request.form["id"]
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tb_peliculas SET estado = 0 WHERE id = %s", (id_pelicula,))
        mysql.connection.commit()
        flash("Pelicula eliminado correctamente")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error al eliminar: {e}")
    finally:
        cursor.close()

    return redirect(url_for("home"))

@app.errorhandler(404)
def error_404(e):
    return "Página no encontrada", 404

@app.errorhandler(405)
def error_405(e):
    return "Método no permitido", 405



if __name__ == "__main__":
    app.run(port=3000, debug=True)
