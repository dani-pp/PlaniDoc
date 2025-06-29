function mostrarPaso(numero) {
  // Oculta todos los pasos
  document.querySelectorAll('.paso').forEach(paso => {
    paso.classList.add('hidden');
    paso.classList.remove('opacity-100');
    paso.classList.add('opacity-0');
  });

  // Muestra el paso actual
  const pasoActual = document.getElementById(`paso-${numero}`);
  if (pasoActual) {
    pasoActual.classList.remove('hidden');
    pasoActual.classList.remove('opacity-0');
    pasoActual.classList.add('opacity-100');
  }
}


const correo = document.getElementById('correo');
const contraseña = document.getElementById('contraseña');
const nombres = document.getElementById('nombres');
const apellidos = document.getElementById('apellidos');
const paso_1 = document.getElementById('botonPaso1');
const paso_2 = document.getElementById('botonPaso2');
const form = document.getElementById('formRegistro');

paso_1.classList.remove('bg-blue-600','hover:bg-blue-400','cursor-pointer');
paso_1.classList.add('bg-blue-200');
paso_2.classList.remove('bg-blue-600','hover:bg-blue-400','cursor-pointer');
paso_2.classList.add('bg-blue-200');


  form.addEventListener('input', () => {
    if (correo.validity.valid && contraseña.validity.valid) {
      paso_1.classList.add('bg-blue-600','hover:bg-blue-400','cursor-pointer');
      paso_1.disabled = false;
    }
    else{
      paso_1.disabled = true;
      paso_1.classList.remove('bg-blue-600','hover:bg-blue-400','cursor-pointer');
      paso_1.classList.add('bg-blue-200');
    }
  });

  form.addEventListener('input', () => {
    if (nombres.validity.valid && apellidos.validity.valid) {
      paso_2.classList.add('bg-blue-600','hover:bg-blue-400','cursor-pointer');
      paso_2.disabled = false;
    }
    else{
      paso_2.disabled = true;
      paso_2.classList.remove('bg-blue-600','hover:bg-blue-400','cursor-pointer');
      paso_2.classList.add('bg-blue-200');
    }
  });

