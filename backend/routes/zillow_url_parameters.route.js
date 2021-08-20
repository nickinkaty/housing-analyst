import express from "express";

import { createZillowUrlParameters } from "../controllers/zillow_url_parameters.controller.js";

const router = express.Router();

// REAL ESTATE ROUTES
router.post("/zillowUrlParameters", createZillowUrlParameters);
// router.post("/auth/signin", siginUser);
// router.get("/users/first_name", searchFirstnameOrLastname);

export default router;
