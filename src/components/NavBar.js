import React from "react";
import { Link } from "react-router-dom";
import "../components/NavBar.css";

const NavBar = () => {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/">Home</Link>
      <Link to="/">Home</Link>
    </nav>
  );
};

export default NavBar;
