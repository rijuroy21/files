let stud1 = {
    name: 'alan',
    YOB: 2002,
    getAge: function () {
        return new Date().getFullYear() - this.YOB
    },
    getName: function () {
        return this.name
    }
}
console.log(stud1.getAge(), stud1.getName())   

let stud2 = {
    name: 'aby',
    YOB: 2004,
    getAge: function () {
        return new Date().getFullYear() - this.YOB
    },
    getName: function () {
        return this.name
    }
}
console.log(stud2.getAge(), stud2.getName())   