import React, {useEffect, useState} from 'react'
import {useParams} from "react-router";
import {useDispatch} from "react-redux";
import {getTask, getSolutions, createUserTask, createSolution} from "../actions/task";
import Grid from "@mui/material/Grid";
import {Container, Paper, Typography} from "@mui/material";
import "../styles/Main.css"



const Profile = (props) => {


    return (
        <Container className="MainPage">

        </Container>
    );
}

export default Profile;