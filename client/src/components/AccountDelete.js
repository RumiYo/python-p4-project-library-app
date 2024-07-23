import { Link, useOutletContext } from "react-router-dom";
import { useState } from "react";

function AccountDelete(){

    const { member, updateMember } = useOutletContext(); 
    const [ message , setMessage] = useState("") 

    function handleSubmit(e){
        e.preventDefault();
        console.log("Delete", member.id)
        const loans = member.loans
        console.log(loans)
        loans.forEach((loan) => {
            fetch(`/loans/${loan.id}`, {
                method: "DELETE",
            })
            .then((r) => {
                if (!r.ok) {
                    r.json().then((err) => setMessage(err.error));
                    console.log(message)
                }
            })
        })
        fetch(`/members/${member.id}`, {
            method: "DELETE",
          }).then((r) => {
            if (r.ok) {
              updateMember(null);
            } else {
                r.json().then((err) => setMessage(err.error));
                console.log(message)
            }
        })
     }

    

    return (
        <div id="memberEdit">
            <h3>Delete Account</h3>
            <form onSubmit={handleSubmit}>
            <p>Are you sure you want to delete your account?</p>
            <input type="submit" value="Yes, Delete my account" className="buttons"/>
            <p>Once you click this delete button, you will be signed out from the app</p>
            </form>
            <br/><br/>
            <Link to={`/account`}>Close</Link>
        </div>

    )
}

export default AccountDelete;