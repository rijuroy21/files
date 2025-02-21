function greet(name, callback){
    console.log('helo'+name)
    callback()
}
function sayGoodmorning(){
    console.log('Good morning')
}
greet('Athul',sayGoodmorning)