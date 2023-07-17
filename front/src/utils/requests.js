import axios, { AxiosResponse, AxiosError } from "axios";

const baseURL = "http://localhost:8000/"

export default function make_request(method, url, data, headers, callback) {
    axios({
        method: method,
        url: baseURL + url,
        data: data,
        headers: headers,
        withCredentials: true
    })
      .then((response) => {
          callback(response);
        // catch Errors
      }).catch((reason) => {
          console.log(reason)
    if (reason.response.status === 401) {
        console.log("Wrong token!!!!!!!!")
    } else {
      // Handle else
    }
    console.log(reason.message)
  });
}