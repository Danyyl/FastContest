import axios from "axios";
import make_request from "../utils/requests"

const baseURL = "http://localhost:8000/"

export function login(username, password, navigate) {
    let bodyFormData = new FormData()
    bodyFormData.append("username", username)
    bodyFormData.append("password", password)
    // const callback = (response) => {
    //     console.log("Callback")
    // }
    // make_request(
    //     'post',
    //     "auth/jwt/login",
    //     bodyFormData,
    //     { "Content-Type": "multipart/form-data" },
    //     callback
    // )
    return (dispatch) => {
        const callback = (response) => {
        dispatch(getUser("/", navigate));
    }
    make_request(
        'post',
        "auth/jwt/login",
        bodyFormData,
        { "Content-Type": "multipart/form-data" },
        callback
    )
    }
}

export function register(username, password, name, navigate) {
    let bodyFormData = new FormData()
    bodyFormData.append("username", username)
    bodyFormData.append("password", password)
    bodyFormData.append("name", name)
    const req_data = {
        "email": username,
        "password": password,
        "name": name
    }
    // const callback = (response) => {
    //     console.log("Callback")
    // }
    // make_request(
    //     'post',
    //     "auth/jwt/login",
    //     bodyFormData,
    //     { "Content-Type": "multipart/form-data" },
    //     callback
    // )
    return (dispatch) => {
        const callback = (response) => {
        navigate("/login");
            // dispatch(login(username, password, navigate))
    }
    make_request(
        'post',
        "auth/register",
        req_data,
        // { "Content-Type": "multipart/form-data" },
        callback
    )
    }
}


export function getUser(url="", navigate=null) {
    return (dispatch) => {
        const callback = (response) => {
            const user = response.data
          console.log(user)
          dispatch(setUser(user))
          if (url) {
              navigate(url);
          }
        }
        make_request(
    'get',
        "auth/me",
            null,
    {},
            callback
        )
    //     axios({
    //     method: 'get',
    //     url: baseURL + "auth/me/",
    //     withCredentials: true
    // })
    //   .then((response) => {
    //       const user = response.data
    //       console.log(user)
    //       dispatch(setUser(user))
    //       if (url) {
    //           navigate(url);
    //       }
    //     // catch Errors
    //   });
    }
}


export const setUser = (user) => (dispatch) => {
    console.log("Set User");
    dispatch({
        type: "SET_USER",
        payload: user
    })
}