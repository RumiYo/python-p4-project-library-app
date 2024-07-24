import React, { useState } from "react";
import { useFormik } from 'formik';
import * as yup from "yup";

function LoginForm({ onLogin }){

    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const formSchema = yup.object().shape({
        user_id: yup.string().required("Must enter a UserID").max(10),
        password: yup.string().required("Must enter password").max(15),
      });

    
    const formik = useFormik({
    initialValues: {
        user_id: "",
        password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
        setIsLoading(true);
        fetch("/login", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(values),
        })
        .then((r) => {
        setIsLoading(false);
        if (r.ok) {
            r.json().then((member)=> onLogin(member));
        } else {
            r.json().then((err) => setError(err.error));
        }
        })
    }
    })

        
    return (
        <div >
            <h2>Login</h2>
            <form className="LoginSignupForms" onSubmit={formik.handleSubmit}>
                <p>Type your UserID and Password:</p>
                <label htmlFor="user_id">UserID: </label>
                <input
                    type="text"
                    id="user_id"
                    autoComplete="off"
                    value={formik.values.user_id}
                    onChange={formik.handleChange}
                />

                <label htmlFor="password">   Password: </label>
                <input
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    value={formik.values.password}
                    onChange={formik.handleChange}
                />
                <br/>
                <input type="submit" className="buttons"/>
                {isLoading && <p>Loading...</p>}
                {error && <p>{error}</p>}
            </form>
        </div>
    )
}

export default LoginForm;