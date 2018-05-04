import React from 'react';
import MechanicalTheatre from './MechanicalTheatre';
import Passage from './Passage';
import readFinneganPassage from './api';
import withTextIntervalReader from './textIntervalReader';
import './App.css';

const PassageWithTextIntervalReader = withTextIntervalReader(Passage, readFinneganPassage);

/**
 *  Where the words of Finnegan's Wake pass through the bits and bytes of time, beneath the clouds
 *  and above the waves. ("A way a lone a last a loved a long the")
 */
const App = () => (
    <div className="App">
      <MechanicalTheatre>
        <PassageWithTextIntervalReader />
      </MechanicalTheatre>
    </div>
);

export default App;
