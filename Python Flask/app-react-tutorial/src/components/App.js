import React from 'react';
import HomePage from './HomePage';
import AboutPage from './AboutPage';
import TechPage from './TechPage';
import PageNotFoundPage from './PageNotFoundPage';
import ManageTechPage from './ManageTechPage';
import Header from '../common/Header';
import {Route, Switch, Redirect} from 'react-router-dom';
import {ToastContainer} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App(){
 /*   function getPage(){
        const route = window.location.pathname;
        if(route === '/tech') return <TechPage /> ;
        if(route === '/about') return <AboutPage /> ;
        return <HomePage />; 
    }*/

    return(
        <div className="container-fluid">
            <ToastContainer autoClose={3000} hideProgressBar />
            <Header />
            <Switch>
                <Route path="/" exact component={HomePage}/>
                <Route path="/tech" exact component={TechPage}/>
                <Route path="/about" exact component={AboutPage}/>
                <Route path="/technology/:rank" exact component={ManageTechPage}/>
                <Route path="/technology" exact component={ManageTechPage}/>
                <Redirect from="/about-page" to="/about" />
                <Route component={PageNotFoundPage}/>
            </Switch>
        </div>
    )
}

export default App;