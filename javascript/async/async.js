// async function fetchData(){
//     let responses=await fetch('https://dummyjson.com/posts')
//     let data=await responses.json()
//     console.log(data)
//     console.log('helo')
// }
// fetchData()

async function fetchData() {
    try {
        let response=await fetch('https://dummyjson.com/posts');
        
        if(!response.ok) { 
            throw new Error('Fetch unsuccessful')
        }

        let data=await response.json()
        console.log(data)
        data.posts.forEach(value => {
            let newdiv=document.createElement('div')
            newdiv.innerHTML=
            `<h3>${value.title}</h3>
            <p>${value.body}</p>
            <p>${value.tags}</p>
            <p>${value.userId}</p>`
        document.body.appendChild(newdiv)

            
        });

    } catch(error) {
        console.log('Error happened:', error.message)
    }
}
fetchData();
