import React, { Component }from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addTurma } from '../../actions/turmas';



export class Form extends Component{
    state = {
        nome: "",
        tipo_sala: "",
        id_escola: ""
    };

    static propTypes = {
        addTurma: PropTypes.func.isRequired
    };

    onChange = e => this.setState({ [e.target.name]: 
        e.target.value });
    onSubmit = e => {
        e.preventDefault();
        const { nome, tipo_sala, id_escola} = this.state;
        const turma = { nome, tipo_sala, id_escola};
        this.props.addTurma(turma);
    };
    render(){
        const {nome, tipo_sala, id_escola} = this.state;
        return(
         <div className="card card-body mt-4 mb-4">
             <h2>Add</h2>
             <form onSubmit={this.onSubmit}>
                 <div className="form-group">
                     <label>Nome</label>
                     <input
                        className="form-control"
                        type="text"
                        name="nome"
                        onChange={this.onChange}
                        value={nome} />
                
                     <label>Tipo de sala</label>
                     <input
                        className="form-control"
                        type="text"
                        name="tipo_sala"
                        onChange={this.onChange}
                        value={tipo_sala} />

                     <label>ID de Escola</label>
                     <input
                        className="form-control"
                        type="text"
                        name="id_escola"
                        onChange={this.onChange}
                        value={id_escola} />                    
                 </div>

                 <div className="form-group">
                     <button className="btn btn-primary">
                         submit
                     </button>

                 </div>
             </form>
         </div>   
        )
    }
}

export default connect(null,{addTurma})(Form);