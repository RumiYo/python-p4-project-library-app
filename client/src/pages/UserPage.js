import { useEffect, useState } from "react";
import { useOutletContext, Outlet } from "react-router-dom";
import { Link } from "react-router-dom";

function UserPage(){

    const { member, updateMember } = useOutletContext(); 
    const [ loans, setLoans ] =useState([]);

    useEffect(() => {
        fetch(`/members/${member.id}`)
        .then((r)=> {
          if(r.ok){
            r.json().then((member) => {
                updateMember(member)
                setLoans(member.loans)
          })
          }
        })
      }, []);

    const bookslist = loans.map(loan =>
        (
            <tr key={loan.id}>
                <td>{loan.returned_date ? "Returned":"Loaned"}</td>
                <td>{loan.book.title}</td>
                <td>{loan.book.author}</td>
                <td>{loan.loan_date}</td>
                <td>{loan.returned_date}</td>
        </tr>
        ))

    if (!member) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>Account Summary</h2>
            <hr />
            <h3>Loaned or Returned Books</h3>    
            <table id="accountBooksList">
                <thead>
                    <tr>
                        <th>Status</th>
                        <th>Book Title</th>
                        <th>Book Author</th>
                        <th>Loaned Date</th>
                        <th>Returned Date</th>
                    </tr>
                </thead>
                <tbody>
                    {bookslist}
                </tbody>
            </table>
            <br />
            <hr />
            <h3>Account Information</h3>
            <div id="accountDetail">
                <p>UserID:  {member.user_id}</p>
                <p>First Name:  {member.first_name}</p>
                <p>Last Name:  {member.last_name}</p>
                <p>Email Address:  {member.email}</p>
                <p>Password:  ●●●●●●●●●</p>
                <Link to={`/account/edit`} >Update your account information</Link> 
                <Outlet  context={{member: member, updateMember:updateMember}} />
            </div>
        </div>
        
    )

}

export default UserPage;