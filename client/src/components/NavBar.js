import React from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

function NavBar(){
    return (
        <nav>
            <NavLink
                to="/"
                className="nav-link"
            >Home
            </NavLink>
            <NavLink 
                to="/books"
                className="nav-link"
            >All books
            </NavLink>
            <NavLink
                to="/account"
                className="nav-link"
            >Account Summary</NavLink>
        </nav>
    )
}

export default NavBar
