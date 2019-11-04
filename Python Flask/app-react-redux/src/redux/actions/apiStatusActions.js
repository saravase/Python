import * as types from './actionTypes';

export function beforeApiCall(){
	return {
		type: types.BEFORE_API_CALL
	};
}