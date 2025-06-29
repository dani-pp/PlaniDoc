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