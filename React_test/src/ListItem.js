import React, {Component} from 'react';
import './ListItem.css';

class ListItem extends Component{
    constructor(props){
        super(props)
    }

    onliclick = () =>{
        console.log(this.props.item.content)
        this.props.changeItem(this.props.item.content);
    }

    render(){
        if(this.props.item.done){
            return(
                <li className='done-item' onClick={this.onliclick} title="点击改变状态">{this.props.item.content} (已完成)</li>
            );
        }else{
            return(
                <li className='not-done' onClick={this.onliclick} title="点击将标记当前task已完成">{this.props.item.content}</li>
            );
        }
    }
}

export default ListItem;