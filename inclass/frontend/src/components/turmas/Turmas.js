import React, { Component, Fragment }from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTurmas } from "../../actions/turmas";


export class Turmas extends Component{
    static propTypes = {
        turmas: PropTypes.array.isRequired
    };
    componentDidMount() {
        this.props.getTurmas();
    }
    render(){
        return(
            <Fragment>
               <h2>Turmas</h2>
               <table className="table table-striped">
                   <thead>
                       <tr>
                           <th>nome</th>
                           <th>tipo</th>
                           <th>id_sala</th>
                       </tr>
                   </thead>
                   <tbody>
                       {this.props.turmas.map(tbturma => (
                           <tr key = {tbturma.id}>
                               <td>{tbturma.curso}</td>
                               <td>{tbturma.cod_turma}</td>
                               <td>{tbturma.qtd_alunos}</td>
                               <td><button className="btn btn-danger btn-sm">
                                   Delete</button>
                                </td>
                           </tr>
                           
                       ))}
                   </tbody>
               </table>
            </Fragment>
        );
    }
}
const mapStateToProps = state => ({
    turmas: state.turmas.turmas
});

export default connect(mapStateToProps, { getTurmas })(Turmas);