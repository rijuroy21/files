a= parseInt(prompt('Enter a number '));
if(a<=100)
    console.log(`No charge`)
else if (a<=200){
    b=5*(a-100)
    console.log(`${b}`)
}
else if (a>200){
    b=a-200
    result=(b*10)+500
    console.log(`${result}`)
}
else{
    console.log("invalid") 
}
       