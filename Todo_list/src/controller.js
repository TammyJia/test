const fs = require("fs")

const {
  asyncReadFile,
  asyncWriteFile
} = require('./dao')

exports.getTaskbyid = async (req, res) => {
  const id = req.params.id
  const file = await asyncReadFile(req.app.locals.dataFilePath)
  const accounts = JSON.parse(file).filter(v => v.id == id);
  accounts.length == 0 ? res.status(404).send('Can\'t find the task by id: '+id+' .') : res.send("<h2>According to id: " + id +"</h2>" + accounts[0]['content'])
}

exports.getAlltasks = (req, res) => fs.readFile(req.app.locals.dataFilePath, "utf-8", (err, data) => {
  if (err) {
    return res.status(500).send()
  }
  senddata = JSON.parse(data);
  var final = '<h2>TODO List</h2>'
  for(var num = 1; num <= senddata.length; num++){
      final += num + '、' + senddata[num-1]["content"] + '<br/>'
  }
  res.send(final)
})

exports.createTask = async (req, res) => {
  const newAccount = req.body;
  // 获取当前时间
  var myDate = new Date();
  newAccount.createdTime = myDate;

  const file = await asyncReadFile(req.app.locals.dataFilePath)
  const accounts = JSON.parse(file)
  if (accounts.filter(v => v.id == newAccount.id).length != 0) {
    res.status(400).send("id can\'t repeat.")
  } else {
    accounts.push(newAccount)
    await asyncWriteFile(JSON.stringify(accounts), req.app.locals.dataFilePath)
    res.status(201).send(accounts)
  }
}

exports.deleteTask = async (req, res) => {
  const id = req.params.id
  const file = await asyncReadFile(req.app.locals.dataFilePath)
  const accounts = JSON.parse(file)
  const newAccounts = accounts.filter(v => v.id != id)
  if (newAccounts.length === accounts.length) {
    res.status(404).send("Can\'t find current id. Delete failed.")
  } else {
    await asyncWriteFile(JSON.stringify(newAccounts), req.app.locals.dataFilePath)
    res.send("Delete successed.")
  }
}
