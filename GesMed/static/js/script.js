  const botones = document.querySelectorAll(".btn");
  const tablas = {
    medicos: document.getElementById("tabla-medicos"),
    pacientes: document.getElementById("tabla-pacientes"),
    citas: document.getElementById("tabla-citas"),
  };

  botones.forEach(boton => {
    boton.addEventListener("click", () => {
      // Quitar clase 'selected' de todos
      botones.forEach(btn => btn.classList.remove("selected"));
      // Agregar clase 'selected' al botón clickeado
      boton.classList.add("selected");

      // Ocultar todas las tablas
      Object.values(tablas).forEach(tabla => tabla.style.display = "none");

      // Mostrar la tabla correspondiente
      const target = boton.getAttribute("data-target");
      tablas[target].style.display = "block";
    });
  });


 const avatar = document.getElementById("profile-avatar");
  const dropdown = document.getElementById("dropdown-menu");
  const toggleDark = document.getElementById("dark-toggle");

  avatar.addEventListener("click", () => {
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
  });

  toggleDark.addEventListener("change", () => {
    //document.body.style.backgroundImage = toggleDark.checked ? "url('resours/img/black.png')" : "url('resours/img/black.png')";
    document.body.style.backgroundColor = toggleDark.checked ? "#1e1e1e" : "#f0f0f0";
    document.body.style.color = toggleDark.checked ? "#000000" : "#000000";

      // Tarjetas y secciones
  document.querySelectorAll(".card, .table-section").forEach(el => {
    el.style.backgroundColor = toggleDark.checked ? "#2e2e2e" : "#ffffff";
    el.style.color = toggleDark.checked ? "#ffffff" : "#000000";
    el.style.border = toggleDark.checked ? "3px solid #887a7e" : "3px solid #E0E0E0";
  });

document.querySelectorAll(".card, .table-section, .cardnormal").forEach(el => {
  el.style.backgroundColor = toggleDark.checked ? "#2e2e2e" : "#ffffff";
  el.style.color = toggleDark.checked ? "#ffffff" : "#000000";
});

document.querySelectorAll(".cardbold").forEach(el => {
  el.style.color = toggleDark.checked ? "#ffffff" : "#887a7e";
});

const dropdownMenu = document.getElementById("dropdown-menu");

if (toggleDark.checked) {
  dropdownMenu.style.background = "#2e2e2e";
  dropdownMenu.style.color = "#ffffff";
} else {
  dropdownMenu.style.background = "white";
  dropdownMenu.style.color = "#157efb";
}

/*    
const logo = document.querySelector(".logo");

if (toggleDark.checked) {
  logo.src = "{{ url_for('static', filename='resours/img/GEStionMEDicaW.webp') }}";
} else {
  logo.src = "{{ url_for('static', filename='resours/img/GEStionMEDica.webp') }}";
} */

/*
document.querySelectorAll(".welcome .name").forEach(el => {
  if (toggleDark.checked) {
    el.style.color = "#FFA95E";
    el.style.opacity = "0.95";
    el.style.textShadow = "0 0 5px #FFA95E, 0 0 10px #FFA95E, 0 0 20px #FFA95E, 0 0 40px #FFA95E";
    el.style.fontWeight = "bold";    
  } else {    
    el.style.color = "#FFA95E";
    el.style.opacity = "none";
    el.style.textShadow = "none";
    el.style.fontWeight = "none";
  }
});
*/
const botones = document.querySelectorAll(".btn");

if (toggleDark.checked) {
  // Modo oscuro: nuevos gradientes
  botones[0].style.background = "linear-gradient(to bottom right, #4199FD, #1e1e1e)";
  botones[1].style.background = "linear-gradient(to bottom right, #1EC0F5, #1e1e1e)";
  botones[2].style.background = "linear-gradient(to bottom right, #d98bf8, #1e1e1e)";
} else {
  // Modo claro: gradientes originales
  botones[0].style.background = "linear-gradient(to bottom right, #4199FD, #094FEF)";
  botones[1].style.background = "linear-gradient(to bottom right, #1EC0F5, #4199FD)";
  botones[2].style.background = "linear-gradient(to bottom right, #4199FD, #DA5FF9)";
}



  });

  function cerrarSesion() {
    alert("Sesión cerrada");
    // Aquí puedes redirigir a login o limpiar sesión
  }

  // Cierra el menú si haces clic fuera
  document.addEventListener("click", function (e) {
    if (!avatar.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.style.display = "none";
    }
  });




  // Mostrar modal
document.getElementById("abrir-modal-medico").addEventListener("click", function () {
  document.getElementById("modal-medico").style.display = "flex";
});

// Cerrar modal
function closeModal() {
  document.getElementById("modal-medico").style.display = "none";
}

