import React, { Component } from 'react';
import MechanicalTheatre from './MechanicalTheatre';
import Passage from './Passage';
import './App.css';

const FINNEGAN_FOREVER_URL = "https://drsvfxtdvi.execute-api.us-east-1.amazonaws.com/dev/passage";

class App extends Component {
    render() {
        return (
            <div className="App">
              <MechanicalTheatre>
                <Passage finneganForeverUrl={FINNEGAN_FOREVER_URL}/>
              </MechanicalTheatre>
            </div>
        );
    }
}

export default App;
