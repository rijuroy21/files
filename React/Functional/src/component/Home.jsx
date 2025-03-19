import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
function Home() {
    const navigate = useNavigate()
    const prodnavigate = useNavigate()
    const getproduct = (id) => {
        prodnavigate(`/product/${id}`)
    }
    return (
        <>
            <h1>Home pages</h1>
            <button onClick={ ()=>getproduct(103)} > Products</button >
        </>
    )
}
export default Home