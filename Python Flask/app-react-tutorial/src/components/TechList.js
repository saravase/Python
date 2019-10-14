import React from 'react';

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
                                            <th>Name</th>
                                            <th>No Of Developer</th>
                                           <th>Rank</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                    {props.tech.map(t => {
                                        return <tr key={t.rank}>
                                            <td>{t.name}</td>
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

export default TechList;