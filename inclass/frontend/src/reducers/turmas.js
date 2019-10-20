import { GET_TURMAS, DELETE_TURMA } from "../actions/types.js";
import { Turmas } from "../components/turmas/Turmas.js";

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

            
        case DELETE_TURMA:
            return{
                ...state,
                turmas: state.turmas.filter(Turmas => Turmas.id !==
                    action.payload)
            };
        default:
            return state; 

    }
}