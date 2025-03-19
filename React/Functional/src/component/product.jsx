import { useLocation, useParams } from "react-router-dom";

function Product(){
    const {id}=useParams()
    return (
        <>
        <p>product id : {id} </p>
        </>
    )
}
export default Product