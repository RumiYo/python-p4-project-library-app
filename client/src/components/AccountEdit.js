import { Link, useOutletContext } from "react-router-dom";
import { useState } from "react";
import { useFormik } from 'formik';
import * as yup from "yup";

function AccountEdit() {
    
    const { member, updateMember } = useOutletContext(); 

    const [ keyValue, setKeyValue ] = useState("user_id")
    const [ message , setMessage] = useState("")  

    const formSchema = yup.object().shape({
        first_name: yup.string().required("Must enter First Name").max(15),
        last_name: yup.string().required("Must enter Last Name").max(15),
        user_id: yup.string().required("Must enter a UserID").max(10),
        email: yup.string().email("Invalid email").required("Must enter email"),
      });

      const formik = useFormik({
        initialValues: {
          first_name: "",
          last_name: "",
          user_id: "",
          email: "",
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            // console.log("Form submitted");
            // console.log("Key Value: ", keyValue);
            // console.log("Form Data: ", formData);
            // const formData = {
            //     [keyValue]: values[keyValue]
            // };
            fetch(`/members/${member.id}`, {
                method: "PATCH",
                headers: {
                "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            })
            .then((r) =>{
                if(r.ok){
                    r.json()
                    .then((updatedMember)=>{
                        updateMember(updatedMember);
                        setMessage("Successfully Updated");
                        console.log(updatedMember)
                    });
                } else {
                    r.json()
                    .then((err) => setMessage(err.error));
                    console.log(message);
                }
            }).catch((error) => {
                console.error('Error: ', error);
            })
        }
    });

    return (
        <div id="memberEdit">
            <h3>Account information update</h3>
            <div className="dropdown">
                <label htmlFor="infochange">I want to change:</label>
                <select id="books" name="books" onChange={(e)=> setKeyValue(e.target.value)}>
                    <option value="user_id">UserID</option>
                    <option value="first_name">First Name</option>
                    <option value="last_name">Last Name</option>
                    <option value="email">Email Address</option>
                </select>
                <form onSubmit={formik.handleSubmit}>
                    <input
                        type="text"
                        id={keyValue}
                        name={keyValue}
                        autoComplete="off"
                        value={formik.values[keyValue]}
                        onChange={formik.handleChange}
                    />
                    <input type="submit" className="buttons"/>
                </form>
                <p>{message}</p>
            </div>
            <br/>
            <Link to={`/account`}>Close</Link>
        </div>
    );
}

export default AccountEdit;