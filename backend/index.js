import express from "express";
import cors from "cors";
import dotenv from "dotenv";

// ROUTES IMPORT
import realEstateRoute from "./routes/real_estates.route.js";

// CONFIGURE DOTENV
dotenv.config();

const app = express();

// MIDDLEWARE
app.use(cors());
// Add middleware for parsing JSON and urlencoded data and populating `req.body`
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// ROUTES
app.use(process.env.API_BASE_URL, realEstateRoute);

app.listen(process.env.API_PORT, () => {
  console.log(process.env.API_BASE_URL);
  console.log(`We are live on ${process.env.API_PORT}`);
});

export default app;
