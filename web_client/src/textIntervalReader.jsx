import React, { Component } from 'react';
import PropTypes from 'prop-types';

/**
 *  A higher order component that reads text from `readTextInterval`: an async function that returns
 *  `{ text, readingEvery }`, where `text` is a text string read and `readingEvery` is the number
 *  of seconds after which new `text` should be read. Every `readingEvery` seconds, this component
 *  will read text from `readTextInterval` and pass the read text to `WrappedComponent`s `text` prop.
 */
const withTextIntervalReader = (WrappedComponent, readTextInterval) => (
    class extends Component {
        state = {
            text: ''
        }
        onTextIntervalRead = ({ text }) => {
            this.setState({ text });
        }
        onFirstTextIntervalRead = ({ text, readingEvery }) => {
            this.intervalId = setInterval(() => {
                readTextInterval().then(this.onTextIntervalRead);
            }, readingEvery * 1000);
            this.onTextIntervalRead({text});
        }
        componentDidMount() {
            readTextInterval()
                .then(this.onFirstTextIntervalRead);
        }
        componentWillUnmount() {
            clearInterval(this.intervalId);
        }
        render = () => (
            <WrappedComponent text={this.state.text} {...this.props} />
        );
    }
);

withTextIntervalReader.propTypes = {
    WrappedComponent: PropTypes.element.isRequired,
    readTextInterval: PropTypes.func.isRequired
};

export default withTextIntervalReader;
