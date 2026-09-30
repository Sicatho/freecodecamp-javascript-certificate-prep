// Workshop 3: URL Builder
function buildUrl(host, route) {
    return "https://" + host + "/" + route;
}
console.log(buildUrl("freecodecamp.org", "learn"));