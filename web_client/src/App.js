import React, { Component } from 'react';
import MechanicalTheatre from './MechanicalTheatre';
import Passage from './Passage';
import readFinneganPassage from './api';
import './App.css';



const App = () => (
    <div className="App">
      <MechanicalTheatre>
        <Passage readPassage={readFinneganPassage}/>
      </MechanicalTheatre>
    </div>
);

export default App;
