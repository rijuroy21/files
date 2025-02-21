try {
    let x=y+10
    console.log(x)
} catch (error) {
    console.log('An error occurred:', error.message)
}
finally{
    console.log('execution complete')
}