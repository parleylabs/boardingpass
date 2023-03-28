import React from 'react'
import { observer } from 'mobx-react'
import authStore from "../stores/AuthStore"


class Dashboard extends React.Component {
    authStore = authStore;

    logoutHandler = async () => {
        await this.authStore.loginSession.logout()
    }

    render() {
        return (
            <>
                <p>Welcome to Boarding Pass Dashboard</p>
                <button onClick={(e) => { e.preventDefault(); this.logoutHandler(); }}>
                    Logout
                </button>
            </>
        )
    }

}

export default observer(Dashboard)
