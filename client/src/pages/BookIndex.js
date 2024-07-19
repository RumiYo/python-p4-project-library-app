import React, { useEffect, useState } from "react";
import { Link } from  "react-router-dom";
import { Outlet, useOutletContext } from "react-router-dom";

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
            <ul>
                {books.map((book) => (
                <li key={book.id}>
                    <span>
                    {book.title} | Author: {book.author}
                    </span>
                </li>
                ))}
      </ul>
        </div>
        
    )

}

export default BookIndex;