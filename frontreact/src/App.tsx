import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import MyButton from './button/button';
import UsersPage from './users/page';

function App() {
  return (
  <BrowserRouter>
      <Routes>
        <Route path="/" element={<MyButton/>}></Route>
        <Route path="/users" element={<UsersPage/>}></Route>
      </Routes>
  </BrowserRouter>
  );
}

export default App;
