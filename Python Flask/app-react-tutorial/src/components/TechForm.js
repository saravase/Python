import React from 'react';
import TextInput from '../common/TextInput';
import NumericInput from '../common/NumericInput';
import PropTypes from 'prop-types';

export default function TechForm(props){
	return(
			<div className="container">
				<div className="card">
					<div className="card-body">
						<form onSubmit={props.onSubmit}>
							<TextInput
							 	type="text"
							 	id="name"
							 	name="name"
							 	label="Name"
							 	onChange={props.onChange} 
							 	placeholder="Name" 
							 	value={props.tech.name}
							 	error={props.errors.name} />
							<NumericInput
								type="number"
								id="nod"
								name="nod"
								label="No Of Developer"
								onChange={props.onChange} 
								placeholder="No Of Developer"
								value={props.tech.nod} 
								error={props.errors.nod} />
							<NumericInput
								type="number"
								id="rank"
								name="rank"
								label="Rank"
								onChange={props.onChange}
								placeholder="Rank"
								value={props.tech.rank} 
								error={props.errors.rank} />
							<div className="form-group">
								<input type="submit" id="submit" name="submit" className="btn btn-primary"  value="Add"/>
							</div>
						</form>	
					</div>
				</div>
			</div>
		)
}

TechForm.propTypes = {
	tech : PropTypes.object.isRequired,
	errors : PropTypes.object.isRequired,
	onChange: PropTypes.func.isRequired,
	onSubmit: PropTypes.func.isRequired
};