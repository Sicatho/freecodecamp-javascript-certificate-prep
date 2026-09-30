// Workshop 4: Receipt Formatter
function formatReceiptItem(item, price) {
    return `${item.padEnd(15, ".")} $${price.toFixed(2)}`;
}
console.log(formatReceiptItem("Coffee", 3.5));