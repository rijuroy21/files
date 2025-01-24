a= parseInt(prompt('Enter year of service '));
b= parseInt(prompt('Enter salary  '));
if (a>5){
    c=(a*0.05);
    console.log(`your bonus is ${c}`)
}
else{
    console.log(`not eligible ${b}`)
}