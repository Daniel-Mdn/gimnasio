from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session
import flask
from flask.globals import request
from flask.wrappers import Request
from Database import db
import forms, functions
from flask import session

def registraUsuario(mysql, request, registerForm):
    datos=[]
    datos.append(request.form['usuario'])
    datos.append(request.form['nombre'])
    datos.append(request.form['apellido'])
    datos.append(request.form['mail'])
    datos.append(request.form['contrasenia'])
    datos.append(request.form['sexo'])
    datos.append(request.form['fechaNacimiento'])
    datos.append(request.form['altura'])
    datos.append(request.form['peso'])
    datos.append(request.form['cintura'])
    datos.append(request.form['cuello'])
    datos.append(request.form['caderas'])

    x= (i for i in datos if i.strip()=="")
    lista = list(x) 
    if (len(lista)!=0):
        flash('Complete todos los datos')
        return redirect(url_for('Register'))
    else:
        coincidenciasUsuario= db.coincidenciasMail(datos, mysql)
        coincidenciasMail= db.coincidenciasUsuario(datos, mysql)
        if (len(coincidenciasMail)==0 and len(coincidenciasUsuario)==0):
            db.registrarUsuario(datos, mysql)
            flash('Registrado correctamente')
            return redirect(url_for('Index', success=True))
        else:
            if (len(coincidenciasUsuario)!=0):
                flash('El usuario ya esta registrado')
            if (len(coincidenciasMail)!=0):
                flash('El mail ya esta registrado')
            return redirect(url_for('Register'))

def usuarioIniciado():
    if 'username' in session:
        return True
    else:
        return False

def rutinaIniciada():
    if 'idrutina' in session:
        return True
    else:
        return False

def iniciarSesion(mysql, request):
    if request.form['boton']=="Iniciar Sesion":
        usuario= request.form['usuario']
        contrasenia= request.form['contrasenia']
        datosUsuario=db.estaRegistrado(mysql, usuario, contrasenia)
        if (len(datosUsuario)!=0):
            session['username']= datosUsuario[0][0]
        else:    
            flash("Alguno de los datos es incorrecto")
            return redirect(url_for('Index', success=False))
    if request.form['boton']=="Terminar Rutina":
        rutina=request.form['rutina']
        ejercicio=request.form.getlist('ejercicio')
        pesos=request.form.getlist('pesos')
        repeticiones=request.form.getlist('repeticiones')
        descansos=request.form.getlist('descansos')
        idrutina=db.seleccionarIdRutina(mysql, rutina)
        for j in range(0, len(pesos)):
            print("idrutina", idrutina[0][0], "ejercicio", ejercicio[j], "pesos", pesos[j], "repeticiones", repeticiones[j], "descansos", descansos[j])
            db.registrarHistorial(mysql, idrutina[0][0], ejercicio[j], pesos[j], repeticiones[j], descansos[j])    
        flash("Termino la rutina")
        return redirect(url_for('home'))

def mostrarRutinas(mysql, request):
    if 'username' in session and request.method== 'GET':
        datosEjercicioRutina= db.datosEjercicioRutina(mysql, session['username'])
        rutinas= db.rutinasUsuario(mysql, session['username'])
        datosRutinas=functions.rutinaConEjercicios(rutinas, datosEjercicioRutina)
        rutina= request.args.get('rutina')
        if rutina!=None:
            ejercicios=db.seleccionarEjerciciosRutina(mysql, session['username'], rutina)
            rutina=db.seleccionarNombreRutina(mysql, rutina)
            calorias=functions.calcular_calorias(ejercicios)
            return render_template('home.html', datosRutinas=datosRutinas, rutina=rutina, ejercicios=ejercicios, calorias=calorias)
        return render_template('home.html', datosRutinas=datosRutinas, rutina=rutina)
    else:
        return redirect(url_for('Index'))

def datosUsuario(mysql, request):
    return db.seleccionarUsuario(mysql, session['username'])

def agregarRutina(mysql, request):       
    rutina=request.form['nombre-rutina']
    cur= mysql.connection.cursor()
    cur.execute('SELECT r.nombre FROM rutina r JOIN usuario_rutina ur ON r.id_rutina=ur.id_rutina JOIN usuario u ON u.id_usuario=ur.id_usuario WHERE r.nombre="{0}" and u.usuario = "{1}"'.format(rutina, session['username']))
    rutinaRepetida = db.rutinaRepetida(mysql, rutina, session['username'])
    if (len(rutinaRepetida)==0):
        db.registrarRutina(mysql, rutina)
        session['idrutina']= db.ultimaRutina(mysql)
        db.registrarRutinaUsuario(mysql, session['username'], session['idrutina'])
        datosEjer=db.datosEjercicios(mysql)
        return render_template('add_rutina.html', rutina=rutina , ejercicios=datosEjer)
    else:
        flash("Ya tiene una rutina llamada "+ rutina)
        return redirect(url_for('adm_rutinas'))

def rutinaEnCurso(mysql, request):
    nombrerutina=db.seleccionarNombreRutina(mysql, session['idrutina'])
    datosEjer=db.datosEjercicios(mysql)
    return render_template('add_rutina.html', rutina=nombrerutina , ejercicios=datosEjer)

