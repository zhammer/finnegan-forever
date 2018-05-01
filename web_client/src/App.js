import React from 'react';
import MechanicalTheatre from './MechanicalTheatre';
import Passage from './Passage';
import readFinneganPassage from './api';
import withTextIntervalReader from './textIntervalReader';
import './App.css';

const PassageWithTextIntervalReader = withTextIntervalReader(Passage, readFinneganPassage);

const App = () => (
    <div className="App">
      <MechanicalTheatre>
        <PassageWithTextIntervalReader />
      </MechanicalTheatre>
    </div>
);

export default App;
