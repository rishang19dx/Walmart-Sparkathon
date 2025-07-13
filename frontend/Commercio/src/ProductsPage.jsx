// src/ProductsPage.jsx
import React, { useEffect, useState } from 'react';
import ProductCard from './Productcard';
import Tshirt from './assets/t-shirt.jpg';

const mockProducts = [
  {
    name: "UrbanFit Classic Tee",
    description: "Breathable cotton, perfect for everyday wear.",
    price: 499
  },
  {
    name: "ActiveDry Sports Tee",
    description: "Lightweight, moisture-wicking for your workouts.",
    price: 599
  },
  {
    name: "StreetWear Oversized Tee",
    description: "Trendy oversized fit with bold print.",
    price: 699
  },
  {
    name: "Minimalist Essential Tee",
    description: "Simple design, premium fabric, timeless style.",
    price: 549
  },
  {
    name: "Retro Vintage Tee",
    description: "Washed look with classic retro graphics.",
    price: 649
  },
  {
    name: "EcoSoft Organic Tee",
    description: "Made from 100% organic cotton for comfort & sustainability.",
    price: 749
  }
];


function ProductsPage() {
  const [products, setProducts] = useState(mockProducts);  // show mock until backend confirms real

  useEffect(() => {
    fetch("http://localhost:8000/products")
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log("Fetched data:", data);
        if (Array.isArray(data) && data.length > 0) {
          setProducts(data);
        } else {
          console.warn("Backend empty or invalid. Keeping mock data.");
        }
      })
      .catch(error => {
        console.error("Error fetching products:", error);
        // Do nothing because mock data is already in place
      });
  }, []);


  return (
    <div className="flex flex-wrap justify-start w-full bg-zinc-300 gap-4 p-4">
      {products.map((product, index) => (
        <ProductCard
          key={index}
          link={Tshirt}
          name={product.name}
          description={product.description}
          price={product.price}
        />
      ))}
    </div>
  );
}

export default ProductsPage;
