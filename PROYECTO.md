# Sistema de gimnasio


## Descripción del proyecto

Una aplicación donde existan dos tipos de usuarios (cliente, entrenador) en la cual el cliente podrá armar su propia rutina o recibir rutinas de parte del entrador. Para el armado de rutinas se permitirá una múltiple selección de ejercicios con distintas modalidades y aclarar los tiempos de descanso. El cliente tendrá la posibilidad de cargar sus pesos para cada serie, junto con las repeticiones.

Posibilidades a la hora de armar la rutina:

- Una combinación de ejercicios con las series y repeticiones establecidas.

Ej: Biserie -> 4 series de Press de banca 8 repeticiones + Curl de biseps 12 repeticiones. Igual a las biseries podrían asignarse triseries o circuitos.

Con esto se permitiría al cliente tener un registro de sus progresos, facilitar las anotaciones en el gimnasio (actualmente la mayoría usa una hoja, o no anota).

## Modelo de Dominio

![alt text](https://github.com/Juandiegordp/TPI/blob/main/MapaCanonico.jpg)

## Bosquejo de Arquitectura

Definir la arquitectura del sistema y como interactuan sus diferentes componentes. Utilizar el Paquete **Office** de Draw.io o similar. [Ejemplo Online]().

## Requerimientos


### Funcionales

- Gestionar rutinas de entrenamiento.
- Gestionar clientes.
- Generar estadísticas de progreso del entrenamiento de los clientes.
- Gestionar personal del gimnasio.


### No Funcionales

Listado y descripción breve de los requerimientos no funcionales. Utilizar las categorias dadas:

### Portability

**Obligatorios**

- El sistema debe funcionar correctamente en múltiples navegadores (Sólo Web).
- El sistema debe ejecutarse desde un único archivo .py llamado app.py (Sólo Escritorio).

### Security

**Obligatorios**

- Todas las contraseñas deben guardarse con encriptado criptográfico (SHA o equivalente).
- Todas los Tokens / API Keys o similares no deben exponerse de manera pública.

### Maintainability

**Obligatorios**

- El sistema debe diseñarse con la arquitectura en 3 capas. (Ver [checklist_capas.md](checklist_capas.md))
- El sistema debe utilizar control de versiones mediante GIT.
- El sistema debe estar programado en Python 3.8 o superior.

### Reliability

### Scalability

**Obligatorios**

- El sistema debe funcionar desde una ventana normal y una de incógnito de manera independiente (Sólo Web).
  - Aclaración: No se debe guardar el usuario en una variable local, deben usarse Tokens, Cookies o similares.

### Performance

**Obligatorios**

- El sistema debe funcionar en un equipo hogareño estándar.

### Reusability

### Flexibility

**Obligatorios**

- El sistema debe utilizar una base de datos SQL o NoSQL

## Stack Tecnológico

Definir que tecnologías se van a utilizar en cada capa y una breve descripción sobre por qué se escogió esa tecnologia.

### Capa de Datos

Definir que base de datos, ORM y tecnologías se utilizaron y por qué.

### Capa de Negocio

Definir que librerías e integraciones con terceros se utilizaron y por qué. En caso de consumir APIs, definir cúales se usaron.

### Capa de Presentación

Definir que framework se utilizó y por qué.
