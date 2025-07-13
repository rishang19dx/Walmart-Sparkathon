import React, { useState, useContext } from 'react';
import Star from './assets/star.svg';
import SizeFinderModal from './SizeFinderModal';
import { WalletModalContext } from './App';

function Productcard(props) {
  const [modalOpen, setModalOpen] = useState(false);
  const [recommendedSize, setRecommendedSize] = useState(null);
  const [selectedSize, setSelectedSize] = useState(null);
  const [dimensions, setDimensions] = useState(null);
  const { user, openWalletModal } = useContext(WalletModalContext);

  const handleSizeSubmit = ({ size, sizeCm }) => {
    setRecommendedSize(size);
    setSelectedSize(size);
    setDimensions(sizeCm); // optional display
  };

  const sizes = ['Small', 'Medium', 'Large', 'X-Large'];

  const handleAddToCart = () => {
    if (!user) {
      openWalletModal();
      return;
    }
    if (!selectedSize) {
      alert('Please select a size before adding to cart.');
      return;
    }
    // Cart logic
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const existing = cart.find(item => item.name === props.name && item.size === selectedSize);
    if (existing) {
      existing.quantity += 1;
    } else {
      cart.push({
        name: props.name,
        price: props.price,
        size: selectedSize,
        quantity: 1
      });
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Added to cart!');
  };

  return (
    <div className='bg-zinc-300 md:gap-20 p-3 flex flex-col md:flex-row md:justify-around justify-center border-b-2'>
      <SizeFinderModal isOpen={modalOpen} onClose={() => setModalOpen(false)} onSubmit={handleSizeSubmit} />

      <div className='md:flex md:gap-3'>
        <div className='h-60 w-full md:w-80 md:h-100 bg-zinc-400 rounded-2xl'>
          <img src={props.link} className='object-cover w-full h-full rounded' />
        </div>
        <div className='flex md:h-100 mt-3 justify-between md:flex-col md:gap-3 md:mt-0'>
          <div className='h-25 w-25 md:h-28 bg-zinc-400 rounded-2xl'>
            <img src={props.link} className='object-cover w-full h-full rounded' />
          </div>
          <div className='h-25 w-25 md:h-28 bg-zinc-400 rounded-2xl'>
            <img src={props.link} className='object-cover w-full h-full rounded' />
          </div>
          <div className='h-25 w-25 md:h-28 bg-zinc-400 rounded-2xl'>
            <img src={props.link} className='object-cover w-full h-full rounded' />
          </div>
        </div>
      </div>

      <div className='md:w-150'>
        <div className='text-2xl mt-3 font-extrabold'>{props.name}</div>

        <div className='flex items-center'>
          {[...Array(4)].map((_, i) => <img key={i} src={Star} className='h-5' />)}
          <div className='text-base font-semibold ml-5'>4</div>
          <div className='text-base text-zinc-600'>/5</div>
        </div>

        <div className='text-xl font-bold mt-3'>${props.price}</div>

        <div className='text-xs text-zinc-600 mt-3'>
          {props.description}
        </div>

        <hr className='w-full text-zinc-400 mt-5' />

        <div>
          <div className='mt-3 flex items-center justify-between'>
            <div className='text-zinc-600'>Choose Size</div>
            <div
              onClick={() => setModalOpen(true)}
              className='bg-black text-white py-1 px-3 cursor-pointer text-xs rounded-3xl'
            >
              Find Your Size
            </div>
          </div>

          <div className='flex text-sm items-center justify-between mt-2 gap-2'>
            {sizes.map(size => (
              <div
                key={size}
                onClick={() => setSelectedSize(size)}
                className={`px-3 py-1 rounded-3xl cursor-pointer transition-colors duration-200
                  ${selectedSize === size
                    ? 'bg-black text-white'
                    : 'bg-white text-zinc-600 border border-zinc-400'}
                `}
              >
                {size}
              </div>
            ))}
          </div>

          {recommendedSize && (
            <div className='mt-2 text-sm text-green-600 font-semibold'>
              Recommended Size: {recommendedSize}
              {dimensions && (
                <span className='text-xs block text-zinc-500 mt-1'>
                  Shoulder: {dimensions.shoulderCm.toFixed(1)} cm,
                  Waist: {dimensions.hipCm.toFixed(1)} cm
                </span>
              )}
            </div>
          )}

        </div>

        <hr className='w-full text-zinc-400 mt-5' />

        <div className='text-white bg-black px-5 py-3 items-center justify-center flex rounded-3xl mt-5 cursor-pointer' onClick={handleAddToCart}>
          Add to Cart
        </div>
      </div>
    </div>
  );
}

export default Productcard;
