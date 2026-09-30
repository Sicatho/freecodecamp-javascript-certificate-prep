// Workshop 3: Gradebook Assistant
function findAverage(student) {
    let sum = student.grades.reduce((a, b) => a + b, 0);
    return sum / student.grades.length;
}
console.log("Average:", findAverage({ grades: [80, 90, 100] }));