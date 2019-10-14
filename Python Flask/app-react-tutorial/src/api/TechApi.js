import { handleResponse, handleError} from './apiUtils';
const baseUrl = 'http://localhost:5000/get-tech';

export function getTech(){
    return fetch(baseUrl)
    .then(handleResponse)
    .catch(handleError);
}