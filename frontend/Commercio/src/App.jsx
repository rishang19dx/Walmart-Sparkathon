import React from 'react'
import Navbar from './Navbar'
import Mainhome from './Mainhome'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Productcard from './Productcard';
import Tshirt from './assets/t-shirt.jpg';

function App() {
  return (
    <div>
      <Router>
        <Navbar /> 
        <Routes>
          <Route path="/" element={<Mainhome />} />
          <Route path="/products" element={<Productcard link={Tshirt} />} />
        </Routes>
      </Router>
    </div>
  )
}

export default App
