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
function add(a,b) 
{
    return a+b
}
function sub(a,b) 
{
    return a-b
}
function mul(a,b)
 {
    return a*b
}
function div(a,b) 
{
    return a/b
}
