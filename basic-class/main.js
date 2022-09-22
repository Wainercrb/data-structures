// Simple JS class

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age 
    }

    get_person_data() {
        console.log(`Your name is ${this.name}, your age is ${this.age}`)
    }
}

person1 = new Person('John Junior Dos Santos', 30)
person2 = new Person('Rhoda Dest', 24)
person1.get_person_data()
person2.get_person_data()
