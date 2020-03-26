import React, {Component} from 'react';
import ListItem from './ListItem.js';
import NewItem from './NewItem.js';

class TodoList extends Component{
    constructor(props){
        super(props);
        this.state = {
            todolist:[{content:'Read books', done:true}, {content:'Take lessons', done:false}]
        }
    }

    addItem = (newItem) =>{
        const newlist = [...this.state.todolist, {content:newItem, done:false}]
        this.setState({
            todolist:newlist
        })
    }

    changeItem = (needtochangeitem) =>{
        var newlist = [...this.state.todolist];
        for (var item of newlist){
            if(item.content==needtochangeitem){
                item.done = true;
                break;
            }
        }
        this.setState({
            todolist:newlist
        })
    }

    render(){
        return(
            <div>
            <ul>
                {this.state.todolist.map(item=>(<ListItem item={item} changeItem={this.changeItem} />))}
            </ul>
            <NewItem addItem={this.addItem}/>
            </div>
        );
    }
}

export default TodoList
