import React from 'react';
import TextInput from '../common/TextInput';
import NumericInput from '../common/NumericInput';
import PropTypes from 'prop-types';

const TechForm =({
	technology,
	onSave,
	onChange,
	saving =false,
	errors ={}
})=>{
	return(
			<div className="container">
				<div className="card">
					<div className="card-body">
						<form onSubmit={onSave}>
							<h2>{technology.id ? "Edit": "Add"} Tech</h2>
							{errors.onSave && (
								<div className="alert alert-danger">{errors.onSave}</div>
								)
							}
							<TextInput
							 	type="text"
							 	id="name"
							 	name="name"
							 	label="Name" 
							 	onChange={onChange}
							 	placeholder="Name" 
							 	value={technology.name}
							 	error={errors.name}
							 />
							<NumericInput
								type="number"
								id="nod"
								name="nod"
								label="No Of Developer"
								onChange={onChange}
								placeholder="No Of Developer"
								value={technology.nod}
								error={errors.nod}
							/>
							<NumericInput
								type="number"
								id="rank"
								name="rank"
								label="Rank"
								onChange={onChange}
								placeholder="Rank"
								value={technology.rank}
								error={errors.rank}
							/>
							<div className="form-group">
								<input type="submit" id="submit" name="submit" className="btn btn-primary"  value={saving? "Saving...": "Save"} disabled={saving}/>
							</div>
						</form>	
					</div>
				</div>
			</div>
		)
}

TechForm.propTypes = {
	technology : PropTypes.object.isRequired,
	errors : PropTypes.object.isRequired,
	onChange: PropTypes.func.isRequired,
	onSave: PropTypes.func.isRequired,
	saving: PropTypes.bool
};

export default TechForm;