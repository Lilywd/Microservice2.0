import React from 'react'
import { BiSearchAlt } from 'react-icons/bi'
import { IoMdNotificationsOutline } from 'react-icons/io'
import { TbMessageCircle } from 'react-icons/tb'
import './top.css'
import img from '../../../Assets/usericon2.png'
import img2 from '../../../Assets/cpng.png'
import video from '../../../Assets/banner.jpg'
import { BsArrowRightShort } from 'react-icons/bs'
// import { FaRegQuestionCircle } from 'react-icons/fa'

const Top = () => {
  return (
    <div className='topSection'>
      <div className="headerSection flex">
        <div className="title">
          <h1>LC ADMIN PANEL</h1>
          <p>Hello Admin, Welcome back!</p>
        </div>

        <div className="searchBar flex">
          <input type="text" placeholder='Search..'/>
          <BiSearchAlt className='icon'/>
        </div>

        <div className="adminDiv flex">
          <TbMessageCircle className='icon'/>
          <IoMdNotificationsOutline className='icon'/>
          <div className="adminImage">
            <img src={img} alt="LC LOGO" />
          </div>
        </div>
      </div>

      <div className="cardSection flex">
        <div className="rightCard flex">
          <h1>Create and Sell extraordinary products</h1>
          <p>Welcome to LEHKY.CO, where we handcraft artisanal candles to light up your life.</p>

          <div className="buttons flex">
            <button className='btn'>Explore More</button>
            <button className='btn transparent'>Top Sellers</button>
          </div>

          <div className="videoDiv">
            <img src={video} alt="" />
          </div>
        </div>

        <div className="leftCard flex">
          <div className="main flex">

            <div className="textDiv">
              <h1>Stats</h1>

              <div className="flex">
                <span>
                  Today <br /> <small>4 Orders</small>
                </span>
                <span>
                  This Month <br /> <small>142 Orders</small>
                </span>
              </div>         

              <span className="flex link">
                Go to my orders <BsArrowRightShort className='icon'/>
              </span>
            </div>

            <div className="imgDiv">
              <img src={img2} alt="Image name" />
            </div>

            {/* Will be used Later*/}
            {/* <div className="sideBarCard">
            <FaRegQuestionCircle className='icon'/>
            <div className="cardContent">
                <div className="circle1"></div>
                <div className="circle2"></div>

                <h3>Help Center</h3>
                <p>Help center</p>
                <button className='btn'>Help</button>
            </div>
            </div> */}

          </div>
        </div>
      </div>
    </div>
  )
}

export default Top
