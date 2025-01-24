a = parseInt(prompt('Enter a number '));
if (a>100000) {
    tax=0.15*a;
    console.log(`${a}Rupees,tax=${tax}`);
}
else if (a>50000 && a<=100000) {
    tax=0.10*a;
    console.log(`${a}Rupees,tax=${tax}`);
}
else if (a<=50000) {
    tax=0.05*a;
    console.log(`${a}Rupees,tax=${tax}`);
}
else {
    console.log("Invalid input");
}