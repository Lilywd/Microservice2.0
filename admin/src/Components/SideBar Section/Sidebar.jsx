import React from 'react'
import './sidebar.css'
import logo from '../../Assets/logo.jpg'
import {IoMdSpeedometer} from 'react-icons/io'
import {BsTrophy, BsCreditCard2Front} from 'react-icons/bs'
import {BiTrendingUp} from 'react-icons/bi'
import {AiOutlinePieChart} from 'react-icons/ai'
import {FaRegQuestionCircle} from 'react-icons/fa'
import {MdDeliveryDining, MdOutlineExplore, MdOutlinePermContactCalendar} from 'react-icons/md'

const Sidebar = () => {
  return (
    <div className='sideBar grid'>
        <div className='logoDiv flex'>
            <img src={logo} alt='Image'/>
            <h2>LC ADMIN</h2>
        </div>

        <div className="menuDiv">
            <h3 className="divTitle">
                QUICK MENU
            </h3>
            <ul className="menuLists grid">
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <IoMdSpeedometer className = 'icon'/>
                        <span className="smallText">
                            Home
                        </span>
                    </a>
                </li>                
                
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <MdDeliveryDining className = 'icon'/>
                        <span className="smallText">
                            Orders
                        </span>
                    </a>
                </li>                
                                
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <MdOutlineExplore className = 'icon'/>
                        <span className="smallText">
                            Explore
                        </span>
                    </a>
                </li>                
                
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <BsTrophy className = 'icon'/>
                        <span className="smallText">
                            Products
                        </span>
                    </a>
                </li>

            </ul>
        </div>        
        
        <div className="settingsDiv">
            <h3 className="divTitle">
                SETTINGS
            </h3>
            <ul className="menuLists grid">
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <AiOutlinePieChart className = 'icon'/>
                        <span className="smallText">
                            Charts
                        </span>
                    </a>
                </li>                
                
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <BiTrendingUp className = 'icon'/>
                        <span className="smallText">
                            Trends
                        </span>
                    </a>
                </li>                
                                
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <MdOutlinePermContactCalendar className = 'icon'/>
                        <span className="smallText">
                            Contact
                        </span>
                    </a>
                </li>                
                
                <li className="listItem">
                    <a href='#' className='menuLink flex'>
                        <BsCreditCard2Front className = 'icon'/>
                        <span className="smallText">
                            Billing
                        </span>
                    </a>
                </li>

            </ul>
        </div>

        <div className="sideBarCard">
            <FaRegQuestionCircle className='icon'/>
            <div className="cardContent">
                <div className="circle1"></div>
                <div className="circle2"></div>

                <h3>Help Center</h3>
                <p>Help center</p>
                <button className='btn'>Help</button>
            </div>
        </div>
    </div>
  )
}

export default Sidebar
