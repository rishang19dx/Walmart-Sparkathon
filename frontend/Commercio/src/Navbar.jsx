import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // ✅ import navigation hook
import Search from './assets/search.svg';
import Chat from './assets/chat.svg';
import Cart from './assets/cart.svg';
import Avatar from './assets/avatar.svg';
import DD from './assets/dropdown.svg';

function Navbar() {
    const [query, setQuery] = useState('');
    const navigate = useNavigate(); // ✅ hook for navigation

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Search query:', query);
    };

    return (
        <div className='w-screen h-20 bg-white flex items-center justify-around border-b-2 border-gray-500'>
            <div className='text-3xl font-bold cursor-pointer'>Commercio</div>

            <div className='flex gap-15'>
                <div className='cursor-pointer' onClick={() => navigate('/')}>Home</div>
                <div className='cursor-pointer'>On Sale</div>
                <div className='cursor-pointer'>New Arrivals</div>
                <div className='cursor-pointer'>Brands</div>
            </div>

            <div>
                <form
                    onSubmit={handleSubmit}
                    className="flex items-center bg-white rounded-full px-3 py-2 w-90 shadow-md border-1 border-gray-600"
                >
                    <img src={Search} className="w-5 h-5 mr-2 cursor-pointer" />
                    <input
                        type="text"
                        placeholder="What are you looking for?"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        className="w-full bg-transparent outline-none placeholder-gray-500 text-sm text-gray-700"
                    />
                </form>
            </div>

            <div className='flex gap-3'>
                <img src={Chat} className='h-7 cursor-pointer' />
                <img src={Cart} className='h-7 cursor-pointer' />
            </div>

            <div className='flex bg-white rounded-3xl pl-0.5 pr-2 items-center gap-3 cursor-pointer h-9.5 shadow-md border-1 border-gray-600'>
                <div className='h-8 w-8 rounded-full bg-red-800 flex items-center justify-center'>
                    <img src={Avatar} className='h-full' />
                </div>
                <div className='text-gray-800 text-sm font-medium'>Harshit</div>
                <div>
                    <img src={DD} className='h-8' />
                </div>
            </div>
        </div>
    );
}

export default Navbar;
