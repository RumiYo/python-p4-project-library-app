import { Link, useParams, useOutletContext } from "react-router-dom";
import { useState, useEffect } from "react";

function AccountEdit() {
    const params = useParams();
    const { member, updateMember } = useOutletContext(); 

    const [ keyValue, setKeyValue ] = useState("user_id")
    const [ inputValue, setInputValue ] = useState("")
    const [ memberInfo, setMemberInfo ] = useState(member)  
    const [ message , setMessage] = useState("")  

    function handleSubmit(e){
        e.preventDefault();
        const formData = {
            [keyValue]: inputValue
        }
        fetch(`/members/${member.id}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
          })
          .then((r) => {
            if (r.ok) {
              r.json()
              .then((updatedMember) => {
                updateMember(updatedMember)
                setMessage("Successfully Updated")
              });
             } else {
                r.json().then((err) => setMessage(err.error));
                console.log(message)
             }
          }).catch((error) => {
            console.error('Error:', error);
        });
    }

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
                <form onSubmit={handleSubmit}>
                <input
                        type="text"
                        id={keyValue}
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                    />
                    <input type="submit" className="buttons"/>
                </form>
                <p>{message}</p>
            </div>
            <br/>
            <Link to={`/account`}>Close Account Information Update</Link>
        </div>
    );
}

export default AccountEdit;