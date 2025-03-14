import React from 'react'

const Child = ({increment}) => {
  return (
    <div>
      <h1>Child Component</h1>
      <button onClick={increment}>click</button>
    </div>
  )
}

export default Child
