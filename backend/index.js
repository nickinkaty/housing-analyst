import express from "express";
import cors from "cors";
import dotenv from "dotenv";

// ROUTES IMPORT
import realEstateRoute from "./routes/real_estate.route.js";
import regionIdRoute from "./routes/zillow_url_parameters.route.js";

// CONFIGURE DOTENV
dotenv.config();

const app = express();

// MIDDLEWARE
app.use(cors());
// Add middleware for parsing JSON and urlencoded data and populating `req.body`
app.use(express.urlencoded({ extended: false }));
app.use(express.json({ limit: "50mb" }));

// ROUTES
app.use(`${process.env.API_BASE_URL}/realestates`, realEstateRoute);
app.use(`${process.env.API_BASE_URL}/zillowUrlParameters`, regionIdRoute);

app.listen(process.env.API_PORT, process.env.LISTEN_IP, () => {
  console.log(process.env.LISTEN_IP, process.env.API_BASE_URL);
  console.log(`We are live on ${process.env.API_PORT}`);
});

export default app;
