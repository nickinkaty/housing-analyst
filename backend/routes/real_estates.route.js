import express from "express";

import { createRealEstates } from "../controllers/real_estates.controller.js";

const router = express.Router();

// REAL ESTATE ROUTES
router.post("/realestates", createRealEstates);
// router.post("/auth/signin", siginUser);
// router.get("/users/first_name", searchFirstnameOrLastname);

export default router;
