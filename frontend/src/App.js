import React, { Component } from 'react'

class App extends Component {

    render() {
        return (
          <main>
                {this.props.children}
           </main>
        );
    }
}

export default App;
