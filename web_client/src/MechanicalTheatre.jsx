import React, { Component } from 'react';
import cloudLeft from './assets/cloud-left.png';
import cloudRight from './assets/cloud-right.png';
import waves from './assets/waves.png';
import './MechanicalTheatre.css';

const MechanicalTheatre = ({ children }) => (
    <div className="stage">
      <div className="clouds">
        <div className="cloudRight">
          <img className="picture" src={cloudRight} alt=""/>
        </div>
        <div className="cloudLeft">
          <img className="picture" src={cloudLeft} alt=""/>
        </div>
      </div>
      <div className="content">
        {children}
      </div>
      <div className="waves">
        <img className="picture" src={waves} alt=""/>
      </div>
    </div>
);

export default MechanicalTheatre;
