import React from 'react'
import { observer } from 'mobx-react'
import authStore from "../stores/AuthStore"
import StorageService from '../services/StorageService'
import { Redirect } from 'react-router'


class LoginForm extends React.Component {
    authStore = authStore;
    StorageService = StorageService;

    handleLogin = async (e) => {
        e.preventDefault()
        await authStore.loginSession.login({
            username: this.username.value,
            password: this.password.value,
        });
    }

    render() {
        if (StorageService.getToken() || authStore.loginSession.isAuthenticated) {
            return <Redirect to='/dashboard' />
        }
        return (

            <div className='login'>
                <p>Login Form</p>
                 <form onSubmit={this.handleLogin}>
                     <input type="text" placeholder="Username"   ref={input => this.username = input}  /><br/><br/>
                     <input type="password" placeholder="Password" ref={input => this.password = input} /><br/><br/>
                     <button type="submit">submit</button>
                  </form>
            </div>
        )
    }

}

export default observer(LoginForm)
