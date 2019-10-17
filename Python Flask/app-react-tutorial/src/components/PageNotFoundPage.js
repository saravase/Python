import React from 'react';
import {Link} from 'react-router-dom';

function PageNotFoundPage(){

	return(
			<div className="jumbotron">
				<h1>Page Not Found Error</h1>
				<p><Link to="/" exact>Back to Home</Link></p>
			</div>
		)
}

export default PageNotFoundPage;