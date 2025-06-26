import React from "react";
import { Link, NavLink } from "react-router-dom";
import "../components/NavBar.css";

const NavBar = () => {
  return (
    <nav>
      <NavLink
        to="/"
        //  className={({isActive}) => (isActive) ? "" : ""}
      >
        Home
      </NavLink>
      <NavLink to="/abou">Sobre</NavLink>
    </nav>
  );
};

export default NavBar;
