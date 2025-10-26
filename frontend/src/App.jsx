import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

// Define the API URL. 
// This is your backend server's address.
const API_URL = 'http://127.0.0.1:8000/api/store/products'

function App() {
  // Create state to hold our products and loading status
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // useEffect runs once when the component mounts
  useEffect(() => {
    // Define an async function to fetch data
    const fetchProducts = async () => {
      try {
        // Make the GET request to our Django API
        const response = await axios.get(API_URL)

        // Save the data from the response into our state
        setProducts(response.data)
      } catch (err) {
        // Save any errors to state
        setError(err.message)
      } finally {
        // Set loading to false (request is finished)
        setLoading(false)
      }
    }

    // Call the function
    fetchProducts()
  }, []) // The empty array [] means this effect runs only once

  // --- Render the component ---
  if (loading) return <p>Loading products...</p>
  if (error) return <p>Error: {error}</p>

  return (
    <div>
      <h1>My E-Commerce Store</h1>
      <div className="product-list">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <h2>{product.name}</h2>
            <p>Price: ${product.price}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App