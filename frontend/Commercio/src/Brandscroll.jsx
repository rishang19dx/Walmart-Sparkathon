import React from 'react';
import { motion } from 'framer-motion';
import Prada from './assets/prada.svg';
import Gucci from './assets/gucci.svg';
import Zara from './assets/zara.svg';
import Puma from './assets/puma.svg';
import Nike from './assets/nike.svg';
import Dior from './assets/dior.svg';
import Versace from './assets/versace.svg';
import Adidas from './assets/adidas.svg';

const brands = [Prada, Nike, Gucci, Puma, Zara, Versace, Dior, Adidas];

function Brandscroll() {
  const repeatedBrands = [...brands, ...brands, ...brands]; // repeat 3x for seamless loop

  return (
    <div className="relative w-screen overflow-hidden bg-black h-28">
      <motion.div
        className="flex w-max"
        animate={{ x: ['0%', '-33.333%'] }} // scroll only one third since we repeated 3x
        transition={{
          repeat: Infinity,
          ease: 'linear',
          duration: 20,
        }}
      >
        {repeatedBrands.map((brand, i) => (
          <img key={i} src={brand} alt="brand" className="h-24 mx-8" />
        ))}
      </motion.div>
    </div>
  );
}

export default Brandscroll;
