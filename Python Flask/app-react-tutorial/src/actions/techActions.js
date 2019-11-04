import dispatcher from '../appDispatcher';
import * as TechApi from '../api/TechApi';
import actionTypes from './actionTypes';

export function saveTech( tech){
	return TechApi.saveTech(tech).then(saveTech=>{
		debugger;
		dispatcher.dispatch({
			actionType: actionTypes.CREATE_TECH,
			tech: saveTech
		});
	});
}

export function updateTech(tech){
	return TechApi.updateTech(tech).then(updateTech=>{
		dispatcher.dispatch({
			actionType: actionTypes.UPDATE_TECH,
			tech: updateTech
		});
	});
}

export function loadTech(){
	return TechApi.getTech().then(tech=>{
		dispatcher.dispatch({
			actionType: actionTypes.LOAD_TECH,
			tech: tech['technology']
		});
	});
}

export function deleteTech(rank){
	return TechApi.deleteTech(rank).then(()=>{
		dispatcher.dispatch({
			actionType: actionTypes.DELETE_TECH,
			rank: rank
		});
	});
}
