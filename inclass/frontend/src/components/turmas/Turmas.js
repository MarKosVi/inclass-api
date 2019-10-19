import React, { Component }from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getTurmas} from '../../actions/turmas';


export class Turmas extends Component{
    static propTypes = {
        turmas: PropTypes.array.isRequired
    }

    render(){
        return(
            <div>
                <h1>Turmas List</h1>
            </div>
        )
    }
}
const mapStateToProps = state => ({
    turmas: state.turmas.turmas
})

export default connect(mapStateToProps)(Turmas);