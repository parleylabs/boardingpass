import React, { Component } from 'react'
import routes from '../routing/routes'
import { Link } from 'react-router-dom'


/**
 * Home page extra component
 */
class Home extends Component {

    render() {
        return <div className="ut__home">
            <h2>Welcome to Boarding Pass</h2>
            <section className="ut__btn-group">
                <Link className="ut__button" to={routes.login}>Sign in</Link>
            </section>
        </div>
    }

}

export default Home
