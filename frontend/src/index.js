import React from 'react'
import ReactDOM from 'react-dom';
import { Provider } from 'mobx-react'
import { Router, Switch, Route } from 'react-router'
import history from './services/history'
import App from './App'
import Home from './components/Home'
import LoginForm from './components/LoginForm'
import Dashboard from './components/Dashboard'
import routes from './routing/routes'
import authStore from './stores/AuthStore'
import 'semantic-ui-css/semantic.min.css'

const stores = {
    authStore,
};

ReactDOM.render(
    <Provider { ...stores }>
        <App>
            <Router history={history}>
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route path={routes.login} component={LoginForm} />
                    <Route path={routes.dashboard} component={Dashboard} />
                </Switch>
            </Router>
        </App>
    </Provider>,
    document.getElementById('root')
);
