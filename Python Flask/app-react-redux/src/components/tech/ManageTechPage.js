import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';
import {connect} from 'react-redux';
import {loadTech, saveTech, updateTech} from '../../redux/actions/techActions';
import PropTypes from 'prop-types';
import TechForm from './TechForm';
import Spinner from '../common/Spinner';
import {toast} from 'react-toastify';

function ManageTechPage({
	tech,
	loadTech,
	saveTech,
	updateTech,
	history,
	...props
}){
	const [technology, setTechnology] = useState({...props.technology});
	const [errors, setErrors] = useState({});
	const [saving, setSaving] = useState(false);

	useEffect(()=>{
		debugger;
		if(tech.length === 0){
			loadTech().catch(error=>{
				alert("Loading tech failes"+ error);
			});
		}else{
			setTechnology({...props.technology});
		}
	}, [props.technology]);

	function handleChange(event){
		const {name,value} = event.target;
		setTechnology(prevTech=>({
			...prevTech,
			[name]: name === 'nod' || name === 'rank'? parseInt(value ,10): value
		}))
	}

	function handleSave(event){
		event.preventDefault();
		setSaving(true);
		technology.id? 
		updateTech(technology).then(()=>{
			toast.success('Tech Updated')
			history.push('/tech')
		}): 
		saveTech(technology).then(()=>{
			toast.success('Tech Saved')
			history.push('/tech')
		});
	}
		
	return (
			tech.length === 0 ? <Spinner/> : (
			<>
			<div className="jumbotron">
				<h1>Manage Tech</h1>
				<p> This is manage tech page prime</p>
				<Link to="tech" className="btn btn-primary">Tech</Link>
			</div>
			<div className="container">
				<TechForm
				technology={technology}
				errors={errors}
				onChange={handleChange}
				onSave={handleSave}
				saving = {saving}
				/>
			</div>
			</>
			)
		
	)
}

ManageTechPage.propTypes = {
	technology: PropTypes.object.isRequired,
	tech: PropTypes.array.isRequired,
	loadTech: PropTypes.func.isRequired,
	saveTech: PropTypes.func.isRequired,
	updateTech: PropTypes.func.isRequired,
	history: PropTypes.object.isRequired
}

function getTechById(tech, id){
	debugger;
	return tech.find(_tech=> _tech['id'] === id) || null;
}

function mapStateToProps(state, ownProps){
	const id = parseInt(ownProps.match.params.id);
	const technology = id && state.tech.length>0 ? getTechById(state.tech, id): {
			name: '',
			nod: 0,
			rank: 0
		}; 
	return {
		technology,
		tech: state.tech
	}
}

const  mapDispatchToProps = {
	loadTech,
	saveTech,
	updateTech
}

export default connect(mapStateToProps, mapDispatchToProps)(ManageTechPage);