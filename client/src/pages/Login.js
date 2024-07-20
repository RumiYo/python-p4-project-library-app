import { useEffect, useState } from "react";
import { Link, useOutletContext  } from  "react-router-dom";
import LoginForm from "../components/LoginForm";
import SignUpForm from "../components/SignUpForm";

function Login({ onLogin }){
    const [ showLogin, setShowLogin ] =useState(true);

        return (
            <main>
                <h1>Rumi Online Library</h1>
                {showLogin ? (
                    <>
                    <LoginForm onLogin={ onLogin } />
                    <p>Don't have an account?</p>
                    <button onClick={() => setShowLogin(false)}>
                          Go to Signup page
                    </button>
                    </>
                ) : (
                    <>
                        <SignUpForm onSignUp={ onLogin } />
                        <p>Already have an account? </p>
                        <button onClick={() => setShowLogin(true)}>
                            Go to Login page
                        </button>
                    </>
                )}
                <p>Librrary info</p>
            </main>
        )
}

export default Login;