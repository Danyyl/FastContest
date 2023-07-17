import make_request from "../utils/requests"

const baseURL = "http://localhost:8000/"

export function getTasks() {
    return (dispatch) => {
        const callback_func = (response) => {
        const tasks = response.data
          console.log(tasks)
          dispatch(setTasks(tasks))
    }

    make_request(
    'get',
        "tasks/",
            null,
    {},
            callback_func
    )
    //     )
    //     axios({
    //     method: 'get',
    //     url: baseURL + "tasks/",
    //     withCredentials: true
    // })
    //   .then((response) => {
    //       const tasks = response.data
    //       console.log(tasks)
    //       dispatch(setTasks(tasks))
    //     // catch Errors
    //   });
    }
}


export const setTasks = (tasks) => (dispatch) => {
    console.log("Set Tasks");
    dispatch({
        type: "SET_TASKS",
        payload: tasks
    })
}

export function getTask(id, callback) {
    return (dispatch) => {
        const callback_function = (response) => {
         const task = response.data
          console.log(task)
          dispatch(setTask(task))
          callback(task)
        }

        make_request(
    'get',
        "tasks/" + id,
            null,
    {},
            callback_function
    )
    }
}

export const createUserTask = (id) => {
    return (dispatch) => {
        const callback_function = (response) => {
            console.log("UserTask created")
        }

         make_request(
    'post',
        "tasks/user_task",
             {"task_id": id},
    {},
            callback_function
    )
    }
}

export const setTask = (task) => (dispatch) => {
    console.log("Set Task");
    dispatch({
        type: "SET_TASK",
        payload: task
    })
}

export function getSolutions(id, callback) {
    return (dispatch) => {
        const callback_function = (response) => {
            const solutions = response.data
            console.log(solutions)
            dispatch(setSolutions(solutions))
            callback(solutions)
        }

        make_request(
            'get',
            "tasks/" + id + "/solutions",
            {},
            {},
            callback_function
        )
    }
}

const setSolutions = (solutions) => (dispatch) => {
    console.log("Set Solutions");
    dispatch({
        type: "SET_SOLUTIONS",
        payload: solutions
    })
}

export const createSolution = (id, code, callback) => {
    console.log("Send solution");
    return (dispatch) => {
        const callback_function = (response) => {
            dispatch(getSolutions(id, callback));
        }
       make_request(
            'post',
            "tasks/user_task/add_answer",
            {
                "task_id": id,
                "answer": code
            },
            {},
            callback_function
        )
    }
}
