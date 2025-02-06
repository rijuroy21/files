const mybtn = document.getElementById('btn');
mybtn.addEventListener('click',()=>{
    setTimeout(()=>{
        mybtn.style.backgroundColor='red'
    },3000)
})
