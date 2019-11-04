import {EventEmitter} from 'events';
import Dispatcher from '../appDispatcher';
import actionTypes from '../actions/actionTypes';

const CHANGE_EVENT ='change';
let _tech = [];

class TechStore extends EventEmitter{

	addChangeListener(callback){
		this.on(CHANGE_EVENT, callback);
	}

	removeChangeListener(callback){
		this.removeListener(CHANGE_EVENT, callback);
	}

	emitChange(){
		this.emit(CHANGE_EVENT);
	}	

	getTech(){
		console.log(_tech);
		return _tech;
	}

	getTechByRank(rank){
		debugger;
		return _tech.find(tech=> tech.rank.toString() === rank);
	}
}


const store = new  TechStore();

Dispatcher.register(action=>{
	switch(action.actionType){
		case actionTypes.CREATE_TECH:
			debugger;
			_tech.push(action.tech);
			store.emitChange();
			break;
		case actionTypes.UPDATE_TECH:
			_tech = _tech.map(tech=> tech.rank === action.tech.rank? action.tech : tech);
			store.emitChange();
			break;
		case actionTypes.LOAD_TECH:
			_tech = action.tech;
			store.emitChange();
			break;
		case actionTypes.DELETE_TECH:
			_tech = _tech.filter(tech=> tech.rank !== parseInt(action.rank, 10));
			store.emitChange();
			break;
		default:	
			//nothing
	}
});

export default store;