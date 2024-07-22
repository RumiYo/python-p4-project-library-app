import React, { useState } from "react";

function SignUpForm({ onSignUp }){
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [userId, setUserId] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    function handleSubmit(e){
        e.preventDefault();
        console.log(lastName, firstName,userId, email, password)
        setIsLoading(true);
        fetch("/signup", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              first_name: firstName,
              last_name: lastName,
              user_id: userId,
              email: email,
              password: password,
            }),
          })
        .then((r) => {
            setIsLoading(false);
            if (r.ok) {
              r.json().then((member) => onSignUp(member));
            } else {
              r.json().then((err) => setError(err.error));
            }
        });
    }
      
    

    return (
        <>
            <h2>Signup Form</h2>
            <form className="LoginSignupForms" onSubmit={handleSubmit}>
              <p>Please fill out all the information below:</p>
                <label htmlFor="firstName">First Name:  </label>
                <input
                type="text"
                id="firstName"
                autoComplete="off"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                />
                <br/>
                <label htmlFor="lastName">  Last Name:  </label>
                <input
                type="text"
                id="lastName"
                autoComplete="off"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                />
                <br/>
                <label htmlFor="userId">UserID:  </label>
                <input
                type="text"
                id="userId"
                autoComplete="off"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
                />
                <br/>
                <label htmlFor="email">Email Address:  </label>
                <input
                type="text"
                id="email"
                autoComplete="off"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                />
                <br/>
                <label htmlFor="password">Password:  </label>
                <input
                type="text"
                id="password"
                autoComplete="off"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
                <br/>
                <input type="submit" className="buttons"/>

                <p>{error}</p>
            </form>            
        </>
    )
}

export default SignUpForm;