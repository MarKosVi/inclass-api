import { GET_TURMAS } from "../actions/types.js";

const initialState = {
    turmas: []
};

export default function(state = initialState, action){
    switch(action.type){
        case GET_TURMAS:
            return{
                ...state,
                turmas: action.payload
            };
        default:
            return state; 

    }
}