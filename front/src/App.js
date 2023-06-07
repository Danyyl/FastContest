import React, {useEffect, useState} from 'react'
import { Routes, Route } from 'react-router-dom';
import PrivateRouter from "./components/PrivateRouter";
import './styles/App.css'
import LoginPage from "./components/LoginPage";
import Tasks from "./components/Task/Tasks";
import AppLayout from "./components/AppLayout";


function App() {

  return (
    <Routes>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/' element={<PrivateRouter/>}>
            <Route path='/' element={<AppLayout/>}>
                <Route path='/' element={<Tasks/>}/>
            </Route>
        </Route>
    </Routes>
  );
}

export default App;
