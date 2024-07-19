import { useParams, Outlet, useOutletContext  } from "react-router-dom";
import { Link } from "react-router-dom";

function BookDetails(){

    const params = useParams();
    const { booksList } = useOutletContext();

    const book = booksList.find(item => item.id === parseInt(params.id))

    return (

        <div id="bookDetail">

             <h1>{book.title}</h1>
             <img src={book.image_url} alt={book.title} id="bookDetailImage"/>
             <p><b>Rating: </b>{book.star}</p>
             <p><b>Author: </b>{book.author}</p>
             <p><b>Publish year: </b>{book.publish_year}</p>
             <h4>Summary</h4>
             <p>{book.summary}</p>
             <Link id="closeDetails" to={`/books`}>Close details</Link> 
        </div>
    )
}

export default BookDetails;