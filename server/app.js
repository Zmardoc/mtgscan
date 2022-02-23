import express from 'express'
import config from './config.js'

const app = express()
app.listen(config.app.port, () => console.log('Listening on port 3000...'));

app.get('/cards', (req, response) => {
    response.send(movies);
});