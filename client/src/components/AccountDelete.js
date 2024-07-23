import { Link, useOutletContext } from "react-router-dom";

function AccountDelete(){

    const { member, updateMember } = useOutletContext(); 

    function handleSubmit(e){
        e.preventDefault();
        console.log("Delete", member.id)
    }

    return (
        <div id="memberEdit">
            <h3>Delete Account</h3>
            <form onSubmit={handleSubmit}>
            <p>Are you sure you want to delete your account?</p>
            <input type="submit" value="Yes, Delete my account" className="buttons"/>
            </form>
            <br/><br/>
            <Link to={`/account`}>Close</Link>
        </div>

    )
}

export default AccountDelete;