import React from 'react'
import Home from './Home'
import About from './About'

function App() {
  let a;
  return (
    <div>
      hellow wourld
      <br />
      <Home num={a} obj={{ name: "taj", age: 20 }} />

      <About children={"hellow bhai"}>
        this is taj
        <p>this is taj</p>
      </About>
      <Card/>
    </div>
  )
}

export default App
