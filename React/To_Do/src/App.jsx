import { Component } from "react"
class App extends Component{
  constructor(){
    super()
    this.state={
      tasks:[],
      task:"",
    }
  }
  handleInputChange=(event)=>{
    this.setState({task:event.target.value})
  }
  addTask=()=>{
    if (this.state.task.trim()!==""){
      this.setState((prevState)=>({
        tasks:[...prevState.tasks,prevState.task],
        task:"",
      }))
    }
  }

  render(){
    return(
      <>
        <h1>To-Do List</h1>
        <div>
          <input type="text" value={this.state.task} onChange={this.handleInputChange} placeholder="Add a new task"/>
          <button onClick={this.addTask}>Add</button>
        </div>
        <ul>
          {this.state.tasks.map((t,index)=>(
            <li key={index}>{t}</li>
          ))}
        </ul>
      </>
    )
  }
}

export default App
