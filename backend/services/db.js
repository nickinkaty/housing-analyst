const pg = require("pg");

const config = {
  user: process.env.DB_USER, //this is the db user credential
  database: process.env.DB,
  password: process.env.DB_PASS,
  port: process.env.DB_PORT,
  max: process.env.DB_MAX, // max number of clients in the pool
  idleTimeoutMillis: process.env.DB_ITM,
};

const pool = new pg.Pool(config);

pool.on("connect", () => {
  console.log("connected to the Database");
});
