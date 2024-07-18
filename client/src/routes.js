import App from "./App";
import ErrorPage from "./pages/ErrorPage";
import Home from "./pages/Home";
import BookIndex from "./pages/BookIndex";
import UserPage from "./pages/UserPage";


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
            },
            {
                path: "/account",
                element: <UserPage />
            }
        ]
    }
];

export default routes;