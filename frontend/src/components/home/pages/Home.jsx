import React from 'react'
import { Hero } from '../Hero/Hero'
import { Card } from '../Hero/Card'
import { Product } from '../product/Product'
import { Banner } from '../banner/Banner'
import { TopProduct } from '../top/TopProduct'
// import { Price } from '../price/Price'
import { Testimonial } from '../testimonial/Testimonial'
import { Blog } from '../blog/Blog'

export const Home = () => {
    return (
        <>
        <Hero />
        <Card />
        <Product />
        <Banner />
        <TopProduct />
        {/* <Price/> */}
        <Testimonial />
        <Blog/>
        </>
    )
}
