import React, { useEffect, useState } from "react";
import { Outlet, useOutletContext } from "react-router-dom";
import Book from "../components/Book"

function BookIndex(){

    const [books, setBooks] = useState([]);
    const { member } = useOutletContext();

    useEffect(()=>{
        fetch('/books')
        .then((r) =>r.json())
        .then(setBooks);
    }, [])


    return (
        <div>
            <h2>Book Index</h2>
            <Outlet context={{booksList: books, member:member }}/>
            <div className="allBooks">
                {books.map((book) => (
                    <Book bookData={book} key={book.id}/>
                ))}
            </div>
        </div>
        
    )

}

export default BookIndex;