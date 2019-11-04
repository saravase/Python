import {combineReducers} from 'redux';
import tech from './techReducer';
import apiCallInProgress from './apiStatusReducer';

const rootReducer = combineReducers({
	tech,
	apiCallInProgress
});

export default rootReducer;