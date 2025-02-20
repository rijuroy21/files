// class Button{
//     constructor(){
//         this.btn=document.createElement('button')
//         this.btn.textContent="Click me"
//         document.body.appendChild(this.btn)
        
//     }
//     set width(width){
//         this.btn.style.width=width+'px'
//     }
//     set height(height){
//         this.btn.style.height=height+'px'
//     }
// }
// let btn1=new Button()
// btn1.width=100
// btn1.height=30

class Button {
    constructor() {
        this.btn = document.createElement('button');
        this.btn.textContent = "Click me"; 
        document.body.appendChild(this.btn);
    }
    set width(width) {
        this.btn.style.width = width + 'px'; 
    }
    get width() {
        return parseInt(this.btn.style.width);  
    }
}
let btn1 = new Button();
btn1.width = 200; 
console.log(btn1.width); 
