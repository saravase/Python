import React, {useState, useEffect} from 'react';
import { getTech } from '../api/TechApi';
import TechList from './TechList';


function TechPage(){

	const [tech, setTech] = useState([]);

	useEffect(()=> {
		getTech().then(_tech=> setTech(_tech['technology']));
	}, [])

	return(
			<>
            <div className="jumbotron bg-info">
                <h1>Technology</h1>
                <p>Hey Prime this is Technology page</p>
            </div>
            <TechList tech={tech} />
            </>
		)
}

export default TechPage;