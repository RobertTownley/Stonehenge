import React, { Component } from 'react';
import stonehengeImage from '../images/stonehenge.jpg';


export default class Hero extends Component {
  render() {
    return (
      <div className='hero'>
        <img src={stonehengeImage} alt='Stonehenge, taken by Inja Pavlic'/>
        <div className='hero__content'>
          <h1>Welcome to Stonehenge</h1>
          <p>You've done it! You built stonehenge!</p>
        </div>
      </div>
    )
  }
}
