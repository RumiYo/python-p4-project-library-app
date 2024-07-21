import { useParams, Outlet, useOutletContext  } from "react-router-dom";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function BookDetails(){

    const params = useParams();
    const { member } = useOutletContext();
    const [ error, setError] = useState([])
    const [ loaned, setLoaned ] = useState(false)
    const [ book, setBook ] = useState(null)   
    const [ loan, setLoan ] = useState(null)

    useEffect(() => {
        fetch(`/books/${parseInt(params.id)}`)
        .then((r)=> {
          if(r.ok){
            r.json().then((book) => setBook(book))
          }
        })
      }, [params.id]);

      useEffect(() => {
        if (book) {
            for (let loan of book.loans) {
                if (loan.member.id === member.id && loan.returned_date === null) {
                    setLoaned(true);
                    setLoan(loan);
                    break;
                }
            }
        }
    }, [book, member.id]);

    function handleSubmitLoan(e){
        e.preventDefault();
        const formData = {
            book_id: book.id,
            member_id: member.id
        }
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
                console.log(loan);
                setLoaned(true);
                setLoan(loan)
              });
             } else {
                r.json().then((err) => setError(err.error));
             }
          }).catch((error) => {
            console.error('Error:', error);
        });
    }

    function handleSubmitReturn(e){
        e.preventDefault();
        fetch(`/loans/${loan.id}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({}),
          }).then((r) => {
            if (r.ok) {
              r.json()
              .then((loan) => {
                setLoaned(false);
                setLoan(null)
              });
             } else {
                r.json().then((err) => setError(err.error));
             }
          }).catch((error) => {
            console.error('Error:', error);
        });

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
                  <input type="submit" id="loan" value={loaned ? "Loaned" :  "Loan this book"} disabled={loaned} />
                </form>
                <form onSubmit={handleSubmitReturn}>
                    <input type="submit" id="return" value="Return this book" disabled={!loaned} />
                 </form>
             <Link id="closeDetails" to={`/books`}>Close details</Link> 
        </div>
    )
}

export default BookDetails;