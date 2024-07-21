import { useEffect, useState } from "react";
import { useOutletContext  } from "react-router-dom";

function UserPage(){

    const { member } = useOutletContext(); 
    const [ loans, setLoans ] =useState([]);

    useEffect(() => {
        if (member) {
            setLoans(member.loans)
    }}, [loans, member.id]);

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

    if (!loans.length) {
        return <div>Loading...</div>;
    }

    return (
        <body>
            <h2>Account Summary</h2>
            <hr />
            <h3>Loaned or Returned Books</h3>    
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
            <br />
            <hr />
            <h3>Account Information</h3>
            <p>UserID: {member.user_id}</p>
            <p>First Name: {member.first_name}</p>
            <p>Last Name: {member.last_name}</p>
            <p>Email Address: {member.email}</p>
            <p>Password: ●●●●●●●●●</p>

        </body>
        
    )

}

export default UserPage;