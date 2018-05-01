import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './Passage.css';

class Passage extends Component {
    state = {
        text: '',
    }
    componentDidMount() {
        this.props.readPassage()
            .then(({ text, readingEvery }) => {
                this.setState({text: text});
                setInterval(
                    () => {
                        this.props.readPassage().then(
                            ({ text }) => {
                                this.setState({text: text});
                            }
                        );
                    },
                    readingEvery * 1000
                );
            });
    }
    render() {
        return (
            <div className="container">
              <div className="text">{this.state.text}</div>
            </div>
        );
    }
}

Passage.propTypes = {
    readingEvery: PropTypes.function
};

export default Passage;
