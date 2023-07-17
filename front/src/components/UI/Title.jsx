import React, {useEffect, useState} from 'react'
import "../../styles/UI/Title.css"


const Title = (props) => {
    return (
        <div className='title'>
            <h1>
                {props.text}
            </h1>
        </div>
    );
}

export default Title;
