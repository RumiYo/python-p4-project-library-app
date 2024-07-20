import React from "react"
import { Link } from "react-router-dom";
import "../App.css";

function Book({ bookData }){

    return (
         <div className="bookList">
            <img src={bookData.image_url} alt={bookData.title} className="bookListImage"/>
            <h5>{bookData.title}</h5>
            <small>Rating: {bookData.star}</small><br/>
            <small>Author {bookData.author}</small><br/>
            <small>Year: {bookData.publish_year}</small><br/>
            <small>
             <Link to={`/books/${bookData.id}`} >View details</Link> 
            </small> 
        </div>
    )
}

export default Book;