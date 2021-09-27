import express from "express";

import {
  createZillowUrlParameters,
  getAllZillowUrlParameters,
} from "../controllers/zillow_url_parameters.controller.js";

const router = express.Router();

// REAL ESTATE ROUTES
router.post("/", createZillowUrlParameters);
// router.post("/auth/signin", siginUser);
router.get("/", getAllZillowUrlParameters);

export default router;
