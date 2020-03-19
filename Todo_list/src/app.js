const express = require('express')
const {
    getAlltasks,
    getTaskbyid,
    createTask,
    deleteTask
} = require('./controller')

const app = express()
app.locals.dataFilePath = "./data.json"

const port = 8080

app.use(express.json())
app.get('/', function(req, res){
    res.send('<h1>Hi, Welcome to Tammy\'s homework! TODO List!</h1>')
})
app.get("/api/tasks", getAlltasks)
app.post("/api/tasks", createTask)
app.get("/api/tasks/:id", getTaskbyid)
app.delete("/api/tasks/:id", deleteTask)

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

exports.app = app
