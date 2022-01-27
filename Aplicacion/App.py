###from MySQLdb import cursors
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session
import flask
from flask.globals import request
from flask.wrappers import Request
from flask_mysqldb import MySQL
import forms, functions
from Presentacion import views
app = Flask(__name__)

#Mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3300
app.config['MYSQL_DB'] = 'aplicaciongym'
mysql=MySQL(app)

# settings session

app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET'])
def Index():
    return views.Index(mysql, request)

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('Index'))

@app.route('/register', methods = ['POST', 'GET'])
def Register():
    return views.register(mysql, request)

@app.route('/home', methods=['POST', 'GET'])
def home():
    return views.home(mysql, request)

@app.route('/home/user', methods=['GET']) 
def perfil():
    return views.perfil(mysql, request)

@app.route('/home/user/actualize', methods=['POST', 'GET']) 
def actualizar_perfil():
    return views.ActualizarPerfil(mysql, request)

@app.route('/home/administracion_rutinas')
def adm_rutinas():
    return views.administracionRutinas(mysql, request)

@app.route('/home/administracion_rutinas/add_rutina', methods= ['POST'])
def add_rutina():
    return views.crearRutina(mysql, request)

@app.route('/home/administracion_rutinas/add_rutina/create_rutina', methods= ['POST'])
def create_rutina():
    return views.registrarEjerciciosRutina(mysql, request)

@app.route('/home/administracion_rutinas/modify_rutina')
def modify_rutina():
    return views.modificarRutina(mysql, request)
        
@app.route('/home/administracion_rutinas/modify_rutina/add_modification', methods= ['POST'])
def add_modification():
    return views.registrarModiciaciones(mysql, request)

@app.route('/home/administracion_rutinas/delete_rutina')
def delete_rutina():
    return views.eliminarRutina(mysql,request)

@app.route('/home/administracion_rutinas/delete_rutina/confirm_delete', methods= ['POST'])
def confirm_delete():
    return views.registrarEliminacion(mysql, request)

@app.route('/ejercicios')
def ejercicios():
    return render_template('CargarEjercicios.html')

@app.route('/home/historial_rutina', methods= ['GET', 'POST'])
def historial_rutina():
    return views.historial_rutina(mysql, request)

@app.route('/home/historial_usuario', methods= ['GET', 'POST'])
def historial_usuario():
    return views.historial_usuario(mysql, request)

if __name__== '__main__':
    app.run(port = 3000, debug=True)