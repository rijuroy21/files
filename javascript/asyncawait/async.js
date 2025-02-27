// async function fetchData(){
//     let responses=await fetch('https://dummyjson.com/posts')
//     let data=await responses.json()
//     console.log(data)
//     console.log('helo')
// }
// fetchData()



// async function fetchData() {
//     try {
//         let response=await fetch('https://dummyjson.com/posts');
        
//         if(!response.ok) { 
//             throw new Error('Fetch unsuccessful')
//         }

//         let data=await response.json()
//         console.log(data)
//         data.posts.forEach(value => {
//             let newdiv=document.createElement('div')
//             newdiv.innerHTML=
//             `<h3>${value.title}</h3>
//             <p>${value.body}</p>
//             <p>${value.tags}</p>
//             <p>${value.userId}</p>`
//         document.body.appendChild(newdiv)

            
//         });

//     } catch(error) {
//         console.log('Error happened:', error.message)
//     }
// }
// fetchData();




async function fetchData(){
    try{
        let responses = await fetch('https://dummyjson.com/products')
        if (!responses.ok){
            throw new Error('fetch unsuccessful')
        }
        let data = await responses.json()
        console.log(data)
        data.products.forEach(value=>{
            let newdiv = document.createElement('div')
            newdiv.className='product col-lg-2'
            newdiv.innerHTML= 
                `<h3>${value.title}</h3>
                <p>${value.description}</p>
                <p>Price: ${value.price}</p>
                <img src=${value.thumbnail}>`
            document.body.appendChild(newdiv)
        })
    }
    catch(error){
        console.log("Error happened:", error.message)
    }
}

fetchData()





// fetch('https://dummyjson.com/products')
//             .then(res => res.json())
//             .then(data => {
//                 const productsContainer = document.getElementById('products');
//                 data.products.forEach(product => {
//                     // console.log(product.category);
//                     const productElement = document.createElement('div');
//                     productElement.className = 'product col-lg-2';

//                     productElement.innerHTML = `
//                          <img src="${product.thumbnail}" alt="${product.title}">
//                         <h2>${product.title}</h2>
//                         <p>Price: $${product.price}</p>
//                         <button class='btn btn-dark'>
//                             <a href="../JavaScript/API_javascript_page2.html?id=${product.id}">View Product</a>
//                             </button>
//                     `;

//                     productsContainer.appendChild(productElement);

                    
//                 });
//             })
//             .catch(error => console.error('Error fetching products:', error));