import { useEffect, useState } from "react";
import { Link } from  "react-router-dom";
import LoginForm from "../components/LoginForm";
import SignUpForm from "../components/SignUpForm";

function Home(){


    return (
        <main>
            <h2>Home</h2>
            <p>Login Page Here</p>
            <LoginForm />
            <SignUpForm />
        </main>
        
    )

}

export default Home;