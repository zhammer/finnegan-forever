import React from 'react';
import PropTypes from 'prop-types';
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';
import './Passage.css';

/**
 *  A component for prettily displaying text. Text will fade in and out on Component mount /
 *  unmount. If the { text } prop is updated during the component's lifetime, the old text will
 *  crossfade into the new text.
 */
const Passage = ({ text }) => (
    <div className="container">
      <ReactCSSTransitionGroup
        transitionName="example"
        transitionEnterTimeout={250}
        transitionLeaveTimeout={250}>

        <div key={text} className="text">{text}</div>

      </ReactCSSTransitionGroup>
    </div>
);

Passage.propTypes = {
    text: PropTypes.string
};

export default Passage;
