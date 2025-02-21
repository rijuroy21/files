// class Brand{
//     constructor(){
//         this.brand='honda'
//     }
// }
// class Bike extends Brand{
//     constructor (name,price){
//         super()
//         this.name=name
//         this.price=price
//         }
// } 
// let bike1=new Bike ('Goldwings','2000000')
// console.log(bike1.name, bike1.price);

class Brand{
    constructor(brand){
        this.brand=brand
    }
}
class Bike extends Brand{
    constructor (brand,name,price){
        super(brand)
        this.name=name
        this.price=price
        }
} 
let bike1=new Bike ('honda','Goldwings','2000000')
console.log(bike1.brand,bike1.name, bike1.price);