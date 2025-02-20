class Student{
    constructor(name,YOB){
        this.name=name
        this.YOB=YOB
    }
    getAge(){
        return new Date().getFullYear()-this.YOB
    }
    getName(){
        return this.name
    }
}
let stud1=new Student('john',2002)
console.log(stud1.getAge(),stud1.getName())   