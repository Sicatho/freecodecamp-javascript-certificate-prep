// Workshop 2: Tip Calculator
function calculateBill(subtotal, tipPercent) {
    let tip = subtotal * (tipPercent / 100);
    return subtotal + tip;
}
console.log("Total due:", calculateBill(50, 15));