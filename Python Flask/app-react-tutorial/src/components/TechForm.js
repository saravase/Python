import React from 'react';
import TextInput from '../common/TextInput';

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
							 	value={props.tech.name} />
							<TextInput
								type="number"
								id="nod"
								name="nod"
								label="No Of Developer"
								onChange={props.onChange} 
								placeholder="No Of Developer"
								value={props.tech.nod} />
							<TextInput
								type="number"
								id="rank"
								name="rank"
								label="Rank"
								onChange={props.onChange}
								placeholder="Rank"
								value={props.tech.rank} />
							<div className="form-group">
								<input type="submit" id="submit" name="submit" className="btn btn-primary"  value="Add"/>
							</div>
						</form>	
					</div>
				</div>
			</div>
		)
}