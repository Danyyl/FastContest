import React, {useState} from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import TagsList from "../Tag/TagsList";

const TaskItem = (props) => {
  return (
     <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          {props.task.name}
        </Typography>
        <Typography variant="h5" component="div">
          {props.task.text}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {props.task.topic.name}
        </Typography>
        <TagsList tags={props.task.tags}/>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}

export default TaskItem;
