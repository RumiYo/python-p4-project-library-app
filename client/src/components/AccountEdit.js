import { Link, useOutletContext } from "react-router-dom";
import { useState } from "react";
import { useFormik } from 'formik';
import * as yup from 'yup';

function AccountEdit() {

    const { member, updateMember } = useOutletContext(); 

    const [keyValue, setKeyValue] = useState("user_id");
    const [message, setMessage] = useState("");  

    const getValidationSchema = (key) => {
        switch (key) {
            case 'first_name':
                return yup.object().shape({
                    first_name: yup.string().required("Must enter First Name").max(15),
                });
            case 'last_name':
                return yup.object().shape({
                    last_name: yup.string().required("Must enter Last Name").max(15),
                });
            case 'user_id':
                return yup.object().shape({
                    user_id: yup.string().required("Must enter a UserID").max(10),
                });
            case 'email':
                return yup.object().shape({
                    email: yup.string().email("Invalid email").required("Must enter email"),
                });
            default:
                return yup.object().shape({});

            }
    }

    const formik = useFormik({
        initialValues: {
            first_name: "",
            last_name: "",
            user_id: "",
            email: "",
        },
        validationSchema: getValidationSchema(keyValue),
        onSubmit: (values) => {
            console.log("Formik onSubmit values:", values);
            console.log("Form submitted");
            console.log("Key Value: ", keyValue);
            console.log("Sending PATCH request to:", `/members/${member.id}`);
            
            if (!member.id) {
                setMessage("Member ID is not available.");
                return;
            }
    
            const formData = {
                [keyValue]: values[keyValue]
            };
    
            fetch(`/members/${member.id}`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            })
            .then((r) => {
                if (r.ok) {
                    return r.json();
                } else {
                    return r.json().then((err) => {
                        throw new Error(err.error);
                    });
                }
            })
            .then((updatedMember) => {
                updateMember(updatedMember);
                setMessage("Successfully Updated");
            })
            .catch((error) => {
                console.error('Error during fetch:', error);
                setMessage(error.message);
            });
        }
    });
    
    return (
        <div id="memberEdit">
            <h3>Account information update</h3>
            <div className="dropdown">
                <label htmlFor="infochange">I want to change:</label>
                <select id="infochange" name="infochange" onChange={(e) => setKeyValue(e.target.value)}>
                    <option value="user_id">UserID</option>
                    <option value="first_name">First Name</option>
                    <option value="last_name">Last Name</option>
                    <option value="email">Email Address</option>
                </select>
                <form onSubmit={(e) => {
                        e.preventDefault();
                        formik.submitForm();
                    }}> 
                    <input
                        type="text"
                        id={keyValue}
                        name={keyValue}
                        autoComplete="off"
                        value={formik.values[keyValue]}
                        onChange={formik.handleChange}
                    />
                    <input type="submit" className="buttons" />
                </form>
                <p>{message}</p>
            </div>
            <br />
            <Link to={`/account`}>Close</Link>
        </div>
    )

}

export default AccountEdit;