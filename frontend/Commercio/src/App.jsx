import React from 'react'
import Navbar from './Navbar'
import Mainhome from './Mainhome'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ProductsPage from './ProductsPage';

function App() {
  return (
    <div>
      <Router>
        <Navbar /> 
        <Routes>
          <Route path="/" element={<Mainhome />} />
          <Route path="/products" element={<ProductsPage />} />
        </Routes>
      </Router>
    </div>
  )
}

export default App
