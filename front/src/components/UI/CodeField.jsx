import React, {useEffect, useState} from 'react'
import "../../styles/UI/CodeField.css"
import CodeEditor from '@uiw/react-textarea-code-editor';


const CodeField = (props) => {
    return (
        <CodeEditor
      language="python"
      placeholder="Please enter Python code."
      padding={15}
      style={{
        fontSize: 12,
        backgroundColor: "#fefefe",
        fontFamily: 'ui-monospace,SFMono-Regular,SF Mono,Consolas,Liberation Mono,Menlo,monospace',
      }}
      {...props}
    />
    );
}

export default CodeField;