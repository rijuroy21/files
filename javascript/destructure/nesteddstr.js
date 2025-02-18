// let arr=[1,2,[10,20,30],3,4]
// const[first,,third,...rest]=arr
// console.log(...rest)

// let obj={
//     name:'Riju',
//     age:21,
//     place:'Kottayam',
// }
// const{name:userName,age:userAge,place:userPlace}=obj
// console.log(userAge)

// let obj={
//     name:'Riju',
//     age:21,
//     address:{
//         city:'Kottayam',
//         state:'Kerala',
//     }
   
// }
// const{name:userName,age:userAge,address:{city,state}}=obj
// console.log(address)

user={name:'manu',age:'22',place:'kochi'}
    function obj({name,age}){
        console.log(name,age)
    }
    obj(user)
    
