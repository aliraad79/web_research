const express = require('express')

const app = express()
const port = 3000

const celery = require('celery-node');

const celery_client = celery.createClient(
    "amqp://",
    "amqp://"
);

const worker = celery.createWorker(
    "amqp://",
    "amqp://"
);

worker.register("tasks.add", (a, b) => a + b);
worker.start();

const schedule = require('node-schedule');

const job = schedule.scheduleJob("*/10 * * * * *", function () {
    const task = celery_client.createTask("tasks.add");
    const result = task.applyAsync([2, 5]);

    result.get().then(data => {
        console.log("Result is : " + data);
    });
});


app.get('/add-task', (req, res) => {
    const num1 = Number(req.query.num1);
    const num2 = Number(req.query.num2);

    const task = celery_client.createTask("tasks.add");
    const result = task.applyAsync([num1, num2]);
    result.get().then(data => {
        console.log("Result is : " + data);
    });
    res.send("Task send to celery");
})

app.listen(port, () => {
    console.log("Node Started at port " + port)
})
