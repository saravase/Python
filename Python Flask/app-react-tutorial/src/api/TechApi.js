import { handleResponse, handleError} from './apiUtils';
const baseUrl = 'http://localhost:5000/';

export  function getTech(){
    return fetch(baseUrl+'get-tech/')
    .then(handleResponse)
    .catch(handleError);
}


export  function saveTech(tech){
	return fetch(baseUrl+'add-tech/'+(tech.id || ''),{
		method: tech.id? 'PUT': 'POST',
		headers: {'content-type': 'application/json'},
		body: JSON.stringify(
			...tech
			)
	}).then(handleResponse)
    .catch(handleError);
}