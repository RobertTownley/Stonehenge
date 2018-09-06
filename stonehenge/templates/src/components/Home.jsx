import React, { Component } from 'react';

import Hero from './Hero';


export default class Home extends Component {
  render() {
    return (
      <div>
        <Hero />
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
