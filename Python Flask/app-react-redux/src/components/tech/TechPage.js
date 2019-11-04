import React from 'react';
import {Link} from 'react-router-dom';
import {connect} from 'react-redux';
import * as techActions from '../../redux/actions/techActions';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import TechList from './TechList';
import Spinner from '../common/Spinner';


class TechPage extends React.Component{
	componentDidMount(){
		const {actions, tech} = this.props;

		if(tech.length === 0){
			actions.loadTech().catch(error=>{
				alert("Loading tech failes"+ error);
			});
		}
	}

	render(){
		return (
			<>
				<div className="jumbotron">
					<h1>Tech</h1>
					<p> This is tech page prime</p>
					<Link to="/get-tech" className="btn btn-primary">Add Tech</Link>
				</div>
				{this.props.loading ? <Spinner/> :(
					<>
					<div className="container">
						<TechList tech={this.props.tech} />
					</div>
					</>
				)}
			</>
		)
	}
}

TechPage.propTypes = {
	tech: PropTypes.array.isRequired,
	actions: PropTypes.object.isRequired,
	loading: PropTypes.bool.isRequired,
}

function mapStateToProps(state){
	debugger;
	return {
		tech: state.tech,
		loading: state.apiCallInProgress > 0
	}
}


//Type -2
//createTech: course => dispatch(techActions.createTech(course))

function mapDispatchToProps(dispatch){
	return {
		actions: {
			loadTech: bindActionCreators(techActions.loadTech, dispatch)	
		}
	}
}


export default connect(mapStateToProps, mapDispatchToProps)(TechPage);