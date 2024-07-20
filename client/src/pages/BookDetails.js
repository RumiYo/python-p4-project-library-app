import { useParams, Outlet, useOutletContext  } from "react-router-dom";
import { useState } from "react";
import { Link } from "react-router-dom";

function BookDetails(){

    const params = useParams();
    const { booksList, member } = useOutletContext();
    const [errors, setErrors] = useState([]);

    const book = booksList.find(item => item.id === parseInt(params.id))

    function handleSubmitLoan(e){
        e.preventDefault();
        const currentDate = new Date();
        console.log("loan", member.id, member.user_id, book.id, book.title, currentDate)
        const formData = {
            book_id: book.id,
            member_id: member.id
        }
        console.log(formData)
        fetch("/loans", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
          }).then((r) => {
            if (r.ok) {
              r.json()
              .then((loan) => {
                console.log(loan)
              });
             } else {
            //    r.json().then((err) => setErrors(err.errors));
                console.log('no_data')
             }
          });
    }

    function handleSubmitReturn(e){
        e.preventDefault();
        console.log("return")
    }

    if (!book) {
        return <div>Loading...</div>;
    }

    return (

        <div id="bookDetail">

                <h1>{book.title}</h1>
                <img src={book.image_url} alt={book.title} id="bookDetailImage"/>
                <p><b>Rating: </b>{book.star}</p>
                <p><b>Author: </b>{book.author}</p>
                <p><b>Publish year: </b>{book.publish_year}</p>
                <h4>Summary</h4>
                <p>{book.summary}</p>
                <form onSubmit={handleSubmitLoan}>
                  <input type="submit" id="loan" value="Loan this book" />
                </form>
                <form onSubmit={handleSubmitReturn}>
                    <input type="submit" id="return" value="Return this book" />
                 </form>
             <Link id="closeDetails" to={`/books`}>Close details</Link> 
        </div>
    )
}

export default BookDetails;