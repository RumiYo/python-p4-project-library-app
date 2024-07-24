import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { useFormik } from 'formik';
import * as yup from "yup";

function AddBook(){

    const [ message , setMessage] = useState("") ; 
    const [ book , setBook] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();

    const formSchema = yup.object().shape({
        title: yup.string().required("Must enter Book title").max(50, "Title must be at most 50 characters long"),
        author: yup.string().required("Must enter Author Name").max(30, "Author name must be at most 30 characters long"),
        publish_year: yup.number().integer("Publish year must be an integer").max(new Date().getFullYear(), "Publish year cannot be in the future"),
        page: yup.number().integer("Page count must be an integer").positive("Page count must be positive number"),
        image_url: yup.string().url("Must have a valid URL").required("Must enter the image URL for the book cover"),
        summary: yup.string().required("Must enter the book summary"),
        star:yup.number().min(0, "Star rating cannot be negative").max(5,"Star rating cannot be more than 5")
      });

    const formik = useFormik({
        initialValues: {
            title: "",
            author: "",
            publish_year: "",
            page: "",
            image_url: "",
            summary:"",
            star: "",
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
        setIsLoading(true);
        console.log(values);
        fetch("/books", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(values),
        })
        .then((r) => {
            setIsLoading(false);
            if (r.ok) {
            r.json()
            .then((newBook) => {
                setBook(newBook)
                setMessage("Book added successfully!")
                navigate(`/books/${newBook.id}`); 
            });
            } else {
            r.json().then((err) => {
                setMessage(err.error)
                console.log(message)
            });
            }
        })
        }
    })
    

    return (
        <div  id="memberEdit">
            <h3>Please give us all info about your favorite book </h3>
            <form onSubmit={formik.handleSubmit}>
                <label htmlFor="title">Title:  </label>
                    <input
                    type="text"
                    id="title"
                    autoComplete="off"
                    value={formik.values.title}
                    onChange={formik.handleChange}
                    /><br/>
                    <label htmlFor="autor">Author:  </label>
                    <input
                    type="text"
                    id="author"
                    autoComplete="off"
                    value={formik.values.author}
                    onChange={formik.handleChange}
                    /><br/>
                    <label htmlFor="publish_year">Publish Year:  </label>
                    <input
                    type="number"
                    id="publish_year"
                    autoComplete="off"
                    value={formik.values.publish_year}
                    onChange={formik.handleChange}
                    /><br/>
                    <label htmlFor="page">Page:  </label>
                    <input
                    type="number"
                    id="page"
                    autoComplete="off"
                    value={formik.values.page}
                    onChange={formik.handleChange}
                    /><br/>
                    <label htmlFor="image_url">Image URL:  </label>
                    <input
                    type="text"
                    id="image_url"
                    autoComplete="off"
                    value={formik.values.image_url}
                    onChange={formik.handleChange}
                    /><br/>
                    <label htmlFor="summary">Summary:  </label>
                    <input
                    type="text"
                    id="summary"
                    autoComplete="off"
                    value={formik.values.summary}
                    onChange={formik.handleChange}
                    /><br/>
                    <label htmlFor="star">Star:  </label>
                    <input
                    type="number"
                    id="star"
                    autoComplete="off"
                    value={formik.values.star}
                    onChange={formik.handleChange}
                    />
                    <br/>
                    <input type="submit" className="buttons" disabled={isLoading} value={isLoading ? "Submitting..." : "Submit"}/>
            </form>
                <p>{message}</p>
            <br/>
            <Link to={`/books`}>Close</Link>
        </div>
    )
}

export default AddBook