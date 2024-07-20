import React, { useEffect, useState } from "react";
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
            <Outlet context={{booksList: books}}/>
            <div className="allBooks">
                {books.map((book) => (
                    <Book bookData={book} key={book}/>
                ))}
            </div>
        </div>
        
    )

}

export default BookIndex;