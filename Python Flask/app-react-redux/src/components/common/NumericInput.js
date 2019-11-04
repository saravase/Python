import React from 'react';
import PropTypes from 'prop-types';

const NumericInput= ({
	label,
	type,
	id,
	name,
	placeholder,
	onChange,
	value,
	error
 })=>{
	let wrapperClass ="form-group";

	if(error.length>0){
		wrapperClass += " has-error"
	}

	return(
		<div className={wrapperClass}>
			<label>{label}</label>
			<input 
				type={type}
				id={id}
				name={name}
				className="form-control"
				onChange={onChange}
				placeholder={placeholder}
				value={value} 
			/>
			{error && <div className="alert alert-danger">{error}</div>}
		</div>
		)
}

NumericInput.propTypes = {
	label : PropTypes.string.isRequired,
	type: PropTypes.string.isRequired,
	id: PropTypes.string.isRequired,
	name: PropTypes.string.isRequired,
	placeholder: PropTypes.string.isRequired,
	onChange: PropTypes.func.isRequired,
	value: PropTypes.number,
	error: PropTypes.string
};

NumericInput.defaultProps = {
	error : ''
};

export default NumericInput;

