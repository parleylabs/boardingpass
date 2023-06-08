import React, { Component } from 'react'
import { Container } from 'semantic-ui-react'

class App extends Component {

    render() {
        return (
          <main>
                <Container>
                    {this.props.children}
                </Container>
           </main>
        );
    }
}

export default App;
