import React, {Component} from 'react';

class NewItem extends Component{
    constructor(props){
        super(props);
        this.state = {
            inputContent:''
        }
    }

    oninputchange=(event)=>{
        this.setState({
            inputContent: event.target.value
        })
    }

    onButtonclick = () =>{
        this.props.addItem(this.state.inputContent);
        document.getElementById('newcontent').value='';
        this.setState({
            inputContent: ''
        })
    }

    render() {
        return(
            <div>
                <input id='newcontent' type='text' name='newaddtask' onChange={this.oninputchange} />
                <button onClick={this.onButtonclick}>Add item</button>
            </div>
        );
    }
}

export default NewItem;