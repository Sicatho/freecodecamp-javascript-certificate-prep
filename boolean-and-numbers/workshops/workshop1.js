// Workshop 1: Age Gate
function verifyAge(age) {
    if (age >= 18) {
        return "Access Granted.";
    }
    return "Access Denied: Under 18.";
}
console.log(verifyAge(20));