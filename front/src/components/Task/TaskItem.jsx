import React, {useState} from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import TagsList from "../Tag/TagsList";
import "../../styles/Task/TaskList.css"
import {useNavigate} from "react-router";

const TaskItem = (props) => {
    const navigate = useNavigate();

  return (
     <Card classes={"Card"} sx={{ minWidth: 275, background: "#c9ced6"}}>
      <CardContent>
        <Typography variant="h5"  gutterBottom>
          {props.task.name}
        </Typography>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" component="div">
          {props.task.text}
        </Typography>
        <Typography sx={{ mb: 0.5 }} color="text.secondary">
          {props.task.topic.name}
        </Typography>
        <TagsList tags={props.task.tags}/>
      </CardContent>
      <CardActions>
        <Button size="small" onClick={() => {navigate("/task/" + props.task.id)}}>Solve</Button>
      </CardActions>
    </Card>
  );
}

export default TaskItem;
