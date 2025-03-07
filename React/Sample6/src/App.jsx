import React,{Component} from "react";

class App extends Component{
  constructor(){
    super()
    this.inputRef=React.createRef()
  }
  handleChange=(event)=>{
    event.preventDefault()
    alert('inputValue :'+this.inputRef.current.value)
  }
  render(){
    return(
      <>
      <form action="" onSubmit={this.handleChange}>
        <input type="text" ref={this.inputRef}/>
        <input type="submit" value="submit" />
      </form>

    
      </>
    )
  }
}

export default App