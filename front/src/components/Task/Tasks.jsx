import React, {useEffect, useState} from 'react'
import {useDispatch, useSelector} from "react-redux";
import TaskItem from "./TaskItem";
import {getTasks} from "../../actions/task"
import "../../styles/Tasks.css"


const Tasks = (props) => {

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTasks());
    }, [])
    const tasks = useSelector(({taskReducer}) => taskReducer.tasks)

    return (
     <div className='MainPage'>
         {tasks? tasks.map(task =>
            <TaskItem task={task}/>
         ) : ""}
     </div>
    );
}

export default Tasks;
