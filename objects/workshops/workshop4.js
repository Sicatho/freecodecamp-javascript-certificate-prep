// Workshop 4: Smart Door Lock
const allowedKeys = { systemKey123: true, masterKey777: true };
function attemptUnlock(key) {
    return allowedKeys[key] === true ? "Unlocked." : "Access Denied.";
}
console.log(attemptUnlock("systemKey123"));