import React, { Component, Fragment }from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTurmas, deleteTurma } from "../../actions/turmas";


export class Turmas extends Component{
    static propTypes = {
        turmas: PropTypes.array.isRequired,
        getTurmas:PropTypes.func.isRequired,
        deleteTurma: PropTypes.func.isRequired
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
                       {this.props.turmas.map(tbdisciplina => (
                           <tr key = {tbdisciplina.id}>
                               <td>{tbdisciplina.nome}</td>
                               <td>{tbdisciplina.tipo_sala}</td>
                               <td>{tbdisciplina.id_escola}</td>
                               <td>
                                   <button onClick={this.props.deleteTurma.bind(this, tbdisciplina.id)} 
                                   className="btn btn-danger btn-sm">{" "}
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

export default connect(mapStateToProps, { getTurmas, deleteTurma })(Turmas);