import React, { Component, Fragment }from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from "react-router-dom";
import ReactDom from 'react-dom';
import Header from './layout/Header';
import Dashboard from './turmas/Dashboard';
import toModel from './toModel/toModel';
import login from './login/login';
import { Provider } from 'react-redux';
import store from '../store';


class App extends Component {
    render() {
        return(
            <Provider store = {store}>
                <Router>
                    <Fragment>
                        <Header />
                            <div className="container">
                                <Switch>
                                    <Route exact path="/" component={Dashboard} />
                                    <Route exact path="/toModel" component={toModel} />
                                    <Route exact path="/login" component={login} />
                                </Switch>
                            </div>
                    </Fragment>
                </Router>
            </Provider>
        );
    }
}
ReactDom.render( <App /> ,document.getElementById('app')
);