import React, {useEffect, useState} from 'react'
import {useDispatch, useSelector} from "react-redux";
import TaskItem from "./TaskItem";
import {getTasks} from "../../actions/task"
import "../../styles/Tasks.css"
import "../../styles/Main.css"
import Title from "../UI/Title";
import {FormControl, FormHelperText, Grid, InputLabel, MenuItem, Select} from "@mui/material";
import CheckTags from "../UI/CheckTags";


const Tasks = (props) => {

    const dispatch = useDispatch();

    const [tags, setTags] = useState([])

    const [topics, setTopics] = useState([])

    const [topic, setTopic] = useState(0)

    const [checkedTags, setCheckedTags] = useState([])

    useEffect(() => {
        console.log(checkedTags)
    }, [checkedTags])

    useEffect(() => {
        dispatch(getTasks());
    }, [])
    const tasks = useSelector(({taskReducer}) => taskReducer.tasks)

    const isTopicInArray = (topic_t, topics_t) => {
        let checker = false
        topics_t.forEach(top => {
            if (top.id === topic_t.id){
                checker = true
            }
        })
        return checker
    }

    useEffect(() => {
        let tags_ = []
        if (tasks !== undefined) {
            tasks.forEach(task => {
                if (task.tags? task.tags.length: 0 > 0){
                    task.tags.forEach(tag => tags_.push(tag))
                }
            })
        }
        setTags(tags_)

        let topics_ = []
        if (tasks !== undefined) {
            tasks.forEach(task => {
                if (task.topic !== null && isTopicInArray(task.topic, topics_) === false){
                    topics_.push(task.topic)
                }
            })
        }
        setTopics(topics_)
    }, [tasks])

    return (
     <div className='MainPage'>
         <div className='FilterBlock'>
             <Grid container spacing={2}>
                 <Grid item xs={7}>
                    <CheckTags tags={tags} setChecked={setCheckedTags} checked={checkedTags}/>
                 </Grid>
                 <Grid item xs={5} alignSelf="right">
                    <FormControl sx={{ m: 1, minWidth: 120 }}>
                        <InputLabel id="demo-simple-select-helper-label">Topic</InputLabel>
                        <Select
                          labelId="demo-simple-select-helper-label"
                          id="demo-simple-select-helper"
                          value={topic}
                          label="Topic"
                          onChange={(e) => {setTopic(e.target.value)}}
                        >
                            {topics? topics.map(top =>
                            <MenuItem value={top.id} key={top.id}>{top.name}</MenuItem>
                                ): ""}
                          <MenuItem value="">
                            <em>None</em>
                          </MenuItem>
                          <MenuItem value={10}>Ten</MenuItem>
                          <MenuItem value={20}>Twenty</MenuItem>
                          <MenuItem value={30}>Thirty</MenuItem>
                        </Select>
                        <FormHelperText>Choose topic that you need</FormHelperText>
                  </FormControl>
                 </Grid>
             </Grid>
         </div>
         {/*<div className='ListBlock'>*/}
         {/*    {tasks? tasks.map(task =>*/}
         {/*   <TaskItem task={task} key={task.id}/>*/}
         {/*) : ""}*/}
         {/*</div>*/}
         <Grid container spacing={4} justifyContent="center">
             {tasks ? tasks.map(task =>
                 <Grid item xs={5}>
                    <TaskItem task={task} key={task.id}/>
                 </Grid>
             ) : ""}
         </Grid>
     </div>
    );
}

export default Tasks;
