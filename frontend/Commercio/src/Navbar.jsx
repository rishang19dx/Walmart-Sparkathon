import React, { useState, useContext, useRef, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Search from './assets/search.svg';
import Heart from './assets/heart.svg';
import Cart from './assets/cart.svg';
import Avatar from './assets/avatar.svg';
import DD from './assets/dropdown.svg';
import { WalletModalContext } from './App';

function Navbar({ user }) {
    const [query, setQuery] = useState('');
    const { openWalletModal } = useContext(WalletModalContext);
    const [dropdownOpen, setDropdownOpen] = useState(false);
    const dropdownRef = useRef(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Search query:', query);
    };

    const getUserDisplayName = () => {
        if (!user) return "Guest";
        return user.name || user.did || "User";
    };

    const handleProfileClick = () => {
        if (!user) {
            openWalletModal();
        } else {
            setDropdownOpen((open) => !open);
        }
    };

    // Close dropdown on outside click
    useEffect(() => {
        function handleClickOutside(event) {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
                setDropdownOpen(false);
            }
        }
        if (dropdownOpen) {
            document.addEventListener('mousedown', handleClickOutside);
        } else {
            document.removeEventListener('mousedown', handleClickOutside);
        }
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, [dropdownOpen]);

    const handleLogout = () => {
        localStorage.removeItem('user');
        window.location.reload();
    };

    return (
        <div className='w-screen h-20 bg-white flex items-center justify-around border-2 border-gray-500'>
            <Link to="/" className='text-3xl font-bold cursor-pointer'>Commercio</Link>

            <div className='flex gap-15'>
                <Link to="/" className='cursor-pointer'>Home</Link>
                <Link to="/products" className='cursor-pointer'>Products</Link>
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
                <img src={Heart} className='h-8 cursor-pointer' />
                <img src={Cart} className='h-7 cursor-pointer' />
            </div>

            <div className='relative' ref={dropdownRef}>
                <div className='flex bg-white rounded-3xl pl-0.5 pr-2 items-center gap-3 cursor-pointer h-9.5 shadow-md border-1 border-gray-600' onClick={handleProfileClick}>
                    <div className='h-8 w-8 rounded-full bg-red-800 flex items-center justify-center'>
                        <img src={Avatar} className='h-full' />
                    </div>
                    <div className='text-gray-800 text-sm font-medium'>{getUserDisplayName()}</div>
                    <div><img src={DD} className='h-8' /></div>
                </div>
                {user && dropdownOpen && (
                    <div className='absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-lg shadow-lg z-50'>
                        <div className='px-4 py-2 hover:bg-gray-100 cursor-pointer' onClick={() => alert('Profile modal coming soon!')}>View Profile</div>
                        <div className='px-4 py-2 hover:bg-gray-100 cursor-pointer' onClick={() => alert('Orders coming soon!')}>Orders</div>
                        <div className='px-4 py-2 hover:bg-gray-100 cursor-pointer text-red-600' onClick={handleLogout}>Logout</div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Navbar;
