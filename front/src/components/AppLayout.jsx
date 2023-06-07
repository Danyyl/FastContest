import React, {useEffect, useState} from 'react'
import {Outlet} from "react-router";
import NavBar from "./NavBar";
import "../styles/Main.css"



const Tasks = (props) => {

    return (
     <div className='AppLayout'>
         <NavBar className='NavBar'/>
         <Outlet className='Outlet'/>
     </div>
    );
}

export default Tasks;
