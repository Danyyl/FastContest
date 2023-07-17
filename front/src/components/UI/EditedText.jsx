import React, {useEffect, useState} from 'react'
import "../../styles/UI/EditedText.css"
import TextField from "@mui/material/TextField";


const EditedText = (props) => {
    return (
        <TextField
              margin="normal"
              // required
              fullWidth
              {...props}
              // name="password"
              // label="Password"
              // type="password"
              // id="password"
              // autoComplete="current-password"
              // value={credentials.password}
              // onChange={handleChanges}
            />
    );
}

export default EditedText;
