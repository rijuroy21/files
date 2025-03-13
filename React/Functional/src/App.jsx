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


// import { useState,useEffect } from "react";
// function App(){
//   const [count,setCount] =useState(1)
//   const [name,setName] =useState('Manu')
//   useEffect(()=>{
//     console.log('rendered')
//   },[count])
//   return(
//     <>
//       <h1>{count}</h1>
//       <button onClick={()=>setCount(count+1)}>Incriment</button>
//       <h1>{name}</h1>
//       <button onClick={()=>setName('Riju')}>Change Name</button>
//     </>
//   )
// }

// export default App


// import { useState, useEffect } from "react"
// function App() {
//   const [count, setCount] = useState(0)
//   const [running, setRunning] = useState(false)
//   useEffect(() => {
//     if (!running) return
//     const interval = setInterval(() => {
//       setCount((prevCount) => prevCount + 1)
//     }, 1000);
//     return () => {
//       clearInterval(interval)
//       console.log("Cleanup: Interval cleared!!")
//     }
//   }, [running])
//   return (
//     <>
//       <h1>Timer: {count}</h1>
//       <button onClick={() => setRunning(true)}>Start</button>
//       <button onClick={() => setRunning(false)}>Stop</button>
//     </>
//   )
// }

// export default App



// import { useRef, useEffect } from "react"
// function App() {
//   const myRef=useRef(null)

//   useEffect(()=>{
//     console.log(myRef.current)
//   },[])

//   const handleSubmit=(event)=>{
//     event.preventDefault()
//     console.log(myRef.current.value)
//   }
//   return(
//     <>
//     <form onSubmit={handleSubmit}>
//       <input type="text" ref={myRef} placeholder="Focus me !!" />
//       <input type="submit" value="submit" />
//     </form>
//     </>
//   )
// }

// export default App




// import { useRef, useEffect } from "react"
// function App() {
//   const myRef=useRef(null)
//   useEffect(()=>{
//     console.log(myRef.current)
//   },[])

//   const handleSubmit=(event)=>{
//     console.log(myRef.current.value)
//   }
//   return(
//     <>
//       <input type="text" ref={myRef} placeholder="Focus me !!" onChange={handleSubmit} />

//     </>
//   )
// }

// export default App





// import React, { useContext } from "react";
// const MyContext = React.createContext();
// function App() {
//   const value = 'Hello from context'


//   return (
//     <MyContext.Provider value={value}>
//       <ChildComponent />

//     </MyContext.Provider>
//   )
// }
// function ChildComponent() {
//   const contextValue = useContext(MyContext)
//   return (
//   <>
//   {contextValue}
//   </>
//   )
// }
// export default App


// import React, { useContext, useState } from "react"
// const ThemeContext = React.createContext()
// function ThemeProvider({ children }) {
//   const [theme, setTheme] = useState("light")
//   const toggleTheme = () => {
//     setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"))
//   }

//   return (
//     <ThemeContext.Provider value={{ theme, toggleTheme }}>
//       {children}
//     </ThemeContext.Provider>
//   )
// }

// function ThemeButton() {
//   const { theme, toggleTheme } = useContext(ThemeContext);

//   return (
//     <button
//       onClick={toggleTheme}
//       style={{
//         backgroundColor: theme === "light" ? "#fff" : "#333",
//         color: theme === "light" ? "#000" : "#fff",
//       }}
//     >
//       {theme} mode
//     </button>
//   )
// }

// function App() {
//   return (
//     <ThemeProvider>
//       <ThemeButton />
//     </ThemeProvider>
//   );
// }

// export default App




// import {useMemo} from "react"
// import {useState} from "react"

// export default function App(){
//   const [count,setcount]=useState(0)
//   let sum=useMemo(()=>loop(),[])
//   return(<>
//   <p>{count}</p>
//   <button onClick={()=>setcount(count+1)}>+</button>
//   <p>sum is :{sum}</p>
//   </>)
// }

// function loop(){
//   let sum=0
//   for  (let i =0;i<=1e9;i++){
//     sum+=i
//   }
//   return sum
// }



import React, { useMemo, useState } from 'react';

function ExpensiveComponent({ items, filter }) {
    
    const filteredItems = useMemo(() => {
        console.log('Filtering items...'); 
        return items.filter(item => item.includes(filter));
    }, [items, filter]);

    return (
        <div>
            <h3>Filtered Items:</h3>
            <ul>
                {filteredItems.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}

function App() {
    const [filter, setFilter] = useState('');
    const items = ['apple', 'banana', 'cherry', 'date', 'elderberry'];

    return (
        <div>
            <input 
                type="text"
                value={filter}
                onChange={(e) => setFilter(e.target.value)}
                placeholder="Filter items"
            />
            <ExpensiveComponent items={items} filter={filter} />
        </div>
    );
}

export default App;
