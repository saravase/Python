import { handleResponse, handleError} from './apiUtils';
const baseUrl = 'http://localhost:5000/';

export function getTech(){
    return fetch(baseUrl+'get-tech')
    .then(handleResponse)
    .catch(handleError);
}


export function saveTech(tech){
	debugger;
	return fetch(baseUrl+'add-tech',{
		method:'POST',
		headers: {'content-type': 'application/json'},
		body: JSON.stringify(
			tech
			)
	}).then(handleResponse)
    .catch(handleError);
}

export function updateTech(tech){
	debugger;
	return fetch(baseUrl+'replace-tech/'+tech['rank'],{
		method:'PUT',
		headers: {'content-type': 'application/json'},
		body: JSON.stringify(
			tech
			)
	}).then(handleResponse)
    .catch(handleError);	
}


export function deleteTech(rank){
	return fetch(baseUrl+'delete-tech/'+rank,{
		method: 'DELETE',
		headers:{'content-type': 'application/json'}
	}).then(handleResponse)
	.catch(handleError);
}

export function getTechByRank(rank){
	debugger;
	return fetch(baseUrl+'get-tech/'+rank).then(response=>{
		if(!response.ok) throw new Error('Network response was not ok.');
		return response.json().then(tech=> {
			console.log(tech)
			if (tech[rank] === undefined) throw new Error('Tech not found: '+rank)
			return convertDataFormat(tech[rank]);
		});		
	}).catch(handleError);
}

var convertDataFormat = function(tech){
	tech['rank'] = tech['rank'].toString();
	tech['nod'] = tech['nod'].toString();
	return tech
};