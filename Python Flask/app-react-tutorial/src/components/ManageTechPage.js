import React, {useState} from 'react';
import TechForm from './TechForm';
import * from '../api/TechApi';

const ManageTechPage = props=>{
	const [tech, setTech] = useState({
		name: '',
		nod:0,
		rank:0
	});

	function handleChange({target}){
		setTech({
			...tech, [target.name]: target.value
		});		
	}

	function handleOnSubmit(event){
		event.preventDefault();
		TechApi.saveTech(tech);
	}

	return(
		<>
			<div className="jumbotron">
				<h1>ManageTechPage</h1>
			</div>
			<TechForm onChange={handleChange} onSubmit={handleOnSubmit} tech={tech} />
		</>
		)
};

export default ManageTechPage;