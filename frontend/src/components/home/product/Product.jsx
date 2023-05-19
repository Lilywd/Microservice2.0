import { useState } from "react"
import { products } from "../../assets/data/data"
import { Heading } from "../../common/Heading"
import { ProductItem } from "./ProductItems"

export const Product = () => {
  const [data, setdata] = useState(products)
  console.log(setdata)
  return (
    <>
      <section className='product'>
        <div className='container'>
          <Heading title='Products' desc='Check Here' />

          <ProductItem data={data} />
        </div>
      </section>
    </>
  )
}
