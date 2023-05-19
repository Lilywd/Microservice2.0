import React, { useState } from "react"
import { BiSearch } from "react-icons/bi"
import { products } from "../../assets/data/data"
import { SearchItems } from "./SearchItems"

export const Hero = () => {
  
  const [value, setValue] = useState("")
  const onChanage = (e) => {
    setValue(e.target.value)
  }

  const onSearch = (key) => {
    setValue(key)
    console.log("search", key)
  }
  return (
    <>
      <section className='hero'>
        <div className='container'>
          <h1>
            <label>
              Welcome to <span>LEHKY.CO</span> Where We
            </label>
            <br />
            <label>
              Handcraft <span>Artisanal Candles </span> To Light Up Your <span>Life</span>
            </label>
          </h1>
          <p>The highest quality candles you can find, Your Candle, Right Away.</p>
          <div className='search'>
            <span>All Categories</span>
            <hr />
            <input type='text' placeholder='Search Candles...' onChange={onChanage} value={value}/>
            <button>
              <BiSearch className='serachIcon heIcon' />
            </button>
          </div>
          <SearchItems products={products} value={value} onSearch={onSearch} />
          <p>Examples: Oriental Scented Candle</p>
        </div>
      </section>
    </>
  )
}
