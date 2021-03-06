import axios from 'axios';
import {
    GET_TURMAS,
    DELETE_TURMA,
    ADD_TURMA
} from './types';



//GET

export const getTurmas = () => dispatch => {
    axios.get('/api/disciplina/')
        .then(res => {
            dispatch({
                type: GET_TURMAS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));

}


//Delete

export const deleteTurma = (id) => dispatch => {
    axios
        .delete('/api/disciplina/' + id + '/')
        .then(res => {
            dispatch({
                type: DELETE_TURMA,
                payload: id
            });
        })
        .catch(err => console.log(err));

}

//POST
export const addTurma = turma => dispatch => {
    axios
        .post('/api/disciplina/', turma)
        .then(res => {
            dispatch({
                type: ADD_TURMA,
                payload: res.data
            });
        })
        .catch(err => console.log(err));

}