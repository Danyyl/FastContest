import axios from "axios";

const baseURL = "http://localhost:8000/"

export function login(username, password, navigate) {
    let bodyFormData = new FormData()
    bodyFormData.append("username", username)
    bodyFormData.append("password", password)
    console.log(bodyFormData.get("username"))
    axios({
        method: 'post',
        url: baseURL + "auth/jwt/login",
        data: bodyFormData,
        headers: { "Content-Type": "multipart/form-data" },
        withCredentials: true
    })
      .then((response) => {
          console.log(response.headers.get("Set-Cookie"))
          console.log(response.data)
        // catch Errors
      });
    return (dispatch) => {
        dispatch(getUser("/", navigate))
    }
}


export function getUser(url="", navigate=null) {
    return (dispatch) => {
        axios({
        method: 'get',
        url: baseURL + "auth/me/",
        withCredentials: true
    })
      .then((response) => {
          const user = response.data
          console.log(user)
          dispatch(setUser(user))
          if (url) {
              navigate(url);
          }
        // catch Errors
      });
    }
}


export const setUser = (user) => (dispatch) => {
    console.log("Set User");
    dispatch({
        type: "SET_USER",
        payload: user
    })
}