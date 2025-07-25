from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModels import *

albumBP = Blueprint("albumBP", __name__)

#ruta de inicio
@albumBP.route("/inicio")
def home():
    try:
        consultaTodos = getAll()
        return render_template("formulario.html", errores={}, albums=consultaTodos)
    except Exception as e:
        print("Error al obtener los álbumes:"+ str(e))  
        return render_template("formulario.html", errores={}, albums=[])

#ruta album detalles
@albumBP.route("/detallesAlbum/<int:id>")
def detalle(id):
    
    try:
        consultaId = getById(id)
        return render_template("consulta.html", album=consultaId)
    except Exception as e:
        print("Error al obtener el álbum por ID: " + str(e))
        return redirect(url_for("home"))



#ruta para guardar un nuevo album
@albumBP.route("/insertarAlbum", methods=["POST"])
def guardar():
    
    #lista de errores
    
    errores = {}

    tituloV = request.form.get("txtTitulo", "").strip()
    artistaV = request.form.get("txtArtista", "").strip()
    yearV = request.form.get("txtYear", "").strip()

    if not tituloV:
        errores["txtTitulo"] = "Nombre del álbum obligatorio"
    if not artistaV:
        errores["txtArtista"] = "Artista obligatorio"
    if not yearV:
        errores["txtYear"] = "Año de publicación obligatorio"
    elif not yearV.isdigit() or int(yearV) not in range(1800, 2101):
        errores["txtYear"] = "Ingresa un año válido"

    if not errores:
        try:
            insertAlbum(tituloV, artistaV, yearV)
            flash("Album guardado en BD")
            return redirect(url_for("home"))
        
        except Exception as e:
            mysql.connection.rollback()
            flash(f"Algo falló: {e}")
            return redirect(url_for("home"))

    return render_template("formUpdate.html", err=errores)
    
#ruta para editar un album
@albumBP.route("/formUpdate/<int:id>")
def editar(id):
    try:
        consultaId = getById(id)
        return render_template("formUpdate.html", album=consultaId)
    except Exception as e:
        print("Error al consultar por ID: " + str(e))
        return redirect(url_for("home"))
    
#ruta para actualizar un album
@albumBP.route("/actualizarAlbum", methods=["POST"])
def actualizar():
    errores = {}

    id_albumV = request.form.get("txtId", "").strip()
    tituloV = request.form.get("txtTitulo", "").strip()
    artistaV = request.form.get("txtArtista", "").strip()
    yearV = request.form.get("txtYear", "").strip()

    if not tituloV:
        errores["txtTitulo"] = "Nombre del álbum obligatorio"
    if not artistaV:
        errores["txtArtista"] = "Artista obligatorio"
    if not yearV:
        errores["txtYear"] = "Año de publicación obligatorio"
    elif not yearV.isdigit() or int(yearV) not in range(1800, 2101):
        errores["txtYear"] = "Ingresa un año válido"

    if not errores:
        try:
            
            updateAlbum(id_albumV, tituloV, artistaV, yearV)
            flash("Album actualizado en BD")
            return redirect(url_for("home"))
        
        except Exception as e:
            mysql.connection.rollback()
            flash(f"Algo falló: {e}")
            return redirect(url_for("home"))

    return render_template("formUpdate.html", err=errores)

#ruta conformación para eliminar un album
@albumBP.route("/confirmarEliminar/<int:id>")   
def confirmar_eliminar(id):
    try:
        consultaId = getById(id)
        return render_template("confirmarEliminar.html", album=consultaId)
    except Exception as e:
        print("Error al consultar por ID: " + str(e))
        return redirect(url_for("home"))

#ruta para ejecutar delete logico de un album
@albumBP.route("/eliminarAlbum/<int:id>", methods=["POST"])
def softDel(id):
    try:
        softDeleteAlbum(id)
        flash("Album eliminado de la BD")
        return redirect(url_for("home"))
    except Exception as e:
        mysql.connection.rollback()
        flash("Algo falló al eliminar:"+ str(e))
    return redirect(url_for("home"))

