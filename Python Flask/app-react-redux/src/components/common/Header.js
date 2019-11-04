import React from 'react';
import {NavLink} from 'react-router-dom';

const Header = ()=>{
	const activeStyle= { color: "#F15B2A"};
	const style = {backgroundColor: "#fff"};
	return(
		<nav style={style}>
			<NavLink to="/" activeStyle= {activeStyle} exact>Home</NavLink>{" | "}
			<NavLink to="/about" activeStyle= {activeStyle} >About</NavLink>{" | "}
			<NavLink to="/tech" activeStyle= {activeStyle} >Tech</NavLink>
		</nav>
		)
}

export default Header;
