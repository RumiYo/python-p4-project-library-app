import React, { useState } from "react";

function LoginForm({ onLogin }){
    const [ user_id, setUser_id ] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    function handleSubmit(e){
        e.preventDefault();
        setIsLoading(true);
        console.log(user_id, password)
        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ user_id, password}),
        })
        .then((r)=>{
            setIsLoading(false);
            if(r.ok) {
                r.json()
                .then((member)=> onLogin(member))
            } else {
                r.json()
                .then((err) => setError(err.error))
            }
        })
    }
    
    console.log(error)
        
    return (
        <div >
            <h2>Login</h2>

            <form className="LoginSignupForms" onSubmit={handleSubmit}>
                <p>Type your UserID and Password:</p>
                <label htmlFor="user_id">UserID: </label>
                <input
                    type="text"
                    id="user_id"
                    autoComplete="off"
                    value={user_id}
                    onChange={(e) => setUser_id(e.target.value)}
                />

                <label htmlFor="password">   Password: </label>
                <input
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br/>
                <input type="submit" className="buttons"/>
                {isLoading ? "Loading..." : ""}          

                <p>{error}</p>

            </form>
        </div>
    )
}

export default LoginForm;