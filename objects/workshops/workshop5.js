// Workshop 5: Todo Manager
const todoList = {
    tasks: { "Task 1": "Pending" },
    completeTask(name) {
        if (this.tasks[name]) this.tasks[name] = "Completed";
        return this.tasks;
    }
};
console.log(todoList.completeTask("Task 1"));