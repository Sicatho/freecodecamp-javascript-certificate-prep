// Workshop 5: Clearance Discount
function applyDiscount(price, rate) {
    let finalPrice = price - (price * (rate / 100));
    return finalPrice <= 0 ? 0 : finalPrice;
}
console.log("Sale Price:", applyDiscount(100, 25));