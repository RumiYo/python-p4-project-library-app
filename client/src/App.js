import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import "./App.css";
import Login from "./pages/Login";


function App() {
  const [ member, setMember ] = useState(null);

  useEffect(() => {
    fetch("/check_session")
    .then((r)=> {
      if(r.ok){
        r.json().then((member) => setMember(member))
      }
    })
  }, []);

  const handleLogin = (member) => {
    setMember(member); 
  };

  const handleLogOut = () => {
    setMember(null); 
  };

  if (!member)
    return <Login onLogin={handleLogin}  />
  
  return (
    <>
      <header>
        <NavBar  member={member} onLogout={handleLogOut}  />
      </header>
         <Outlet context={{member: member, updateMember:handleLogin }} />
    </>
);
}

export default App;
