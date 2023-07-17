import React, {useState} from 'react'
import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';

const TagsList = (props) => {
  return (
  <Stack height="5vh" direction="row" spacing={1}>
      {props.tags.map(tag =>
        <Chip label={tag.tag.name} key={tag.tag.id} color="primary" />
      )}
  </Stack>

  );
}

export default TagsList;