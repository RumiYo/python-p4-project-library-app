import React from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

function NavBar({ member, onLogout }){

    function handleLogoutClick() {
        fetch("/logout", { method: "DELETE" }).then((r) => {
          if (r.ok) {
            onLogout(null);
          }
        });
      }

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
            <NavLink
                className="nav-link"
                onClick={handleLogoutClick}
            >Logout</NavLink>
        </nav>
    )
}

export default NavBar
