import React from 'react'

function Homecard(props) {
  return (
    <div className='border-l-1 border-gray-800 px-3'>
      <div className='text-3xl font-bold'>{props.title}</div>
      <div>{props.content}</div>
    </div>
  )
}

export default Homecard
