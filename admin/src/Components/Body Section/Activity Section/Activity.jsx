import React from 'react'
import { BsArrowRightShort } from 'react-icons/bs'
import './activity.css'

const Activity = () => {
  return (
    <div className='activitySection'>
      <div className="heading flex">
        <h1>Rescent Activity</h1>
        <button className='btn flex'>
          See All
          <BsArrowRightShort className='icon'/>
        </button>
      </div>
    </div>
  )
}

export default Activity
