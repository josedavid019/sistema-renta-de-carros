// src/components/Navbar.jsx
import React from "react";
<<<<<<< HEAD
import "./Navbar.css";
=======
import "./Navbar.css"; // hoja de estilos opcional
>>>>>>> 7c0dcc5638db46690d0da55f728a0bf1629f751e

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
<<<<<<< HEAD
        {/* Al envolver el logo en <a> con href="/" se redirige al home */}
        <a href="/">
          <img
            src="/Logo empresa.png" 
=======
        {/* Logo envuelto en <a> para redirigir al home */}
        <a href="/">
          <img
            src="/Logo empresa.png"
>>>>>>> 7c0dcc5638db46690d0da55f728a0bf1629f751e
            alt="Logo de la empresa"
            className="navbar-logo"
          />
        </a>
      </div>
      <div className="navbar-right">
        <a href="#catalogo">Catálogo Carros</a>
        <a href="#reservas">Mis Reservas</a>
        <a href="#login" className="navbar-login">
          <i className="fa fa-user" /> Iniciar Sesión
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
