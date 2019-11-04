import * as types from '../actions/actionTypes';
import initialState from './initialState';

export default function techReducer(state = initialState.tech, action){
	switch(action.type) {
		case types.CREATE_TECH_SUCCESS:
			debugger;
			return [...state, {...action.tech}]
		case types.UPDATE_TECH_SUCCESS:
			return state.map(tech=> 
				tech.id === action.tech.id ? action.tech: tech
			);
		case types.LOAD_TECH_SUCCESS:
			return action.tech;
		default:
			return state;
	}
}