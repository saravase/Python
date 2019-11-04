import React from 'react';
import PropTypes from 'prop-types';

export default function NumericInput(props){

    let wrapperClass ="form-group";

	if(props.error.length>0){
		wrapperClass += " has-error"
	}

	return(
		<div className={wrapperClass}>
			<label>{props.label}</label>
			<input type={props.type} id={props.id} name={props.name} className="form-control" onChange={props.onChange} placeholder={props.placeholder} value={props.value} />
			{props.error && <div className="alert alert-danger">{props.error}</div>}
		</div>
		)
}

NumericInput.propTypes = {
    label : PropTypes.string.isRequired,
	type: PropTypes.string.isRequired,
	id: PropTypes.string.isRequired,
	name: PropTypes.string.isRequired,
	onChange: PropTypes.func.isRequired,
	value: PropTypes.string,
	error: PropTypes.string
};

NumericInput.defaultProps = {
	error : ''
};