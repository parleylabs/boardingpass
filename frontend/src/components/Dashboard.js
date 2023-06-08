import React from 'react'
import { observer } from 'mobx-react'
import authStore from "../stores/AuthStore"
import { Header, Divider, Message } from 'semantic-ui-react'
import ApiService from '../services/ApiService'

class Dashboard extends React.Component {
    authStore = authStore;
    ApiService = ApiService;
    constructor() {
        super();
        this.state = { data: [] };
    }

    logoutHandler = async () => {
        await this.authStore.loginSession.logout()
    }

    handleLogin = async (e) => {
        e.preventDefault()
         const result = await ApiService.transfer_keys({
            org_id: this.org_id.value,
            dev_euis: [this.dev_euis.value],
        });
        this.setState({ data: JSON.stringify(result, null, 2) });
        console.log(JSON.stringify(result, null, 2))
    }

    render() {
        return (
            <>
                <br/>
                <Header as='h1'>Boarding Pass</Header>
                <Divider/>
                <p>Welcome to Boarding Pass Dashboard</p>
                <button onClick={(e) => { e.preventDefault(); this.logoutHandler(); }}>
                    Logout
                </button>
                <br/>  <br/>
                <p>Transfer Device Keys</p>
                 <form onSubmit={this.handleLogin}>
                    <input type="org_id" placeholder="Org ID to Transfer to"   ref={input => this.org_id = input}  /><br/><br/>
                     <input type="dev_euis" placeholder="Dev EUIs" ref={input => this.dev_euis = input} /><br/><br/>
                     <button type="submit">submit</button>
                  </form>
                  <br/>
                   <Message>
                    <Message.Header>Output</Message.Header>
                    <pre>
                      { this.state.data }
                    </pre>
                  </Message>
                  <br/><br/>
            </>
        )
    }

}

export default observer(Dashboard)
