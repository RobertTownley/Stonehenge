import React, { Component } from 'react';
import {Link} from 'react-router-dom';

import Hero from './components/Hero';


export default class Home extends Component {
  render() {
    return (
      <div>
        <Hero />
        <h2>Congratulations: You've built Stonehenge</h2>
        <p>
          Your project has been successfully created. If you need more guidance or ideas
          of where to go from here, visit
          <a href='https://github.com/RobertTownley/Stonehenge'>the stonehenge documentation</a>. 
          Otherwise, happy coding!
        </p>
      </div>
    )
  }
}
