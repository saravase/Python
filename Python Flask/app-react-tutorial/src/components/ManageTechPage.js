import React, {useState, useEffect} from 'react';
import TechForm from './TechForm';
import TechStore from '../stores/techStore';
import {toast} from 'react-toastify';
import * as techActions from '../actions/techActions';

const ManageTechPage = props=>{
	const [errors, setErrors] = useState({});
	const [technology, setTechnology] = useState(TechStore.getTech());
	const [tech, setTech] = useState({
		name: '',
		nod:'',
		rank:''
	});

	useEffect(()=>{
		TechStore.addChangeListener(onChange);
		const rank= props.match.params.rank;
		if(technology.length === 0){
			techActions.loadTech();
		}else if(rank){
			setTech(TechStore.getTechByRank(rank));
		}
		return ()=> TechStore.removeChangeListener(onChange);
	}, [technology.length, props.match.params.rank]);

	function onChange(){
		setTechnology(TechStore.getTech());
	}

	function handleChange({target}){
		setTech({
			...tech, [target.name]: target.value
		});		
	}

	function handleOnSubmit(event){
		event.preventDefault();
		if(!formIsValid()) return;
		const rank = props.match.params.rank;
		if(rank){
			techActions.updateTech(tech).then(()=>{
			props.history.push('/tech');
			toast.success('Data Updated')
			});
		}else{
			techActions.saveTech(tech).then(()=>{
			props.history.push('/tech');
			toast.success('Data Saved')
			});
		}
	}

	function formIsValid(){
		const _errors={};
		if(!tech.name) _errors.name = "Technology name required";
		if(!tech.nod) _errors.nod = "Technology no of developer required";
		if(!tech.rank) _errors.rank = "Technology rank required";
		setErrors(_errors);
		// check errors object
		return Object.keys(_errors).length === 0;
	}

	return(
		<>
			<div className="jumbotron">
				<h1>ManageTechPage</h1>
			</div>
			<TechForm onChange={handleChange} onSubmit={handleOnSubmit} tech={tech} errors={errors}/>
		</>
		)
};

export default ManageTechPage;