import React, { useState, useEffect } from 'react'

const Header = () => {
  return (
    <header>
      <h1>My Dashboard</h1>
    </header>
  )
}

const ItemList = ({ items }) => {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{item.name}</li>
      ))}
    </ul>
  )
}

function App() {
  const [count, setCount] = useState(0)
  const [items, setItems] = useState([
    { name: "Apple " },
    { name: "Banana" },
    { name: "Orange" }
  ])

  useEffect(() => {
    console.log("Component mounted")
  }, [])

  const addItem = () => {
    setItems([...items, { name: "New Item" }])
  }

  return (
    <div className="container">
      <Header />
      <h2>Counter Section</h2>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>

      <h2>Items</h2>
      <ItemList items={items} />

      <button onClick={addItem}>Add Item</button>

      <footer>
        <p>Footer content here</p>
      </footer>
    </div>
  )
}

export default App