import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';


const TechList = ({tech})=>(
	<div className="card">
	<div className="card-body">
	<table className="table table-bordered table-striped">
		<caption>Technology List</caption>
		<thead>
			<tr className="table-info">
				<th>Name</th>
				<th>No of developer</th>
				<th>Rank</th>
			</tr>
		</thead>
		<tbody>
			{ tech.map(_tech=>(
					<tr key={_tech['id']}>
						<td><Link to={'/get-tech/'+_tech['id']}>{_tech['name']}</Link></td>
						<td>{_tech['nod']}</td>
						<td>{_tech['rank']}</td>
					</tr>
			))}
		</tbody>
	</table>
	</div>
	</div>
)

TechList.propTypes = {
	tech: PropTypes.array.isRequired
}

export default TechList;