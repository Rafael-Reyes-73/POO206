from app import app, mysql

#metodo para obtener albumes activos
def getAll():
    cursor = mysql.connect()
    cursor.execute("SELECT * FROM tb_albums WHERE active = 1")
    consultaTodo = cursor.fetchall()
    cursor.close()
    return consultaTodo

#obtener album por id
def getById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_albums WHERE id = %s", (id,))
    consultaId = cursor.fetchone()
    consultaId.close()
    return consultaId

#metodo para insertar un nuevo album
def insertAlbum(tituloV, artistaV, anioV):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO tb_albums (nombre_album, nombre_artista, anio_lanzamiento) 
        VALUES (%s, %s, %s)
    """, (tituloV, artistaV, anioV))
    mysql.connection.commit()
    cursor.close()
    
#mwtodo para actualizar un album
def updateAlbum(id_albumV, tituloV, artistaV, anioV):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE tb_albums 
        SET nombre_album = %s, nombre_artista = %s, anio_lanzamiento = %s
        WHERE id = %s
    """, (tituloV, artistaV, anioV, id_albumV))
    mysql.connection.commit()
    cursor.close()
    
#metodo para eliminar un album
def softDeleteAlbum(id_albumV):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE FROM tb_albums set state=%s WHERE id = %s", (0,id))
    mysql.connection.commit()
    cursor.close()
    
    