function closeModalOutside(event) {
  if (event.target.classList.contains("modal")) {
    closeModal();
  }
}

function limpiarCampos() {
  const modal = document.getElementById("modal-medico");
  const inputs = modal.querySelectorAll("input[type='text'], input[type='email'], input[type='password']");
  inputs.forEach(input => input.value = "");
  document.getElementById("preview-img").style.display = "none";
  document.getElementById("preview-text").style.display = "block";
}


// MODAL PACIENTE
const btnAgregarPaciente = document.querySelector('#tabla-pacientes .add-btn');
const modalPaciente = document.getElementById('modalRegistro');
const cerrarPacienteBtn = modalPaciente.querySelector('.close-btn');
const formularioPaciente = modalPaciente.querySelector('.form-gridPaciente');
const botonesPaciente = modalPaciente.querySelector('.buttons');

// Abrir el modal al hacer clic en "Agregar Paciente"
btnAgregarPaciente.addEventListener('click', () => {
  modalPaciente.classList.add('modalpaciente-active');
});

// Cerrar el modal al hacer clic en la X
cerrarPacienteBtn.addEventListener('click', () => {
  modalPaciente.classList.remove('modalpaciente-active');
});

// Cerrar si se hace clic fuera del contenido
modalPaciente.addEventListener('click', (e) => {
  if (e.target === modalPaciente) {
    modalPaciente.classList.remove('modalpaciente-active');
  }
});

// Limpiar el formulario al hacer clic en el botón "Limpiar"
botonesPaciente.querySelector('.btn-limpiar').addEventListener('click', () => {
  formularioPaciente.reset();
});


 // PACIENTE
  function abrirModalEliminarPaciente(id, nombre) {
    document.getElementById("idPacienteEliminar").value = id;
    document.getElementById("textoEliminarPaciente").innerText = `¿Eliminar al paciente ${nombre}?`;
    document.getElementById("formEliminarPaciente").action = `/eliminar_paciente/${id}`;
    document.getElementById("modalEliminarPaciente").style.display = "block";
  }

  function cerrarModalEliminarPaciente() {
    document.getElementById("modalEliminarPaciente").style.display = "none";
  }

  // CITA
  function abrirModalEliminarCita(id, nombrePaciente) {
    document.getElementById("idCitaEliminar").value = id;
    document.getElementById("textoEliminarCita").innerText = `¿Eliminar la cita del paciente ${nombrePaciente}?`;
    document.getElementById("formEliminarCita").action = `/eliminar_cita/${id}`;
    document.getElementById("modalEliminarCita").style.display = "block";
  }

  function cerrarModalEliminarCita() {
    document.getElementById("modalEliminarCita").style.display = "none";
  }

  // Opcional: placeholders
  function verPaciente(id) { alert("Ver paciente: " + id); }
  function actualizarPaciente(id) { alert("Actualizar paciente: " + id); }

  function verCita(id) { alert("Ver cita: " + id); }
  function actualizarCita(id) { alert("Actualizar cita: " + id); }


  const btnAbrir = document.getElementById('btnAgregarCita');
const modal = document.getElementById('modalrecetas');
const btnCerrar = document.getElementById('cerrarModal');

btnAbrir.addEventListener('click', () => {
  modal.classList.add('modal-active');  
});

btnCerrar.addEventListener('click', () => {
  modal.classList.remove('modal-active'); 
});

window.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.classList.remove('modal-active'); 
  }
});

function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) {
    modal.classList.add('modal-active');
    modal.style.display = 'flex';
  }
}

function Cerrar(id) {
  const modal = document.getElementById(id);
  if (modal) {
    modal.classList.remove('modal-active');
    modal.style.display = 'none';
  }
}

function CerrarOutside(event) {
  if (event.target.classList.contains('modal')) {
    event.target.classList.remove('modal-active');
    event.target.style.display = 'none';
  }
}


function verPaciente(id) {
  document.getElementById(id).style.display = 'flex';
}

function Cerrar(id) {
  document.getElementById(id).style.display = 'none';
}

function CerrarModalOutside(event) {
  if (event.target.classList.contains('modalpaciente')) {
    event.target.style.display = 'none';
  }
}


 function abrirModalEliminar(id, nombre) {
    document.getElementById("idMedicoEliminar").value = id;
    document.getElementById("textoConfirmacion").innerText = `¿Estás seguro de eliminar al Dr. ${nombre}?`;
    document.getElementById("modalEliminar").style.display = "block";
    document.getElementById("formEliminar").action = `/eliminar_medico/${id}`;
  }

  function cerrarModalEliminar() {
    document.getElementById("modalEliminar").style.display = "none";
  }