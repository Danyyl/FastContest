import React, {useEffect, useState} from 'react'
import Title from "../UI/Title";
import TaskItem from "./TaskItem";


const UserTasks = (props) => {
    return (
     <div className='MainPage'>
         <div className='FilterBlock'>
             <Title text="My tasks" />
         </div>
         <div className='ListBlock'>

         </div>
     </div>
    );
}

export default UserTasks;