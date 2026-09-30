// Workshop 3: Dice Roller
function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}
console.log("Rolled D6:", rollDice(6));