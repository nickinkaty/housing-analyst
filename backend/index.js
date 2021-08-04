import express from "express";
import cors from "cors";
import pool from "./db/db";
import dotenv from "dotenv";

// CONFIGURE DOTENV
dotenv.config();

const app = express();

// MIDDLEWARE
app.use(cors());
app.use(express.json());

app.listen(process.env.API_PORT, () => {
  console.log(`We are live on ${process.env.API_PORT}`);
});
