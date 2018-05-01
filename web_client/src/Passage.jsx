import React from 'react';
import PropTypes from 'prop-types';
import './Passage.css';

/**
 *  A component for prettily displaying text.
 */
const Passage = ({ text }) => (
    <div className="container">
      <div className="text">{text}</div>
    </div>
);

Passage.propTypes = {
    text: PropTypes.string
};

export default Passage;
