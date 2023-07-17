import React, {useEffect} from "react";
import { Navigate, Outlet } from 'react-router-dom';
import {useDispatch, useSelector} from "react-redux";
import {getUser} from "../actions/auth";
import {useNavigate} from "react-router";

const PrivateRouter = (props) => {
    const {...rest} = props;
    const dispatch = useDispatch()
    useEffect(() => {dispatch(getUser())}, [])
    const isLoggedIn = useSelector(({authReducer}) => authReducer.user)
    return isLoggedIn ? <Outlet/>  : <Navigate to="/login"/>
}
export default PrivateRouter