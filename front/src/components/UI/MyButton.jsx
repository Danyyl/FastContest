import React, {useEffect, useState} from 'react'
import "../../styles/UI/MyButton.css"
import Button from "@mui/material/Button";


const MyButton = (props) => {
    return (
        <Button {...props} variant="outlined">
            {props.value}
        </Button>
    );
}

export default MyButton;
