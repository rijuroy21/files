a=prompt("enter your name")
let mybtn=document.getElementById('btn')
mybtn.addEventListener('click',()=>{
    console.log('button clicked')
    console.log(a)
})