from Negocio import controller
import forms, functions
from flask import Flask, render_template, request, redirect, url_for, flash
   
def register(mysql, request):
   registerForm= forms.RegisterForm(request.form)
   if request.method == 'POST' and registerForm.validate():
      return controller.registraUsuario(mysql, request, registerForm)
   return render_template('register.html', form=registerForm)

def Index(mysql, request):
   if request.method=='GET':
      success= request.args.get('success')
      if success==None:
         if controller.usuarioIniciado():
               return redirect(url_for('home'))
         else:
            return render_template('Index.html')
      else:          
         return render_template('Index.html', success=success)
   return render_template('Index.html')
          

def home(mysql, request):
    if request.method== 'POST':
       controller.iniciarSesion(mysql, request)
    if controller.usuarioIniciado() and request.method== 'GET':
       return controller.mostrarRutinas(mysql, request)
    else:
        return redirect(url_for('Index'))

def historial_rutina(mysql, request):
    if controller.usuarioIniciado() and request.method== 'GET':
       return controller.mostrar_historial_rutina(mysql, request)
    else:
        return redirect(url_for('Index'))

def historial_usuario(mysql, request):
    if controller.usuarioIniciado() and request.method== 'GET':
       return controller.mostrar_historial_usuario(mysql, request)
    else:
        return redirect(url_for('Index'))

def perfil(mysql, request):
    if controller.usuarioIniciado and request.method=='GET':
        success= request.args.get('success')
        usuario=controller.datosUsuario(mysql, request)
        imc=functions.IMC(usuario[8], usuario[7])
        m_basal= controller.calcular_metabolismo_basal(mysql, usuario[7], usuario[8])
        return render_template('perfil.html', success=success, usuario=usuario, imc=imc, evaluacion=functions.evaluarIMC(imc), pg=functions.porcentajeGrasa(usuario[5], usuario[9], usuario[10], usuario[7], usuario[11]), m_basal=m_basal )
    else:
        return redirect(url_for('Index'))

def ActualizarPerfil(mysql, request):
   actualize_form= forms.PerfilForm(request.form)
   if request.method == 'POST' and controller.usuarioIniciado:
      if actualize_form.validate():
         return controller.actualizar_perfil(mysql, request)
      else:
         flash("Alguno de los datos es incorrecto")
         return redirect(url_for('actualizar_perfil', success=False))
   else:
      if request.method == 'GET' and controller.usuarioIniciado:
         datos=controller.formulario_perfil(mysql)
         return render_template('actualizar_perfil.html', form=actualize_form, datos=datos)
      return redirect(url_for('perfil'))

def administracionRutinas(mysql, request):
    if controller.usuarioIniciado():
        return render_template('administracion_rutinas.html')
    else:
        return redirect(url_for('Index'))

def crearRutina(mysql, request):
   if request.method =='POST' and controller.usuarioIniciado():
        return controller.agregarRutina(mysql, request)
   else:
      if controller.rutinaIniciada() and controller.usuarioIniciado():
         return controller.rutinaEnCurso(mysql, request)
      if controller.usuarioIniciado():
         return redirect(url_for('adm_rutinas'))
      else:
         return redirect(url_for('Index'))

def registrarEjerciciosRutina(mysql, request):
   if request.method == 'POST':
      return controller.registrarEjerciciosRutina(mysql, request)
   return redirect(url_for('adm_rutinas'))

def modificarRutina(mysql, request):
    if controller.usuarioIniciado():
      rutinas=controller.rutinasUsuario(mysql)
      rutinaEjercicios=controller.rutinaEjercicios(mysql)
      datosEjer=controller.datosEjercicios(mysql)
      return render_template('modify_rutina.html', rutinas=rutinas , ejercicios=datosEjer, rutinaEjer=rutinaEjercicios)
    else:
        return redirect(url_for('Index'))

def registrarModiciaciones(mysql, request):
   if request.method == 'POST':
      return controller.registrarModificaciones(mysql, request)
   return redirect(url_for('adm_rutinas'))

def eliminarRutina(mysql,request):
   if controller.usuarioIniciado():
      rutinas=controller.rutinasUsuario(mysql)
      rutinaEjercicios=controller.rutinaEjercicios(mysql)
      return render_template('delete_rutina.html', rutinas=rutinas , rutinaEjer=rutinaEjercicios)
   else:
      return redirect(url_for('Index'))

def registrarEliminacion(mysql, request):
    if request.method=='POST' and controller.usuarioIniciado():
        return controller.registrarEliminacion(mysql, request)
    else:
        return redirect(url_for('Index'))

def registrarEjercicios(mysql, request):
   if request.method == 'POST':
      return controller.registrarEjercicio(mysql, request)
   return redirect(url_for('ejercicios'))