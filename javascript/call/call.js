// let obj={
//     name:'john',
//     greet:()=>{
//         console.log(this)
//     }
// }
// obj.greet()

// let obj={
//     name:'john'
//         }
// function greet()        
//    {
//         console.log(`helo${this.name}`)
//     }
// greet.call(obj)

let obj={
    name:'john'
        }
function greet(role)        
   {
        console.log(`helo ${this.name},you are ${role}`)
    }
greet.call(obj,'developer')

