import React from "react";
import UserList from "./UserList";

class App extends React.Component {
  constructor (props){
    super(props);
    this.state={
      users:[]
    };
  }
  componentDidMount(){
    fetch("http://localhost:3000/users")
    .then((response)=> response.json())
    .then((data)=> this.setState({users:data}))
    .catch((error)=>console.error("Error fetching users:",error));
  }
  render(){
    console.log(this.state.users)
    return(
      <div>
        <h1>User List</h1>
        <UserList users={this.state.users}/>{}
      </div>
    );
  }
}

export default App;