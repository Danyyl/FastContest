
const taskReducer = (state = {}, action) => {
 switch (action.type) {
  case 'SET_TASKS':
      console.log(action.payload)
    return {
     ...state,
     tasks: action.payload
    }
  default:
   return state
 }
}

export default taskReducer