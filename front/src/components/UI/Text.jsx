import React, {useEffect, useState} from 'react'
import "../../styles/UI/Text.css"
import Typography from "@mui/material/Typography";


const Text = (props) => {
    return (
         <Typography {...props}>
          {props.value}
        </Typography>
    );
}

export default Text;
