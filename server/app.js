const express = require('express')
const config = require('./config.js')
const bodyParser = require('body-parser')
const router = express.Router()

const app = express()
app.listen(config.app.port, () => console.log('Listening on port 3000...'))

//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

router.post('/create/cards', (request, response) => {
    //code to perform particular action.
    //To access POST variable use req.body()methods.
    console.log(request.body)
})

// add router in the Express app.
app.use("/", router)

app.get('/cards', (request, response) => {
    response.send("ok")
})

