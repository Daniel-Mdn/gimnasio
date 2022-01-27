function cargarRutinaHome(rut){
    var datosRutinas= {{datosRutinas|tojson}};
    datosRutinas.forEach(element => {
      if (rut == element[0]){
        document.getElementById('id-titulo').innerHTML= '<h2>Rutina '+ element[1] +'</h2>';
      }
      for(let i=2; i < element.length; i++){
        console.log(element[i])
        document.getElementById('id-ejercicio').innerHTML='<label>'+ element[i][1] +'</label>';
        document.getElementById('id-info').innerHTML='<label>Peso: '+ element[i][2] +'- Repeticiones: '+ element[i][3] +'- Series: '+ element[i][4] +'- Descansos: '+ element[i][5] +'</label>';
      }
    });

  }