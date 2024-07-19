import React, { useEffect, useState } from "react";
import { Link } from  "react-router-dom";
import { Outlet, useOutletContext } from "react-router-dom";
import Book from "../components/Book"

function BookIndex(){

    const [books, setBooks] = useState([]);

    useEffect(()=>{
        fetch('/books')
        .then((r) =>r.json())
        .then(setBooks);
    }, [])

    return (
        <div>
            <h2>Book Index</h2>
            <div className="allBooks">
                {books.map((book) => (
                    <Book bookData={book} />
                ))}
            </div>
        </div>
        
    )

}

export default BookIndex;