// Workshop 1: Inventory Tracker
function updateStock(store, item, quantity) {
    store[item] = (store[item] || 0) + quantity;
    return store;
}
console.log(updateStock({ apples: 2 }, "apples", 3));