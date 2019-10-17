import React from 'react';
import {Link} from 'react-router-dom';

function AboutPage(){
    return(
        <div className="jumbotron">
            <h1>About</h1>
            <p>Hey prime this is about page</p>
            <Link to="/" className="btn btn-primary">Home</Link>
        </div>
    )
}

export default AboutPage;