import React, {useEffect, useState} from 'react'
import Title from "../UI/Title";
import {useParams} from "react-router";
import {useDispatch} from "react-redux";
import {getTask, getSolutions, createUserTask, createSolution} from "../../actions/task";
import Grid from "@mui/material/Grid";
import MyButton from "../UI/MyButton";
import {Container, Paper, Typography} from "@mui/material";
import TagsList from "../Tag/TagsList";
import CodeField from "../UI/CodeField";
import "../../styles/Task/TaskPage.css";
import "../../styles/Main.css"
import Solution from "./Solution";


const Task = (props) => {
    const {id} = useParams()
    const [task, setTask] = useState({
        name: "",
        text: "",
        score: "",
        topic: {},
        tags: [],
        func_template: ""
    })
    const [solutions, SetSolutions] = useState([])

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(createUserTask(id))
        dispatch(getTask(id, setTask))
        dispatch(getSolutions(id, SetSolutions))
    }, [])

    useEffect(() => {
        setCode(task.func_template);
    }, [task])

    const [code, setCode] = useState(task.func_template)

    const OnSubmit = () => {
        dispatch(createSolution(id, code, SetSolutions));
    }

    return (
        <Container className="MainPage">
             <Grid container spacing={2}>
                 <Grid item xs={5}>
                     <Container className="DataColumn">
                         <Grid container direction="column" spacing={1} >
                             <Grid item xs={4}>
                                 <Container className="AboutBlock">
                                     <Grid container spacing={3}>
                                         <Grid item xs={9}>
                                             <Grid container xs={2} direction="column" spacing={0}>
                                                <Grid item xs={2} mb={-3}>
                                                    <Typography variant="h5" sx={{fontWeight: 'bold'}}>
                                                        {task.name}
                                                    </Typography>
                                                </Grid>
                                                <Grid item xs={2}>
                                                    <TagsList tags={task.tags}/>
                                                </Grid>
                                                <Grid item xs={2}>
                                                    <Typography variant="h6" gutterBottom>
                                                        {task.topic.name}
                                                    </Typography>
                                                 </Grid>
                                             </Grid>
                                        </Grid>
                                         <Grid item xs={2} alignSelf="right">
                                             <Typography variant="h5" color="#fefefe" sx={{fontWeight: 'bold'}} gutterBottom>
                                                        {task.score}
                                             </Typography>
                                         </Grid>
                                     </Grid>
                                 </Container>
                             </Grid>
                             <Grid item xs={8}>
                                 <div className="Description">
                                     <Typography variant="subtitle1">
                                         {task.text}
                                     </Typography>
                                 </div>
                                 {/*<Paper className="Description" sx={{background: "#c9ced6"}}>*/}
                                 {/*    {task.text}*/}
                                 {/*</Paper>*/}
                             </Grid>
                         </Grid>
                     </Container>
                 </Grid>
                 <Grid item xs={7}>
                     <Container className="SecondBlock">
                         <Grid container direction="column" spacing={1} justifyContent="space-around">
                             <Grid item xs={4} >
                                 <Paper className="Result" sx={{background: "#b6b9bf"}}>
                                     {solutions? solutions.map(solution =>
                                     <Solution solution={solution} key={solution.id}/>
                                     ): ""}
                                 </Paper>
                             </Grid>
                             <Grid item xs={6}>
                                 <Paper className="CodeBlock" sx={{background: "#c9ced6"}}>
                                    <CodeField value={code} onChange={(evn) => {setCode(evn.target.value)}}></CodeField>
                                 </Paper>
                             </Grid>
                             <Grid item xs={2}>
                                 <Container className="ButtonBlock">
                                     {/*<Grid container direction="row" border="double" justifyContent="center">*/}
                                     {/*    <Paper>*/}
                                            <MyButton className="ButtonBlock" value="Submit" onClick={OnSubmit}/>
                                         {/*</Paper>*/}
                                            {/*<Grid item xs={4}>*/}
                                            {/*    <Paper>*/}
                                            {/*        <MyButton value="Submit"/>*/}
                                            {/*    </Paper>*/}
                                            {/*</Grid>*/}
                                            {/*<Grid item xs={4}>*/}
                                            {/*    <Paper>*/}
                                            {/*        <MyButton/>*/}
                                            {/*    </Paper>*/}
                                            {/*</Grid>*/}
                                     {/*</Grid>*/}
                                 </Container>
                             </Grid>
                         </Grid>
                     </Container>
                 </Grid>
             </Grid>
    </Container>
    );
}

export default Task;