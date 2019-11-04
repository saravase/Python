import * as types from './actionTypes';
import * as TechApi from '../../api/TechApi';
import { beforeApiCall } from './apiStatusActions';

export function loadTechSuccess(tech){
	return { type: types.LOAD_TECH_SUCCESS, tech};
}

export function createTechSuccess(tech){
	return { type: types.CREATE_TECH_SUCCESS, tech};	
}

export function updateTechSuccess(tech){
	return { type: types.UPDATE_TECH_SUCCESS, tech};	
}

export function loadTech(){
	return function(dispatch){
		dispatch(beforeApiCall());
		return TechApi.getTech().then(tech=>{
			dispatch(loadTechSuccess(tech['technology']));
		}).catch(error=>{
			throw error;
		})
	};
}

export function saveTech(tech){
	return function(dispatch, getState){
		dispatch(beforeApiCall());
		return TechApi.saveTech(tech).then(savedTech=>{
			dispatch(createTechSuccess(savedTech));
		}).catch(error=>{
			throw error;
		});
	};
}

export function updateTech(tech){
	return function(dispatch, getState){
		dispatch(beforeApiCall());
		return TechApi.updateTech(tech).then(updateTech=>{
			dispatch(updateTechSuccess(updateTech));
		}).catch(error=>{
			throw error;
		});
	};
}