import axios from 'axios';
import { GET_TURMAS } from './types';

//GET

export const getTurmas = () => dispatch => {
    axios.get('/api/turma/')
        .then(res => {
            dispatch({
                type: GET_TURMAS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
}

