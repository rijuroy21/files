function padString(str, length, char) {
    let totalPadding = length - str.length;
    if (totalPadding <= 0) return str;

    let leftPadding = Math.floor(totalPadding / 2);
    let rightPadding = totalPadding - leftPadding;

    return char.repeat(leftPadding) + str + char.repeat(rightPadding);
}


let a = "Hello";
let b = padString(a, 10, "*"); 
console.log(b);
