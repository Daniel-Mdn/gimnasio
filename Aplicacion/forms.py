from wtforms import Form, validators, PasswordField, BooleanField, FloatField, IntegerField, RadioField, DateField
from wtforms import StringField


class RegisterForm(Form):
    usuario= StringField('Usuario', [validators.Length(min=4, max=25, message="El usuario que tener entre 4 a 25 caracteres")])
    nombre= StringField('Nombre', [validators.Length(min=3, max=12, message="El nombre que tener entre 3 a 12 caracteres")])
    apellido= StringField('Apellido', [validators.Length(min=4, max=12, message="El apellido que tener entre 3 a 12 caracteres")])
    sexo= RadioField('Sexo', choices =['Masculino', 'Femenino'])
    fechaNacimiento= DateField('Fecha de nacimiento',format='%Y-%m-%d')
    altura= FloatField('Altura en cm (opcional)', [validators.required()])
    peso= FloatField('Peso en kg (opcional)', [validators.required()])
    cintura= FloatField('Cintura en cm', [validators.required()])
    cuello= FloatField('Cuello en cm', [validators.required()])
    caderas= FloatField('Caderas en cm')
    contrasenia= PasswordField('Contraseña', [validators.DataRequired(), validators.EqualTo('confirmarContra', message='No coinciden las contraseñas')])
    confirmarContra= PasswordField('Repetir Contraseña')
    terminos = BooleanField('Acepto los terminos y condiciones', [validators.DataRequired(message="Acepte los terminos y condiciones")])

class PerfilForm(Form):
    altura= FloatField('Altura en cm (opcional)', [validators.required()])
    peso= FloatField('Peso en kg (opcional)', [validators.required()])
    cintura= FloatField('Cintura en cm (opcional)', [validators.required()])
    cuello= FloatField('Cuello en cm (opcional)', [validators.required()])
    caderas= FloatField('Caderas en cm (opcional)')
    