const taskReducer = (state = {}, action) => {
    switch (action.type) {
        case 'SET_TASKS':
            console.log(action.payload)
            return {
                ...state,
                tasks: action.payload
            }
        case 'SET_TASK':
            console.log(action.payload)
            return {
                ...state,
                task: action.payload
            }
        case 'SET_SOLUTIONS':
            console.log(action.payload)
            return {
                ...state,
                solutions: action.payload
            }
        default:
            return state
    }
}

export default taskReducer