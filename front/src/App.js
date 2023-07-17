import React, {useEffect, useState} from 'react'
import { Routes, Route } from 'react-router-dom';
import PrivateRouter from "./components/PrivateRouter";
import './styles/App.css'
import LoginPage from "./components/LoginPage";
import Tasks from "./components/Task/Tasks";
import AppLayout from "./components/AppLayout";
import Profile from "./components/Profile";
import Statistic from "./components/Stat/Statistic";
import UserTasks from "./components/Task/UserTasks";
import Task from "./components/Task/Task"
import Register from "./components/Register";


function App() {

  return (
    <Routes>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/' element={<PrivateRouter/>}>
            <Route path='/' element={<AppLayout/>}>
                <Route path='/' element={<Tasks/>}/>
                <Route path='/me' element={<Profile/>}/>
                <Route path='/stat' element={<Statistic/>}/>
                <Route path='/my-tasks' element={<UserTasks/>}/>
                <Route path='/task/:id' element={<Task/>}/>
            </Route>
        </Route>
    </Routes>
  );
}

export default App;
