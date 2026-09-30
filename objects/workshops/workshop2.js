// Workshop 2: Car Dashboard
const vehicle = {
    speed: 0,
    accelerate(amount) {
        this.speed += amount;
        return `Current speed: ${this.speed}mph`;
    }
};
console.log(vehicle.accelerate(25));