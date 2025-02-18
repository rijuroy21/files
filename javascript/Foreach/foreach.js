// let arr=[1,2,3,4,5]
// arr.forEach((value,index,array)=>{
//     console.log(`${index}:${value}`)
//     console.log(array)
// })

// let arr=[1,2,3,4,5]
// arr.forEach((value,index,array)=>{
//     console.log(`${index}:${value}`)
//     console.log(array)
// })

let arr=[1,2,3,4,5]
arr.forEach((value,index,array)=>{
    array[index]=value*value
})