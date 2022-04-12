import mysql from 'mysql';
import config from './config.js';

var dbConnection = mysql.createConnection({
  host: config.db.host,
  user: config.db.user,
  password: config.db.password,
  database: config.db.database
});

dbConnection.connect(err => {
  if (err) throw err;
  console.log('Connected!');

  dbConnection.query("INSERT INTO mtg_card (card_name, card_description)VALUES ('testovaci karticka', 'popis');", function (err, result) {
    if (err) throw err;
    console.log("Result: " + result);
  });
});
