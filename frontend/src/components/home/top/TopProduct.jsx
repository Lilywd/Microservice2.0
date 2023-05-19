import React, { useState } from "react"
import { topProducts } from "../../assets/data/data"
import { Heading } from "../../common/Heading"
import { ProductItem } from "../product/ProductItems"

export const TopProduct = () => {
  const [data, setdata] = useState(topProducts)
  const allCategories = ["all", ...new Set(data.map((item) => item.category))]
  const [category, setCategory] = useState(allCategories)

  /*console.log(setCartItems)
  console.log(setCategory)
  console.log(allCategories)*/

  const handleFilter = (category) => {
    const newItem = topProducts.filter((item) => item.category === category)
    setCategory(newItem)

    if (category === "all") {
      setCategory(topProducts)
      return
    }
  }
  return (
    <>
      <section className='topproduct'>
        <div className='container'>
          <div className='head'>
            <Heading title='Top Selling Products' desc='Multipurpose candles for every home! Giving light to the world.' />
            <div className='category'>
              {category.map((category) => (
                <button className='button' onClick={() => handleFilter(category)}>
                  {category}
                </button>
              ))}
            </div>
          </div>
          <ProductItem data={data} />
        </div>
      </section>
    </>
  )
}
