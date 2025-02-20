let obj={
    name:'john'
        }
function greet(role)        
   {
        console.log(`helo ${this.name},you are ${role}`)
    }
let bindFn = greet.bind(obj,'developer') 
bindFn()