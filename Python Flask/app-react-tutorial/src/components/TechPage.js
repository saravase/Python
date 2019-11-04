import React, {useState, useEffect} from 'react';
import TechList from './TechList';
import TechStore from '../stores/techStore';
import {loadTech, deleteTech} from '../actions/techActions';
import {Link} from 'react-router-dom';

function TechPage(){

	const [tech, setTech] = useState(TechStore.getTech());

	useEffect(()=> {
		TechStore.addChangeListener(onChange);
		if(TechStore.getTech().length === 0) loadTech();
		return ()=> TechStore.removeChangeListener(onChange);
	}, [])

	function onChange(){
		setTech(TechStore.getTech());
	}

	return(
			<>
            <div className="jumbotron bg-info">
                <h1>Technology</h1>
                <p>Hey Prime this is Technology page</p>
            </div>
            <div className="text-right"><Link to="/technology" exact className="btn btn-primary mb-1">New Tech</Link></div>
            <TechList tech={tech}  deleteTech = {deleteTech}/>
            </>
		)
}

export default TechPage;