def registrarEjerciciosRutina(mysql, request):
    cantEjerc= len(request.form.getlist('orden'))
    if cantEjerc>0 and request.form.get('botonSubmit')=="botonSubmit":
        nombreEjer= request.form.getlist('nombre-ejer')
        series= request.form.getlist('series')
        repeticiones= request.form.getlist('repeticiones')
        peso= request.form.getlist('peso')
        descansos= request.form.getlist('descansos')
        idrutina= session['idrutina']
        fechaRutina=db.seleccionFechaRutina(mysql, idrutina)
        for i in range(cantEjerc):
            idejercicio=db.seleccionarIdEjercicio(mysql, nombreEjer[i])
            db.registrarRutinaEjercicio(mysql, fechaRutina, idrutina, idejercicio, descansos[i], repeticiones[i], peso[i], series[i])
        session.pop('idrutina')
        flash('Creada correctamente')
    else:
        db.eliminarRutina(mysql, session['username'], session['idrutina'])
        session.pop('idrutina')
        flash('No se agrego ningun ejercicio')
    return redirect(url_for('adm_rutinas'))

def rutinasUsuario(mysql):
    return db.rutinasUsuario(mysql, session['username'])
    

def rutinaEjercicios(mysql):
    return db.datosEjercicioRutina(mysql, session['username'])

def datosEjercicios(mysql):
    return db.datosEjercicios(mysql)

def registrarModificaciones(mysql, request):
    cantEjerc= len(request.form.getlist('orden'))
    if cantEjerc>0 and request.form.get('botonSubmit')=="botonSubmit":
        nombrerutina= request.form['nomb-rut']
        idrutina=request.form['numb-rut']
        nombreEjer= request.form.getlist('nombre-ejer')
        series= request.form.getlist('series')
        repeticiones= request.form.getlist('repeticiones')
        peso= request.form.getlist('peso')
        descansos= request.form.getlist('descansos')
        db.modificarRutina(mysql, idrutina)       
        fechaRutina=db.seleccionFechaRutina(mysql, idrutina)
        for i in range(cantEjerc):
            idejercicio=db.seleccionarIdEjercicio(mysql,nombreEjer[i])
            db.registrarRutinaEjercicio(mysql, fechaRutina, idrutina, idejercicio, descansos[i], repeticiones[i], peso[i], series[i])
        flash('Modificada correctamente')
    return redirect(url_for('adm_rutinas'))

def registrarEliminacion(mysql, request):
    if request.form.get('botonSubmit')=="botonSubmit":
        cantEjerc= len(request.form.getlist('orden'))
        idrutina= request.form['numb-rut']
        db.eliminarRutina(mysql, session['username'], idrutina)
        flash('eliminada correctamente')
    else:
        flash('No se hicieron cambios')
    return redirect(url_for('adm_rutinas'))

def registrarEjercicio(mysql, request):
    nombre=request.form['nombre-ejercicio']
    descrip=request.form['descripcion']
    db.registrarEjercicio(mysql, nombre, descrip)
    flash('Se registro el ejercicio')

def mostrar_historial_rutina(mysql, request):
    datosEjercicioRutina= db.datosEjercicioRutina(mysql, session['username'])
    rutinas= db.rutinasUsuario(mysql, session['username'])
    datosRutinas=functions.rutinaConEjercicios(rutinas, datosEjercicioRutina)
    rutina= request.args.get('rutina')
    if rutina!=None:
        ejercicios=db.historialEjerciciosRutina(mysql, session['username'], rutina)
        rutina=db.seleccionarNombreRutina(mysql, rutina)
        print(ejercicios)
        return render_template('historial_rutina.html', datosRutinas=datosRutinas, rutina=rutina, ejercicios=ejercicios)
    return render_template('historial_rutina.html', datosRutinas=datosRutinas, rutina=rutina)

def mostrar_historial_usuario(mysql, request):
    historial=db.historial_usuario(mysql, session['username'])
    usuario=db.seleccionarUsuario(mysql, session['username'])
    return render_template('historial_usuario.html', historial=historial, nombre=usuario[1], apellido=usuario[2])

def actualizar_perfil(mysql, request):
    altura= float(request.form['altura'])
    peso= float(request.form['peso'])
    cintura= float(request.form['cintura'])
    cuello= float(request.form['cuello'])
    caderas=float(request.form['caderas'])

    usuario= db.datos_usuario(mysql, session['username'])
    sexo=usuario[0][0]
    print("altura", altura)
    db.actualizar_perfil(mysql, session['username'], altura, peso, cintura, cuello, caderas)
    db.registrar_historial(mysql, session['username'], functions.IMC(peso, altura), functions.metabolismo_basal(peso, altura, functions.calcular_edad(db.fecha(mysql, session['username'])), db.sexo(mysql, session['username'])), functions.porcentajeGrasa(sexo, cintura, cuello, altura, caderas))
    flash("Se registraron correctamente los cambios")
    return redirect(url_for('perfil', success=True))

def formulario_perfil(mysql):
    datosUsuario=db.datos_usuario(mysql, session['username'])
    return datosUsuario[0]

def calcular_metabolismo_basal(mysql, altura, peso):
    return functions.metabolismo_basal(peso, altura, functions.calcular_edad(db.fecha(mysql, session['username'])), db.sexo(mysql, session['username']))