import React from 'react';
import {Link} from 'react-router-dom';

const HomePage = ()=> (
	<div className="jumbotron">
		<h1>Home</h1>
		<p> This is home page prime</p>
		<Link to="about" className="btn btn-primary">About</Link>
	</div>
	);

export default HomePage;