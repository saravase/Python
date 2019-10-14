import React from 'react';
import { getTech } from '../api/TechApi';

class TechPage extends  React.Component{

    state = {
        tech : []
    };

    componentDidMount(){
        getTech().then(tech=> {
            this.setState({ tech : tech['technology']});
            console.log(tech['technology']);
        });
    }

    render(){
        return(
            <>
            <div className="jumbotron bg-info">
                <h1>Technology</h1>
                <p>Hey Prime this is Technology page</p>
            </div>
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
                                    {this.state.tech.map(tech => {
                                        return <tr key={tech['rank']}>
                                            <td>{tech['name']}</td>
                                            <td>{tech['nod']}</td>
                                            <td>{tech['rank']}</td>
                                        </tr>
                                    })}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </>
        )
    }
}

export default TechPage;