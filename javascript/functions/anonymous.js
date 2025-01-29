a = parseInt(prompt("Enter the first number: "));
b = parseInt(prompt("Enter the second number: "));
while (true) {
    uc = parseInt(prompt(`1. Addition
                          2. Subtraction
                          3. Multiplication
                          4. Division
                          5. Exit
                          Enter your choice:`));
    if (uc==1) {
        console.log("Result:"+add(a,b));
        break
    } 
    else if(uc==2) {
        console.log("Result:"+sub(a,b));
        break 
    } 
    else if(uc==3) {
        console.log("Result:"+mul(a,b));
        break
    } 
    else if(uc==4) {
        console.log("Result:"+div(a,b));
        break
    }
    else if(uc==5) {
        console.log("Exit");
        break
    } 
    else {
        console.log("invalid");
    }
}
let add=function(a,b){
    res=a+b
    return res
}

let sub=function(a,b){
    res=a-b
    return res
}

let mul=function(a,b){
    res=a*b
    return res
}

let div=function(a,b){
    res=a/b
    return res
}