from flask_mysqldb import MySQL
###from MySQLdb import cursors

def registrarUsuario(datos, mysql):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO usuario (usuario, nombre, apellido, mail, contra, sexo, fecha_nacimiento, altura, peso, cintura, cuello, caderas) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", {7}, {8}, {9}, {10}, {11})'.format
    (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11]))
    mysql.connection.commit()

def coincidenciasMail(datos, mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT usuario,mail FROM usuario WHERE mail="{0}"'.format(datos[3]))
    coincidenciasMail= cur.fetchall()
    return coincidenciasMail

def coincidenciasUsuario(datos, mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT usuario,mail FROM usuario WHERE usuario="{0}"'.format(datos[0]))
    coincidenciasUsuario= cur.fetchall()
    return coincidenciasUsuario

def estaRegistrado(mysql, usuario, contrasenia):
    cur= mysql.connection.cursor()
    cur.execute('SELECT u.id_usuario FROM usuario u WHERE (u.usuario= %s or u.mail=%s) AND u.contra=%s', (usuario, usuario, contrasenia))
    datosUsuario= cur.fetchall()
    return datosUsuario

def seleccionarIdRutina(mysql, rutina):
    cur= mysql.connection.cursor()
    cur.execute('SELECT id_rutina FROM rutina WHERE nombre="{0}"'.format(rutina))
    idrutina=cur.fetchall()
    return idrutina

def registrarHistorial(mysql, idrutina, ej, pesos, repeticiones, descansos):
    cur= mysql.connection.cursor()
    print("idrutina", idrutina, "ejercicio", ej, "pesos", pesos, "repeticiones", repeticiones, "descansos", descansos)
    cur.execute('INSERT into historial_rutina(id_rutina, id_ejerc, fecha_realizacion, peso, repeticiones, descanso) VALUES (%s, %s , CURDATE(), %s, %s, %s)', [idrutina, ej, pesos, repeticiones, descansos])
    mysql.connection.commit()

def datosEjercicioRutina(mysql,id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT r.id_rutina, e.id_ejercicio, e.nombre, re.peso, re.repeticiones, re.series, re.descanso FROM usuario_rutina ur JOIN rutina r ON r.id_rutina=ur.id_rutina JOIN rutina_ejercicio re ON r.id_rutina=re.id_rutina JOIN ejercicio e ON e.id_ejercicio=re.id_ejercicio WHERE ur.id_usuario={0}'.format(id))
    return cur.fetchall()

def rutinasUsuario(mysql,id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT distinct(r.id_rutina), r.nombre FROM usuario_rutina ur JOIN rutina r ON r.id_rutina=ur.id_rutina WHERE ur.id_usuario={0}'.format(id))
    return cur.fetchall()

def seleccionarNombreRutina(mysql, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('SELECT r.nombre FROM rutina r WHERE r.id_rutina={0}'.format(idrutina))
    nombreRutina= cur.fetchall()
    nombreRutina=nombreRutina[0][0]
    return nombreRutina

def seleccionarEjerciciosRutina(mysql, idusuario, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('SELECT e.id_ejercicio, e.nombre, re.peso, re.repeticiones, re.series, re.descanso FROM usuario_rutina ur JOIN rutina r ON r.id_rutina=ur.id_rutina JOIN rutina_ejercicio re ON r.id_rutina=re.id_rutina JOIN ejercicio e ON e.id_ejercicio=re.id_ejercicio WHERE ur.id_usuario={0} AND r.id_rutina={1}'.format(idusuario, idrutina))
    ejercicios= cur.fetchall()
    return ejercicios

def seleccionarUsuario(mysql, id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT usuario, nombre, apellido, mail, contra, sexo, fecha_nacimiento, altura, peso, cintura, cuello, caderas FROM usuario WHERE id_usuario={0}'.format(id))
    usuario= cur.fetchall()
    return usuario[0]
def rutinaRepetida(mysql, rutina,idusuario):
    cur= mysql.connection.cursor()
    cur.execute('SELECT r.nombre FROM rutina r JOIN usuario_rutina ur ON r.id_rutina=ur.id_rutina JOIN usuario u ON u.id_usuario=ur.id_usuario WHERE r.nombre="{0}" and u.usuario = "{1}"'.format(rutina, idusuario))
    return cur.fetchall()

def registrarRutina(mysql, rutina):
    cur= mysql.connection.cursor()
    cur.execute('INSERT into rutina(fecha, nombre, estado) VALUES (CURDATE(), %s , "Creada")', [rutina])
    mysql.connection.commit()

def ultimaRutina(mysql):
    cur= mysql.connection.cursor()
    cur.execute('SELECT max(id_rutina) FROM rutina')
    idrutina=cur.fetchall()
    return idrutina[0][0]

def datosEjercicios(mysql):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM ejercicio')
    return cur.fetchall()

def registrarRutinaUsuario(mysql, idusuario, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('INSERT into usuario_rutina(id_usuario, id_rutina, fecha_rutina) VALUES (%s, %s , CURDATE())', [idusuario, idrutina])
    mysql.connection.commit()

def seleccionFechaRutina(mysql, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('SELECT fecha FROM rutina WHERE id_rutina= {0}'.format(idrutina)) 
    fecharutina= cur.fetchall()
    return fecharutina[0][0]
    
def seleccionarIdEjercicio(mysql, nombreEjercicio):
    cur= mysql.connection.cursor()
    cur.execute('SELECT id_ejercicio FROM ejercicio WHERE nombre= %s' , [nombreEjercicio]) 
    idejercicio= cur.fetchall()
    return idejercicio[0][0]

def registrarRutinaEjercicio(mysql, fecharutina, idrutina, idejercicio, descansos, repeticiones, peso, series):
    cur= mysql.connection.cursor()
    cur.execute('INSERT into rutina_ejercicio(fecha_rutina, id_rutina, id_ejercicio, descanso, repeticiones, peso, series) VALUES( %s, %s, %s, %s, %s, %s, %s )',
    (fecharutina, idrutina, idejercicio, descansos, repeticiones, peso, series))
    mysql.connection.commit()

def modificarRutina(mysql, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('UPDATE rutina r SET fecha=CURDATE() WHERE r.id_rutina={0}'.format(idrutina))
    cur.execute('DELETE FROM rutina_ejercicio WHERE id_rutina={0}'.format(idrutina))
    mysql.connection.commit()  

def eliminarRutina(mysql, usuario, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('DELETE FROM rutina_ejercicio WHERE id_rutina = {0}'.format(idrutina))
    cur.execute('DELETE FROM usuario_rutina WHERE id_rutina ={0} and id_usuario={1}'.format(idrutina, usuario))
    cur.execute('DELETE FROM rutina WHERE id_rutina = {0}'.format(idrutina))
    mysql.connection.commit()

def registrarEjercicio(mysql, nombre, descrip):
    cur= mysql.connection.cursor()
    cur.execute('INSERT INTO ejercicio(nombre, descripcion) VALUES (%s, %s)', (nombre, descrip))
    mysql.connection.commit()

def historialEjerciciosRutina(mysql, idusuario, idrutina):
    cur= mysql.connection.cursor()
    cur.execute('SELECT hr.fecha_realizacion, e.id_ejercicio, e.nombre, hr.peso, hr.repeticiones, hr.descanso FROM  historial_rutina hr  JOIN rutina r ON hr.id_rutina=r.id_rutina JOIN rutina_ejercicio re ON hr.id_rutina=re.id_rutina and hr.id_ejerc=re.id_ejercicio JOIN ejercicio e ON e.id_ejercicio=re.id_ejercicio WHERE hr.id_rutina={0} ORDER BY(hr.id_historial)'.format(idrutina))
    ejercicios= cur.fetchall()
    return ejercicios

def datos_usuario(mysql, id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT sexo, altura, peso, cintura, cuello, caderas FROM usuario WHERE id_usuario={0}'.format(id))
    datos= cur.fetchall()
    return datos

def actualizar_perfil(mysql, id, altura, peso, cintura, cuello, cadera):
    cur= mysql.connection.cursor()
    cur.execute('UPDATE usuario u SET altura={0}, peso={1}, cintura={2}, cuello={3}, caderas={4} WHERE u.id_usuario={5}'.format(altura, peso, cintura, cuello, cadera, id))
    mysql.connection.commit()

def registrar_historial(mysql, id, imc, m_basal, p_grasa):
    cur= mysql.connection.cursor()
    cur.execute('INSERT INTO historial_usuario(id_usuario, imc, metabolismo_basal, porcentaje_grasa, fecha_historial) VALUES ({0}, {1}, {2}, {3}, CURDATE())'.format(id, imc,m_basal, p_grasa))
    mysql.connection.commit()

def fecha(mysql, id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT fecha_nacimiento FROM usuario WHERE id_usuario={0}'.format(id))
    fecha= cur.fetchall()
    return fecha[0][0]


def sexo(mysql, id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT sexo FROM usuario WHERE id_usuario={0}'.format(id))
    sexo= cur.fetchall()
    return sexo[0]

def historial_usuario(mysql, id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT imc, metabolismo_basal, porcentaje_grasa, fecha_historial FROM historial_usuario WHERE id_usuario={0} ORDER BY(id_historial_usuario)'.format(id))
    historial= cur.fetchall()
    return historial