import React, {useEffect, useState} from 'react'
import "../../styles/UI/CheckTag.css"
import Chip from "@mui/material/Chip";
import Stack from "@mui/material/Stack";

// tags={tags} setChecked={setCheckedTags}
const CheckTags = (props) => {
    const HandleCheck = (e) => {
        if (e.target.checked) {
            props.setChecked([...props.checked, e.target.value])
        }
        else {
            props.setChecked(props.checked.filter(item => item !== e.target.value))
        }

    }

    return (
        <Stack height="5vh" direction="row" spacing={4} marginLeft="8%">
      {props.tags.map(tag =>
          <label className="container">
              <input type="checkbox" value={tag.tag.id} onChange={HandleCheck}/>
              <span key={tag.tag.id} className="checkmark">{tag.tag.name}</span>
          </label>
      )}
        </Stack>
    );
}

export default CheckTags;
