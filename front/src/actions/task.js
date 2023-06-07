import axios from "axios";

const baseURL = "http://localhost:8000/"

export function getTasks() {
    return (dispatch) => {
        axios({
        method: 'get',
        url: baseURL + "tasks/",
        withCredentials: true
    })
      .then((response) => {
          const tasks = response.data
          console.log(tasks)
          dispatch(setTasks(tasks))
        // catch Errors
      });
    }
}


export const setTasks = (tasks) => (dispatch) => {
    console.log("Set Tasks");
    dispatch({
        type: "SET_TASKS",
        payload: tasks
    })
}