import { useRouteError } from "react-router-dom";

function ErrorPage(){
    
    const error = useRouteError();

    return (
        <main>
            <h1>Woops! Something went wrong!</h1>
        </main>
    )
}

export default ErrorPage;