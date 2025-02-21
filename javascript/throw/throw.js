function canVote(age) {
    if (age < 18) {
        throw new Error('ineligible')
    }
    return 'eligible'
}
try {
    console.log(canVote(15))
} catch (error) {
    console.log(error.message)
}
