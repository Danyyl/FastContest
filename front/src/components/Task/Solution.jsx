import React, {useState} from 'react'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import "../../styles/Task/Solution.css"
import Text from "../UI/Text";


const Solution = (props) => {

  return (
     <Card className="Solution" sx={{background: "#c9ced6", marginLeft: "10%", marginBottom: "2%"}}>
      <CardContent>
        <Text value={props.solution.submitted_at}/>
        <Text value={props.solution.status}/>
        <Text value={props.solution.score}/>
      </CardContent>
    </Card>
  );
}

export default Solution;
