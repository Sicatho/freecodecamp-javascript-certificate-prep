import os

# Complete map of paths and the runnable JS code they should contain
repo_structure = {
    # ---------------- variables-and-strings ----------------
    "variables-and-strings/labs/lab1.js": """// Lab 1: Variable Declaration
const curriculum = "FreeCodeCamp JavaScript";
let status = "In Progress";
console.log("Curriculum:", curriculum, "| Status:", status);""",

    "variables-and-strings/labs/lab2.js": """// Lab 2: String Concatenation
let firstName = "Camper";
let greeting = "Hello, " + firstName + "! Welcome to coding.";
console.log(greeting);""",

    "variables-and-strings/labs/lab3.js": """// Lab 3: Template Literals
const user = "Alex";
const challenge = "Variables & Strings";
console.log(`User ${user} successfully initialized challenge: ${challenge}.`);""",

    "variables-and-strings/labs/lab4.js": """// Lab 4: String Methods
let message = "javascript prep";
console.log("Length:", message.length);
console.log("Uppercase:", message.toUpperCase());""",

    "variables-and-strings/labs/lab5.js": """// Lab 5: Type Coercion
let numericString = "100";
let conversion = Number(numericString) + 50;
console.log("Converted total (expected 150):", conversion);""",

    "variables-and-strings/workshops/workshop1.js": """// Workshop 1: Profile Generator
function createProfile(name, role, city) {
    return `Profile Info: ${name} works as a ${role} based out of ${city}.`;
}
console.log(createProfile("Sam", "Developer", "Austin"));""",

    "variables-and-strings/workshops/workshop2.js": """// Workshop 2: Mad Libs Game
function playMadLibs(noun, verb, adjective) {
    return `The ${adjective} ${noun} decided to ${verb} across the floor.`;
}
console.log(playMadLibs("cat", "scamper", "speedy"));""",

    "variables-and-strings/workshops/workshop3.js": """// Workshop 3: URL Builder
function buildUrl(host, route) {
    return "https://" + host + "/" + route;
}
console.log(buildUrl("freecodecamp.org", "learn"));""",

    "variables-and-strings/workshops/workshop4.js": """// Workshop 4: Receipt Formatter
function formatReceiptItem(item, price) {
    return `${item.padEnd(15, ".")} $${price.toFixed(2)}`;
}
console.log(formatReceiptItem("Coffee", 3.5));""",

    "variables-and-strings/workshops/workshop5.js": """// Workshop 5: Tag Generator
function generateHtmlTag(tag, text) {
    return `<${tag}>${text}</${tag}>`;
}
console.log(generateHtmlTag("h1", "JavaScript Certification"));""",


    # ---------------- boolean-and-numbers ----------------
    "boolean-and-numbers/labs/lab1.js": """// Lab 1: Arithmetic Operators
let total = 25 + 5;
let remainder = 10 % 3;
console.log("Sum:", total, "| Modulus Remainder:", remainder);""",

    "boolean-and-numbers/labs/lab2.js": """// Lab 2: Truthy vs Falsy
let testValue = "Hello"; 
console.log("Is truthy:", Boolean(testValue));""",

    "boolean-and-numbers/labs/lab3.js": """// Lab 3: Comparison Operators
console.log("Strict (5 === '5'):", 5 === '5');
console.log("Loose (5 == '5'):", 5 == '5');""",

    "boolean-and-numbers/labs/lab4.js": """// Lab 4: Logical Operators
let hasPremium = true;
let isEnrolled = false;
console.log("Can access course:", hasPremium || isEnrolled);""",

    "boolean-and-numbers/labs/lab5.js": """// Lab 5: The Math Object
let randomNum = Math.floor(Math.random() * 10) + 1;
print("Random Number (1-10):", randomNum);
console.log("Random Number (1-10):", randomNum);""",

    "boolean-and-numbers/workshops/workshop1.js": """// Workshop 1: Age Gate
function verifyAge(age) {
    if (age >= 18) {
        return "Access Granted.";
    }
    return "Access Denied: Under 18.";
}
console.log(verifyAge(20));""",

    "boolean-and-numbers/workshops/workshop2.js": """// Workshop 2: Tip Calculator
function calculateBill(subtotal, tipPercent) {
    let tip = subtotal * (tipPercent / 100);
    return subtotal + tip;
}
console.log("Total due:", calculateBill(50, 15));""",

    "boolean-and-numbers/workshops/workshop3.js": """// Workshop 3: Dice Roller
function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}
console.log("Rolled D6:", rollDice(6));""",

    "boolean-and-numbers/workshops/workshop4.js": """// Workshop 4: Even Odd Checker
function isEven(num) {
    return num % 2 === 0;
}
console.log("Is 4 even?:", isEven(4));""",

    "boolean-and-numbers/workshops/workshop5.js": """// Workshop 5: Clearance Discount
function applyDiscount(price, rate) {
    let finalPrice = price - (price * (rate / 100));
    return finalPrice <= 0 ? 0 : finalPrice;
}
console.log("Sale Price:", applyDiscount(100, 25));""",


    # ---------------- objects ----------------
    "objects/labs/lab1.js": """// Lab 1: Object Creation
const course = {
    title: "JavaScript Prep",
    lessons: 30
};
console.log(course);""",

    "objects/labs/lab2.js": """// Lab 2: Property Access
const user = { username: "coder101", score: 95 };
console.log("Dot access:", user.username);
console.log("Bracket access:", user["score"]);""",

    "objects/labs/lab3.js": """// Lab 3: Modifying Objects
let laptop = { brand: "Generic" };
laptop.ram = "16GB"; // addition
laptop.brand = "Premium"; // modification
console.log(laptop);""",

    "objects/labs/lab4.js": """// Lab 4: Object Methods
const dog = {
    name: "Buddy",
    bark: function() { return `${this.name} says Woof!`; }
};
console.log(dog.bark());""",

    "objects/labs/lab5.js": """// Lab 5: Object Iteration
const inventory = { apples: 5, bananas: 8 };
const keys = Object.keys(inventory);
console.log("Inventory categories:", keys);""",

    "objects/workshops/workshop1.js": """// Workshop 1: Inventory Tracker
function updateStock(store, item, quantity) {
    store[item] = (store[item] || 0) + quantity;
    return store;
}
console.log(updateStock({ apples: 2 }, "apples", 3));""",

    "objects/workshops/workshop2.js": """// Workshop 2: Car Dashboard
const vehicle = {
    speed: 0,
    accelerate(amount) {
        this.speed += amount;
        return `Current speed: ${this.speed}mph`;
    }
};
console.log(vehicle.accelerate(25));""",

    "objects/workshops/workshop3.js": """// Workshop 3: Gradebook Assistant
function findAverage(student) {
    let sum = student.grades.reduce((a, b) => a + b, 0);
    return sum / student.grades.length;
}
console.log("Average:", findAverage({ grades: [80, 90, 100] }));""",

    "objects/workshops/workshop4.js": """// Workshop 4: Smart Door Lock
const allowedKeys = { systemKey123: true, masterKey777: true };
function attemptUnlock(key) {
    return allowedKeys[key] === true ? "Unlocked." : "Access Denied.";
}
console.log(attemptUnlock("systemKey123"));""",

    "objects/workshops/workshop5.js": """// Workshop 5: Todo Manager
const todoList = {
    tasks: { "Task 1": "Pending" },
    completeTask(name) {
        if (this.tasks[name]) this.tasks[name] = "Completed";
        return this.tasks;
    }
};
console.log(todoList.completeTask("Task 1"));""",
}

# Execution loop to build directory directories and fill them
for path, code in repo_structure.items():
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, "w") as f:
        f.write(code)

print("Rebuilt structure successfully. Open your project folder to view the files.")

