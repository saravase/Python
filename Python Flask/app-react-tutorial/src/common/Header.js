import React from 'react';
import {NavLink} from 'react-router-dom';

function Header(){

	const activeStyle = { color: "orange"};

    return(
        <nav>
            <NavLink to="/" activeStyle={activeStyle} exact>Home</NavLink>
            {"|"}
            <NavLink to="/about" activeStyle={activeStyle} >About</NavLink>
            {"|"}
            <NavLink to="/tech" activeStyle={activeStyle} >Tech</NavLink>
        </nav>
    )
}

export default Header;