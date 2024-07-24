import App from "./App";
import ErrorPage from "./pages/ErrorPage";
import Home from "./pages/Home";
import BookIndex from "./pages/BookIndex";
import UserPage from "./pages/UserPage";
import BookDetails from "./pages/BookDetails";
import AddBook from "./components/AddBook";
import AccountEdit from "./components/AccountEdit";
import AccountDelete from "./components/AccountDelete";


const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "/",
                element: <Home />,
            },
            {
                path: "/books",
                element: <BookIndex />,
                children: [
                    {
                        path: "/books/:id",
                        element: <BookDetails />
                    },
                    {
                        path: "/books/add",
                        element: <AddBook />
                    }

                ]
            },
            {
                path: "/account",
                element: <UserPage />,
                children: [
                    {
                        path: "/account/edit",
                        element: <AccountEdit />
                    },
                    {
                        path: "/account/delete",
                        element: <AccountDelete />
                    }
                ]
            }
        ]
    }
];

export default routes;