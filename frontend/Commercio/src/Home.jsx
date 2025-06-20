import React, { useEffect, useState } from 'react';
import Homecard from './Homecard';
import Homeimg01 from './assets/homeimg01.png';
import Homeimg02 from './assets/homeimg02.png';
import Homeimg03 from './assets/homeimg03.png';
import Homeimg04 from './assets/homeimg04.png';

function Home() {
  const images = [Homeimg01, Homeimg02, Homeimg03, Homeimg04];
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prev) => (prev + 1) % images.length);
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className='h-[calc(100vh-5rem-6.25rem)] bg-zinc-300 flex'>
      <div className='w-3/5 h-full pt-10 pl-20 flex flex-col gap-8'>
        <div className='text-6xl font-extrabold'>
          <div>FIND OUTFITS</div>
          <div>THAT MATCHES</div>
          <div>YOUR STYLE</div>
        </div>

        <div className='text-gray-800'>
          Browse through our diverse range of meticulously crafted garments,
          <br />
          designed to bring out your individuality and cater to your sense of style.
        </div>

        <div className='bg-black text-white w-max py-3 px-15 rounded-full'>Shop Now</div>

        <div className='flex gap-5'>
          <Homecard title="200+" content="International Brands" />
          <Homecard title="2,000+" content="High-Quality Products" />
          <Homecard title="30,000+" content="Happy Customers" />
        </div>
      </div>

      <div className='flex-1 h-full overflow-hidden relative'>
        <div
          className='whitespace-nowrap transition-transform duration-700 h-full pt-5'
          style={{ transform: `translateX(-${index * 100}%)` }}
        >
          {images.map((src, i) => (
            <img
              key={i}
              src={src}
              className='inline-block w-full h-full object-contain'
              alt={`Slide ${i + 1}`}
            />
          ))}
        </div>
      </div>

    </div>
  );
}

export default Home;
