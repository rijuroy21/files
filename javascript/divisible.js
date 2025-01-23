a= parseInt(prompt('Enter a number '));
last_digit=a%10
if(last_digit%3==0){
    console.log(a,"divisible by 3")
}
else{
   console.log(a,"is not divisible by 3")
}