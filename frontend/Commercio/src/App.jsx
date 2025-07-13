import React, { useState, useEffect, createContext } from 'react'
import { Routes, Route } from 'react-router-dom'
import Navbar from './Navbar'
import Home from './Home'
import Brandscroll from './Brandscroll'
import WalletOnboarding from './WalletOnboarding'
import FloatingChatbox from './FloatingChatBox'
import ProductsPage from './ProductsPage'

export const WalletModalContext = createContext();

function App() {
  const [user, setUser] = useState(null);
  const [walletModalOpen, setWalletModalOpen] = useState(false);

  // Load user from localStorage on app start
  useEffect(() => {
    const stored = localStorage.getItem('user');
    if (stored) {
      try {
        setUser(JSON.parse(stored));
      } catch (e) {
        console.error('Failed to parse stored user:', e);
        localStorage.removeItem('user');
      }
    }
  }, []);

  // Save user to localStorage when it changes
  useEffect(() => {
    if (user) {
      localStorage.setItem('user', JSON.stringify(user));
    } else {
      localStorage.removeItem('user');
    }
  }, [user]);

  const handleUserOnboarded = (userObj) => {
    setUser(userObj);
    setWalletModalOpen(false);
  };

  const openWalletModal = () => setWalletModalOpen(true);
  const closeWalletModal = () => setWalletModalOpen(false);

  return (
    <WalletModalContext.Provider value={{ user, openWalletModal }}>
      <Navbar user={user} />
      <WalletOnboarding open={walletModalOpen} onClose={closeWalletModal} onUserOnboarded={handleUserOnboarded} />
      <Routes>
        <Route path="/" element={
          <>
            <Home />
            <Brandscroll />
          </>
        } />
        <Route path="/products" element={<ProductsPage />} />
      </Routes>
      <FloatingChatbox user={user} />
    </WalletModalContext.Provider>
  )
}

export default App
