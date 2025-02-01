function getChar(str, index) {
    return index >= 0 && index < str.length ? str.charAt(index) : undefined;
}

let a = "Hello";
let b = getChar(a, 1);
console.log(b);

let c = getChar(a, 10);
console.log(c);
