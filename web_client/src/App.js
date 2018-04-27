import React, { Component } from 'react';
import Passage from './Passage';
import './App.css';

const FINNEGAN_FOREVER_URL = "https://drsvfxtdvi.execute-api.us-east-1.amazonaws.com/dev/passage";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Passage finneganForeverUrl={FINNEGAN_FOREVER_URL}/>
      </div>
    );
  }
}

export default App;
