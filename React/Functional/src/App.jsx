// function App(){
//   return(
//     <>
//     <h1>Helo Riju</h1>
//     </>
//   )
// }
// export default App
  


// const App=()=>(
//   <>
//     <h1>Hello Riju</h1>
//   </>
// )
// export default App



// import{ useState } from "react";

// function App(){
//   const[name,setName]=useState('Manu')
//   return(
//     <>
//     <h1>{name}</h1>
//     <button onClick={()=>setName('Riju')}>Change Name</button>
//     </>
//   )
// }
// export default App

// import { useState } from "react";
// function App(){
//   const [count,setCount] =useState(1)
//   const handleChange=()=>{
//     setCount(count+1)
//   }
//   return(
//     <>
//       <h1>{count}</h1>
//       <button onClick={handleChange}>Incriment</button>
//     </>
//   )
// }

// export default App



// import { useState,useEffect } from "react";
// function App(){
//   const [count,setCount] =useState(null)
//   // const handleChange=()=>{
//   //   setCount(count+1)
//   useEffect(()=>{
//     console.log('rendered')
//   },[])
//   return(
//     <>
//       <h1>{count}</h1>
//       <button onClick={()=>setCount(count+1)}>Incriment</button>
//     </>
//   )
// }

// export default App


import { useState,useEffect } from "react";
function App(){
  const [count,setCount] =useState(1)
  const [name,setName] =useState('Manu')
  useEffect(()=>{
    console.log('rendered')
  },[count])
  return(
    <>
      <h1>{count}</h1>
      <button onClick={()=>setCount(count+1)}>Incriment</button>
      <h1>{name}</h1>
      <button onClick={()=>setName('Riju')}>Change Name</button>
    </>
  )
}

export default App
