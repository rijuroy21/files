import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"

function Home() {
    const prodnavigate = useNavigate()
    const getproduct = (id) => {
        prodNavigate(`/product/${id}`)
    }

    const [products, setProducts] = useState([])

    useEffect(() => {
        fetch('https://dummyjson.com/products')
            .then(response => response.json())
            .then(json => {
                console.log(json);
                setProducts(json);
            })
    }, [])

    return (
        <>
            <h1>Home page</h1>
            <ul>
                {posts.map((product, index) => (
                    <ul key={product.id}>
                        <li>{index + 1}. {product.title}
                            <button onClick={() => getproduct(product.id)}>Get id</button></li>
                    </ul>
                ))}
            </ul>
        </>
    );
}

export default Home;
