// let regex=/[cr]at/
// console.log(regex.test('cat'))
// console.log(regex.test('rat'))

// let regex=/[a-z 0-9]/
// console.log(regex.test('rat'))
// console.log(regex.test('DKJGF'))

// let regex=/^cat/
// console.log(regex.test('i love cat'))
// console.log(regex.test('cat is an animal'))

// let regex=/^cat/im
// console.log(regex.test('cat is an animal \n i love cat'))

// let regex=/meats?$/im
// console.log(regex.test('meat'))
// console.log(regex.test('meats'))

// let regex=/fish.*$/i
// console.log(regex.test('fish'))
// console.log(regex.test('fishes'))

// let regex=/[^hello]/
// console.log(regex.test('hello'))
// console.log(regex.test('hello how are you'))


// let regex=/l{2}o/
// console.log(regex.test('hello'))
// console.log(regex.test('helo'))
// console.log(regex.test('helllllo'))

// let regex = /l{2,4}o$/
// console.log(regex.test('hello'))
// console.log(regex.test('helo'))
// console.log(regex.test('hellllllo'))


let regex = /\d3/
console.log(regex.test('abc123'))
console.log(regex.test('456'))
console.log(regex.test('1234'))


