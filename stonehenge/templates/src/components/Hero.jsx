import React, { Component } from 'react';
import {Link} from 'react-router-dom';


export default class Hero extends Component {
  render() {
    return (
      <div className='hero'>
        <img src='images/stonehenge.jpg' alt='Image of Stonehenge, taken by Inja Pavlic'/>
        <h1>Welcome to Stonehenge</h1>
      </div>
    )
  }
}
