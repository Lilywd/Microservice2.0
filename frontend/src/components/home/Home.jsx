import React from "react"
import { BiCard } from "react-icons/bi"
import { Banner } from "./banner/Banner"
import { Blog } from "./blog/Blog"
import { Details } from "./details/Details"
import { Hero } from "./Hero/Hero"
import { Card } from "./Hero/Card"
// import { Price } from "./price/Price"
import { Product } from "./product/Product"
import { Testimonial } from "./testimonial/Testimonial"
import { TopProduct } from "./top/TopProduct"

export const Home = () => {
  return (
    <>
      <Hero />
      <Card />
      <Product />
      <Banner />
      <TopProduct />
      {/* <Price /> */}
      <Testimonial />
      <Blog />
    </>
  )
}
