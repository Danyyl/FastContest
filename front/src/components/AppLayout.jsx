import React, {useEffect, useState} from 'react'
import {Outlet} from "react-router";
import NavBar from "./NavBar";
import "../styles/Main.css"
import {Paper, Grid} from "@mui/material";



const Tasks = (props) => {

    return (
     // <Grid container className='AppLayout'>
     <Grid container className="AppLayout">
         <Grid item xs={2} alignContent="center">
            {/*<NavBar className='NavBar'/>*/}
                <NavBar/>
         </Grid>
         <Grid item xs={10} alignContent="center">
             {/*<Outlet className='Outlet'/>*/}
             <Outlet/>
         </Grid>
     </Grid>
     //    <Grid container spacing={4} justifyContent="center">
     //     <Grid item xs={6} border="double">
     //        Hello
     //     </Grid>
     //     <Grid item xs={6} border="double">
     //         World
     //     </Grid>
     // </Grid>
    );
}

export default Tasks;
