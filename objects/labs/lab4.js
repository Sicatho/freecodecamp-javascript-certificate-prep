// Lab 4: Object Methods
const dog = {
    name: "Buddy",
    bark: function() { return `${this.name} says Woof!`; }
};
console.log(dog.bark());