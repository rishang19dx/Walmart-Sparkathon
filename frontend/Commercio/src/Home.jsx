import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Homecard from './Homecard';
import Homeimg01 from './assets/homeimg01.png';
import Homeimg02 from './assets/homeimg02.png';
import Homeimg03 from './assets/homeimg03.png';
import Homeimg04 from './assets/homeimg04.png';
import { Link } from 'react-router-dom';

function Home() {
  const images = [Homeimg01, Homeimg02, Homeimg03, Homeimg04];
  const [index, setIndex] = useState(0);
  const [direction, setDirection] = useState(1);

  useEffect(() => {
    const timer = setInterval(() => {
      setDirection(1);
      setIndex((prev) => (prev + 1) % images.length);
    }, 5000);

    return () => clearInterval(timer);
  }, [images.length]);

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

        <Link
  to="/products"
  className='bg-black text-white w-max py-3 px-6 rounded-full cursor-pointer inline-block'
>
  Shop Now
</Link>


        <div className='flex gap-5'>
          <Homecard title="200+" content="International Brands" />
          <Homecard title="2,000+" content="High-Quality Products" />
          <Homecard title="30,000+" content="Happy Customers" />
        </div>
      </div>

      <div className='flex-1 h-full overflow-hidden relative flex items-center justify-center'>
        <div className='w-full h-full relative'>
          <AnimatePresence initial={false} custom={direction}>
            <motion.img
              key={index}
              src={images[index]}
              alt={`Slide ${index + 1}`}
              custom={direction}
              initial={{ opacity: 0, x: direction > 0 ? 100 : -100 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: direction > 0 ? -100 : 100 }}
              transition={{
                x: { type: 'tween', duration: 0.5 },
                opacity: { duration: 0.25 }  // ⬅️ Faster fade-out
              }}
              className='absolute w-full h-full object-contain'
            />

          </AnimatePresence>
        </div>
      </div>
    </div>
  );
}

export default Home;
