const express = require("express");
const app = express();
const cors = require("cors");

require("dotenv").config();
const { pool } = require("./services/db");

// MIDDLEWARE
app.use(cors());
app.use(express.json());

app.listen(process.env.API_PORT, () => {
  console.log(process.env.API_PORT);
});
