import React from 'react'
import Prada from './assets/prada.svg';
import Gucci from './assets/gucci.svg';
import Zara from './assets/zara.svg';

function Brandscroll() {
  return (
    <div className='h-25 w-screen bg-black flex'>
      <img src={Prada} className='h-25' />
      <img src={Gucci} className='h-25' />
      <img src={Zara} className='h-25' />
    </div>
  )
} 

export default Brandscroll
