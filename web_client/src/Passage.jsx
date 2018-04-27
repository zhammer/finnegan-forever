import React, { Component } from 'react';
import readPassage from './api';
import './Passage.css';

class Passage extends Component {
    componentWillMount() {
        this.setState({passageText: ''});
        readPassage(this.props.finneganForeverUrl)
            .then(({ passage, reading_every }) => {
                this.setState({passageText: passage});
                const readingEvery = reading_every * 1000;
                setInterval(
                    () => {
                        readPassage(this.props.finneganForeverUrl).then(
                            ({ passage }) => {
                                this.setState({passageText: passage});
                            }
                        );
                    },
                    readingEvery
                );
            });
    }
    render() {
        return (
            <div className="grid">
              <div className="text">{this.state.passageText}</div>
            </div>
        )
    }
}

export default Passage;
