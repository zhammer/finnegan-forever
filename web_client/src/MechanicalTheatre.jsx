import React from 'react';
import cloudLeft from './assets/cloud-left.png';
import cloudRight from './assets/cloud-right.png';
import waves from './assets/waves.png';
import './MechanicalTheatre.css';

/**
 *  A responsive Mechanical Theatre, inspired by the Victoria and Albert Museum's '18th-century
 *  Mechanical Theatre' display. Children are rendered beneath the clouds and above the waves.
 */
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
