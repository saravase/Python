import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

function TechList(props){
	return (
		<div className="container-fluid">
                <div className="row">
                    <div className="col-xl-12">
                        <div className="card">
                            <div className="card-body">
                                <table className="table table-bordered table-striped">
                                    <thead className="table-primary">
                                        <tr>
                                            <th>&nbsp;</th>
                                            <th>Name</th>
                                            <th>No Of Developer</th>
                                           <th>Rank</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                    {props.tech.map(t => {
                                        return <tr key={t.id}>
                                            <td><input type="button" onClick={()=>props.deleteTech(t.rank)} className="btn btn-outline-danger" value="Delete" /></td>
                                            <td><Link to={"/technology/"+t.rank}>{t.name}</Link></td>
                                            <td>{t.nod}</td>
                                            <td>{t.rank}</td>
                                        </tr>
                                    })}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
}

TechList.propTypes = {
	tech : PropTypes.arrayOf(PropTypes.shape({
		name : PropTypes.string.isRequired,
		nod : PropTypes.number.isRequired,
		rank : PropTypes.number.isRequired
	})).isRequired
};
export default TechList;