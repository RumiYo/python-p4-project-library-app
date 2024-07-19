import App from "./App";
import ErrorPage from "./pages/ErrorPage";
import Home from "./pages/Home";
import BookIndex from "./pages/BookIndex";
import UserPage from "./pages/UserPage";
import BookDetails from "./pages/BookDetails";


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
                    }
                ]
            },
            {
                path: "/account",
                element: <UserPage />
            }
        ]
    }
];

export default routes;