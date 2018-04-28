import React, { Component } from 'react';
import clouds from './assets/clouds.png';
import waves from './assets/waves.png';
import './MechanicalTheatre.css';

class MechanicalTheatre extends Component {
    render() {
        return (
            <div className="stage">
              <div className="clouds">
                <img className="picture" src={clouds} alt=""/>
              </div>
              <div className="content">
                {this.props.children}
              </div>
              <div className="waves">
                <img className="picture" src={waves} alt=""/>
              </div>
            </div>
        );
    }
}

export default MechanicalTheatre;
